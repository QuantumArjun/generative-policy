'''
Sim_Human: 

Identity 
- LLM Familarity
- LLM Frequency 
- LLM Self-Description 
- LLM System String
- Age 
- Gender 
- Employment 
- Education 
- Marital 
- Religion 
- Ethnicity 
- Location 
- Stated Preferences 

"Questions" 
- Given two model responses, which one would you pick? (We just look at the turn one responses)
 - Which one they picked 
 - Why they picked it (text description, as well as a ranking of values, fluency, factuality, safety, diversity, creativity, helpfulness)

 Task, we want the persona to pick the right model, as well as give the justification as to why (citing the top value) 

 Engineering Tasks
 - Step 1: Construct the Simualted Humans from the survey responses (We can then go from there )
    - Identity paragraph, value preferences, and conversation information 
    - 2 options, which one they picked, and why they picked that one 
 - Step 2: 
'''

from create_participant import sample_participant
from agents.human import human_LLM
from agents.digital_twin import twin_LLM
from agents.optimizer import optimizer_LLM
from agents.lm_questioner import questioner_llm
from agents.meta_questioner import meta_questioner_llm
import logger as logging
import args
import random
import ast
from scoring import *
from data.PRISM.prism_dataset import get_prism_data

def run_optimization():
    twin_llm = twin_LLM(model_name=args.model_name)       # LM for digital twins
    optim_llm = optimizer_LLM(model_name=args.model_name)     # LM for optimizer
    question_llm = questioner_llm(model_name=args.model_name)    # LM for the questioner
    meta_question_llm = meta_questioner_llm(model_name=args.model_name)    # LM for the meta questioner

    #Load in full participants dataset
    participants = get_prism_data()

    #Sample Participants
    chosen_participants = sample_participant(participants, args.num_participants_train)

    #Sets the Optimizer Task
    optim_task = args.Optimizer_Task
    optim_llm.set_optim_task(optim_task)

    # Use the Participant class to insantiate a human LLM 
    all_humans = create_humans(chosen_participants)

    #Select one human (for now)
    chosen_participant = all_humans[0]

    print("Number of conversation", len(chosen_participant.participant_object.conversation_preferences))

    #Set the Context for the Meta Questioner - hardcode this one in 
    meta_question_llm.set_domain(task="PRISM_domain")

    last_transcript = ""
    persona_scores =[]

    for j in range(args.steps):
        logger.info(f"Optimizer Step {j}")

        #Step 0 - Answer Questions (inital) 
        persona_reponses = twin_llm.answer_prism_questions(chosen_participant)

        #Step 0 - Calculate scores 
        persona_score = score_prism_responses(persona_reponses)
        print("Initial Score", persona_score)
        
        #Step 1: Display Current Persona 
        logger.info(f"Current Persona: {twin_llm.identity}")

        #Step 2: Get Instructions for Questioner
        instruction = meta_question_llm.generate_question_instructions()
        logger.info(f"Questioner Instructions: {instruction}")

        #Step 3: Give instructions to Questioner 
        question_llm.set_prompt(prompt=instruction)
        
        print("Simulated Human Identity: ", chosen_participant.identity)

        #Step 4: Run Simulated Human, Agent Quesitoner Loop 
        human_transcript = single_questioner_loop(chosen_participant, question_llm, "Human")
        logger.info(f"Human Transcript: {human_transcript}")

        last_transcript = human_transcript

        #Step 5: Run Digital Twin, Agent Questioner Loop 
        twin_transcript = single_questioner_loop(twin_llm, question_llm, "Twin")
        logger.info(f"Digital Twin Transcript: {twin_transcript}")

        #Step 6: Show both to optimizer and get revised persona
        result, revised_persona = optim_llm.revise_instructions(twin_llm.identity, human_transcript, twin_transcript)
        logger.info(f"Optimizer Result: {result}")

        #Step 7: Update Digital Twin Persona 
        twin_llm.append_persona_instructions(revised_persona)

    #Output Final Persona 
    logger.info(f"Final Persona: {twin_llm.identity}")

    #Persona 
    twin_llm.set_identity(twin_llm.identity)
    logger.info(f"Created Persona Identity {twin_llm.identity}")
    persona_reponses = twin_llm.answer_prism_questions(chosen_participant)
    persona_score, max_score = score_prism_responses(persona_reponses)

    #Transcript 
    twin_llm.set_identity(last_transcript)
    logger.info(f"Created Transcript Identity {twin_llm.identity}")
    transcript_responses = twin_llm.answer_prism_questions(chosen_participant)
    transcript_score, max_score = score_prism_responses(transcript_responses)

    #Identity 
    twin_llm.set_identity(chosen_participant.participant_object.identity_paragraph)
    logger.info(f"Created Base Identity {twin_llm.identity}")
    base_responses = twin_llm.answer_prism_questions(chosen_participant)
    identity_score, max_score = score_prism_responses(base_responses)
    
    #Simulated Human Performance
    twin_llm.set_identity(chosen_participant.identity)
    logger.info(f"Created Simulated Human Identity {twin_llm.identity}")
    sim_human_responses = twin_llm.answer_prism_questions(chosen_participant)
    sim_human_score, max_score = score_prism_responses(sim_human_responses)
    
    #Nothing 
    twin_llm.set_identity("I have no preferences")
    logger.info(f"Created Nothing Identity {twin_llm.identity}")
    nothing_response = twin_llm.answer_prism_questions(chosen_participant)
    nothing_score, max_score = score_prism_responses(nothing_response)
    


    logger.info(f"Persona Score: {persona_score}")
    # logger.info(f"Persona Responses: {persona_reponses}")
    
    logger.info(f"Transcript Score: {transcript_score}")
    # logger.info(f"Transcript Responses: {transcript_responses}")
    
    
    logger.info(f"Identity Score: {identity_score}")
    # logger.info(f"Identity Responses: {base_responses}")
    
    logger.info(f"Simulated Human Score: {sim_human_score}")
    # logger.info(f"Simulated Human Responses: {sim_human_responses}")
    
    logger.info(f"Nothing Score: {nothing_score}")
    # logger.info(f"Nothing Responses: {nothing_response}")

    logger.info(f"Max Score: {max_score}")


def sample_participant(participants, num_participants):
    return random.sample(participants, num_participants)

def create_humans(participants):
    all_humans = []
    for participant in participants: 
        human = human_LLM(model_name=args.model_name)
        human.set_participant_object(participant)
        print(participant.identity_paragraph)
        print(participant.stated_values_paragraph)
        print(participant.conversations_paragraph)
        total_identity = participant.identity_paragraph + "\n" + participant.stated_values_paragraph + "\n" + participant.conversations_paragraph
        human.set_identity(total_identity)
        all_humans.append(human)
    
    return all_humans

def single_questioner_loop(human, questioner, identity):
    transcript = ""
    questioner.set_history(transcript)

    for i in range(args.num_questions):
        #Question Creator asks a Question
        question = questioner.generate_question()

        logger.info(f"{identity} Question #{i}: {question}")

        #Human Simulator answers the quesiton
        response = human.answer_question(question)

        logger.info(f"{identity} Response #{i}: {response}")

        #Conversation is recorded in the transcript
        transcript += "Question Asked: " + question + "\n" + identity + "'s Answer: " + response + "\n\n"
        questioner.set_history(transcript)
        
        logger.info("\n--New Question--")

    return transcript

if __name__ == "__main__":
    logger = logging.create_logger()
    logger.info("Personas Module - PRISM Dataset")
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
