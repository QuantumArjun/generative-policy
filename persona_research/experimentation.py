from create_participant import sample_participant
from agents.human import human_LLM
from agents.digital_twin import twin_LLM
from agents.optimizer import optimizer_LLM
from agents.lm_questioner import questioner_llm
import logger as logging
import args
import random
import ast
from scoring import *

from data.data_processor import anes_key_question, w26_key_question, w27_key_question, w29_key_question, w32_key_question, w34_key_question, w36_key_question, w41_key_question, w42_key_question, w43_key_question, w45_key_question, w49_key_question, w50_key_question, w54_key_question, w82_key_question, w92_key_question

from data.data_processor import anes_key_fields, w26_key_fields, w27_key_fields, w29_key_fields, w32_key_fields, w34_key_fields, w36_key_fields, w41_key_fields, w42_key_fields, w43_key_fields, w45_key_fields, w49_key_fields, w50_key_fields, w54_key_fields, w82_key_fields, w92_key_fields


# here, create the whole pipeline in create_participant, simulate_participant, and output data from GPT to a text file

def run_optimization():
    twin_llm = twin_LLM(model_name=args.model_name)       # LM for digital twins
    optim_llm = optimizer_LLM(model_name=args.model_name)     # LM for optimizer
    question_llm = questioner_llm(model_name=args.model_name)    # LM for the questioner

    #Get the Key Questions and their Indices 
    train_indices = []
    val_indices = []
    context_indices = []
    all_indices = []
    chosen_participants_train = []

    sampling = True
    while sampling == True: 
        if args.dataset.value[0] == "ANES":
            key_indices = [0, 10]
        else:
            train_indices = random.sample(range(0, args.dataset.value[1]), args.num_train_questions)
            val_indices = random.sample(range(0, args.dataset.value[1]), args.num_val_questions)
            context_indices = random.sample(range(0, args.dataset.value[1]), args.num_optimizer_context)
            all_indices = train_indices + val_indices

        #Sample n participants from the dataset
        result, chosen_participants_train, chosen_participants_test = sample_participant(all_indices)

        if result == False:
            logger.info("Not enough participants with key fields, resampling...")
        else:
            sampling = False

    train_questions, train_answer_choices = get_key_questions(train_indices)
    val_questions, val_answer_choices = get_key_questions(val_indices)
    context_questions, context_answer_choices = get_key_questions(context_indices)

    logger.info(f"Train Questions: {train_questions}")

    logger.info(f"Key Answer Choices: {train_answer_choices}")

    logger.info(f"Val Questions: {val_questions}")

    logger.info(f"Key Answer Choices: {val_answer_choices}")

    logger.info(f"Context Questions: {context_questions}")

    all_indices = train_indices + val_indices
    print("All Indices: ", all_indices)

    #Sets the Optimizer Task and the train question 
    optim_task = args.Optimizer_Task
    optim_task += f"Here are examples of questions that digital twin might be asked. Note, the actual questions will be different, but these just indicate the domain of questions that will be asked. \n {context_questions} \n"
    optim_llm.set_optim_task(optim_task)
    optim_llm.set_key_questions(train_questions)
    optim_llm.set_context(context_questions)

    #We get an initial set of instructions from the Optimizer LLM
    initial_instructions = optim_llm.create_initial_prompt()

    # Turn them into humans
    all_humans_train = create_humans(chosen_participants_train, train_questions, train_indices, val_questions, val_indices)

    if args.run_test:
        all_humans_test = create_humans(chosen_participants_test, train_questions, train_indices, val_questions, val_indices)

    #Set first time variables
    scores = []
    val_scores = []
    test_train_scores = []
    test_val_scores = []
    instruction = initial_instructions

    # Run Baseline
    logger.info("Baseline")
    baseline_train_score, baseline_val_score = baseline(all_humans_train, train_questions, train_answer_choices, val_questions, val_answer_choices, train_indices, val_indices)

    #If test exists
    baseline_test_train_score = None
    baseline_test_val_score = None

    if args.run_test:
        logger.info("Baseline Test")
        baseline_test_train_score, baseline_test_val_score = baseline(all_humans_test, train_questions, train_answer_choices, val_questions, val_answer_choices, train_indices, val_indices)

    for j in range(args.steps):
        logger.info(f"Optimizer Step {j}")

        # STEP 1: Set the prompt for the Questioner
        question_llm.set_prompt(prompt=instruction)

        logger.info(f"Prompt to Questioner: {instruction}")

        #Steps 2 - 4: Run the Human, Agent Questioner Loop
        transcripts, train_responses, val_responses, max_train_score, max_val_score = full_questioner_loop(all_humans_train, question_llm, twin_llm, train_questions, train_answer_choices, val_questions, val_answer_choices, train_indices, val_indices)

        # STEP 5: Use the Optimizer to score the previous results, and create a new questionaire
        result, instruction, score, total, optim_feedback = optim_llm.optimize(transcripts, train_questions, train_answer_choices, instruction, train_responses, max_train_score)

        #Step 6: Evaluate on the Validation Set
        val_score, _ = score_responses(val_questions, val_responses, val_answer_choices)

        logger.info(f"New Prompt to Optimizer:  {optim_feedback}")

        logger.info(f"Optimizer Feedback: {result}")

        scores.append(score)
        val_scores.append(val_score)

        if args.run_test:
            logger.info("Running Test Participants")
            _, _, _, max_test_train_score, max_test_val_score = full_questioner_loop(all_humans_test, question_llm, twin_llm, train_questions, train_answer_choices, val_questions, val_answer_choices, train_indices, val_indices)

            test_train_score, _ = score_responses(train_questions, train_responses, train_answer_choices)
            test_train_scores.append(test_train_score)

            test_val_score, _ = score_responses(val_questions, val_responses, val_answer_choices)
            test_val_scores.append(test_val_score)

            logger.info(f"Test Train Score: {test_train_score}/{max_test_train_score}")

            logger.info(f"Test Val Score: {test_val_score}/{max_test_val_score}")

        logger.info(f"Optimizer Step {j} Train Score: {score}/{max_train_score}")
        logger.info(f"Optimizer Step {j} Val Score: {val_score}/{max_val_score}")

        logger.info("=============================================")

    logger.info(f"Final Instruction: {instruction}")

    
    #Final Baseline Train
    logger.info(f"Final Baseline Train Score: {baseline_train_score}/{max_train_score}")

    #Final Train
    logger.info(f"Final Train Scores (All Rounds): {scores}")

    #Final Baseline Val
    logger.info(f"Final Baseline Val Score: {baseline_val_score}/{max_val_score}")

    #Final Val 
    logger.info(f"Final Val Scores (All Rounds): {val_scores}")

    if args.run_test:
        logger.info("=============================================")
        #Final Baseline Test Train
        logger.info(f"Final Baseline Test Train Score: {baseline_test_train_score}/{max_test_train_score}")

        #Final Test Train
        logger.info(f"Final Test Train Scores (All Rounds): {test_train_scores}")

        #Final Baseline Test Val
        logger.info(f"Final Baseline Test Val Score: {baseline_test_val_score}/{max_test_val_score}")

        #Final Test Val
        logger.info(f"Final Test Val Scores (All Rounds): {test_val_scores}")

def baseline(all_humans, train_questions, train_answer_choices, val_questions, val_answer_choices, train_indices, val_indices):
    #Run the baseline
    train_responses = []
    val_responses = []

    for i, participant in enumerate(all_humans):
        logger.info(f"Participant {i} Identity: {participant.base_identity}")
        human_train_responses = participant.answer_key_questions(train_questions, train_answer_choices, False)
        human_val_responses = participant.answer_key_questions(val_questions, val_answer_choices, False)


        train_responses_actual = get_key_question_answers(participant, train_indices)
        val_responses_actual = get_key_question_answers(participant, val_indices)

        #Logging Responses per Participant

        logger.info(f"Participant {i} Train Responses: {human_train_responses} ")

        logger.info(f"Participant {i} Train Correct Responses: {train_responses_actual}")

        logger.info(f"Participant {i} Val Responses: {human_val_responses} ")

        logger.info(f"Participant {i} Val Correct Responses: {val_responses_actual}")
        
        train_responses.append((human_train_responses, train_responses_actual))
        val_responses.append((human_val_responses, val_responses_actual))
    
    baseline_train_score, _ = score_responses(train_questions, train_responses, train_answer_choices)
    
    baseline_val_score, _ = score_responses(val_questions, val_responses, val_answer_choices)

    max_train_score = len(train_questions) * len(all_humans)
    max_val_score = len(val_questions) * len(all_humans)

    logger.info(f"Baseline Train Score: {baseline_train_score} / {max_train_score}")

    logger.info(f"Baseline Val Score: {baseline_val_score} / {max_val_score}")

    logger.info("=============================================")

    return baseline_train_score, baseline_val_score

def full_questioner_loop(all_humans, question_llm, twin_llm, train_questions, train_answer_choices, val_questions, val_answer_choices, train_indices, val_indices):
    #Reset the Round to Round Variables
    train_responses = []
    val_responses = []
    transcripts = []
    max_train_score = 0
    max_val_score = 0

    for i, human in enumerate(all_humans): 
        # TODO: double check to make sure participants are numbered for other datasets/human classes too 
        logger.info(f"Evaluating Participant {i}")

        # STEP 2: Imitate the base human (for now, we use a Priveledged LLM)

        logger.info(f"Participant {i} Identity: {human.identity}")

        # STEP 3: Run the Human, Agent Questioner Loop 
        transcript = human_questioner_loop(human, question_llm)
        transcript = transcript.replace("\n", " ")
        transcript = transcript.replace("Q: Q:", "Q:")

        transcripts.append(transcript)
        
        #STEP 4: Use the Questionare to create a digital twin, and ask it key question
        twin_llm.create_identity_from_questionaire(human.base_identity, transcript)
        twin_train_responses = twin_llm.answer_key_questions(train_questions, train_answer_choices)

        #Step 4.5, now do it on the Val questions 
        twin_val_responses = twin_llm.answer_key_questions(val_questions, val_answer_choices)

        # Getting a list of the participant's actual answers to the key questions
        train_responses_actual = get_key_question_answers(human, train_indices)
        val_responses_actual = get_key_question_answers(human, val_indices)


        #Adding this responses to a list
        train_responses.append((twin_train_responses, train_responses_actual))
        val_responses.append((twin_val_responses, val_responses_actual))

        print("Evaluating Digital Twin....")

        # Logging
        logger.info(f"Twin {i} Background {twin_llm.identity}")

        logger.info(f"Twin {i} Train Responses: {twin_train_responses} ")

        logger.info(f"Participant {i} Train Correct Responses: {train_responses_actual}")

        logger.info(f"Twin {i} Val Responses: {twin_val_responses} ")

        logger.info(f"Participant {i} Val Correct Responses: {val_responses_actual}")

        max_train_score += len(train_questions)
        print("Max Train Score: " + str(max_train_score))

        max_val_score += len(val_questions)
        print("Max Val Score: " + str(max_val_score))
    
    return transcripts, train_responses, val_responses, max_train_score, max_val_score
        

def human_questioner_loop(human, questioner):
    transcript = ""
    questioner.set_history(transcript)

    for i in range(args.num_questions):
        #Question Creator asks a Question
        question = questioner.generate_question()

        logger.info(f"Question #{i}: {question}")

        #Human Simulator answers the quesiton
        response = human.answer_question(question)

        logger.info(f"Response #{i}: {response}")

        #Conversation is recorded in the transcript
        transcript += "Q: " + question + "\nA: " + response + "\n\n"
        questioner.set_history(transcript)
        
        logger.info("\n--New Question--")

    return transcript

def key_question_answer_pairs(key_questions, train_indices, participant, include_context=True):
    # function takes in the indices (list) of the key question fields, as well as the human, and returns a string concateniating the questions and the answers

    actual_results = get_key_question_answers(participant, train_indices)
    result = ""
    if include_context:
        result = "\nThis is how you answered previous questions. DO NOT reveal the answers to these questions while answering."
    for i in range(len(key_questions)):
        result += "\nQuestion: " + key_questions[i] + " " + "\nYour Previous Answer: " + actual_results[i] + " \n"
    
    if include_context:
        result += "\nAnswer questions based on the above information. Be as consistent to this persona as possible."
    
    return result

def get_key_question_answers(participant, indices):
    # function take in the indices (list) of the key question fields and returns a list with the key data 
    actual_results = [] 
    for i in indices: 
        actual_results.append(participant.participant_object.all_fields[i])
    return actual_results 

def create_humans(chosen_participants, train_questions, train_indices, val_questions, val_indices):
    human_list = []
    for participant in chosen_participants:
        identity_paragraph = participant.identityParagraph()
        human = human_LLM(model_name=args.model_name)
        human.set_base_identity(identity_paragraph)
        human.set_participant_object(participant)
        
        identity_paragraph += key_question_answer_pairs(train_questions, train_indices, human)
        human.set_train_identity(identity_paragraph)

        identity_paragraph += key_question_answer_pairs(val_questions, val_indices, human, False)
        human.set_identity(identity_paragraph)

        human_list.append(human)
    
    return human_list

def get_key_questions(indices):
    questions, answer_choices = [], []
    master_list, key_fields = [], []
    
    if args.dataset.value[0] == "ANES":
        key_questions = ["Key Question: Who did you vote for in the 2012 election? And if you didn't, who would you have voted for? Give only the last name of the predicted candidate, and no other words.", "Key Question: Do you discuss politics with your friends? Answer with only yes or no."]
        key_answer_choices = [["Obama", "Romney"], ["Yes", "No"]]
        return key_questions, key_answer_choices

    elif args.dataset.value[0] == "w26":
        master_list = w26_key_question
        key_fields = w26_key_fields
    elif args.dataset.value[0] == "w27":
        master_list = w27_key_question
        key_fields = w27_key_fields
    elif args.dataset.value[0] == "w29":
        master_list = w29_key_question
        key_fields = w29_key_fields
    elif args.dataset.value[0] == "w32":
        master_list = w32_key_question
        key_fields = w32_key_fields
    elif args.dataset.value[0] == "w34":
        master_list = w34_key_question
        key_fields = w34_key_fields
    elif args.dataset.value[0] == "w36":
        master_list = w36_key_question
        key_fields = w36_key_fields
    elif args.dataset.value[0] == "w41":
        master_list = w41_key_question
        key_fields = w41_key_fields
    elif args.dataset.value[0] == "w42":
        master_list = w42_key_question
        key_fields = w42_key_fields
    elif args.dataset.value[0] == "w43":
        master_list = w43_key_question
        key_fields = w43_key_fields
    elif args.dataset.value[0] == "w45":
        master_list = w45_key_question
        key_fields = w45_key_fields
    elif args.dataset.value[0] == "w49":
        master_list = w49_key_question
        key_fields = w49_key_fields
    elif args.dataset.value[0] == "w50":
        master_list = w50_key_question
        key_fields = w50_key_fields
    elif args.dataset.value[0] == "w54":
        master_list = w54_key_question
        key_fields = w54_key_fields
    elif args.dataset.value[0] == "w82":
        master_list = w82_key_question
        key_fields = w82_key_fields
    elif args.dataset.value[0] == "w92":
        master_list = w92_key_question
        key_fields = w92_key_fields

    temp_results = [] 
    
    print(indices)
        
    for i in indices:
        temp_results.append(master_list[key_fields[i]])
    
    for result in temp_results:
        questions.append(result[0])
        unprocessed_choices = result[1]
        list_converted = ast.literal_eval(unprocessed_choices)
        if "Refused" in list_converted:
            list_converted.remove("Refused")
        answer_choices.append(list_converted)
    
    return questions, answer_choices

if __name__ == "__main__":
    logger = logging.create_logger()
    logger.info("Arguments")
    logger.info(f"Dataset {args.dataset.value[0]}")
    logger.info(f"Model Name {args.model_version}")  
    logger.info(f"# Steps {args.steps}")
    logger.info(f"# Participants Sampled (Train) {args.num_participants_train}")
    logger.info(f"# Participants Sampled (Test) {args.num_participants_test}")
    logger.info(f"# Train Questions {args.num_train_questions}")
    logger.info(f"# Val Questions {args.num_val_questions}")
    logger.info(f"# Optimizer Context {args.num_optimizer_context}")
    run_optimization()
