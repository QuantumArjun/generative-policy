import openai
import langchain
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from api import *
from langchain.schema.messages import HumanMessage, SystemMessage
import re
import args
from scoring import *
import logger as logging
import anthropic

class optimizer_LLM:
    def __init__(self, model_name):
        if model_name == "openai" and not args.use_crfm:
            os.environ["OPENAI_API_KEY"] = openai_key
            self.model = ChatOpenAI(model_name=args.model_version)
        # elif model_name == "openai" and args.use_crfm:
        #     CRFM_API_KEY = os.getenv("CRFM_API_KEY")
        #     self.model = crfmChatLLM(model_name="openai/gpt-4-0314", max_tokens=args.question_answering_max_tokens, temperature=args.temperature)
        elif model_name == "claude":
            self.model = anthropic.Anthropic(api_key=claude_key)

        self.optim_task = ""
    
    def set_optim_task(self, optim_task):
        self.optim_task = optim_task
    
    def revise_instructions(self, current_instructions, human_transcript, twin_transcript):
        prompt = f"Revise the digital twin's persona based on the following transcripts. \
            The assistant's current persona is: \n{current_instructions}\n \
            The assistant's interview with the human is: \n{human_transcript}\n \
            The assistant's interview with the persona is: "

        critique = f"Answer in the following format, focusing on where the human and the persona \
            most diverged, and then how the persona might be improved.\n" 
        critique += "Critique: <Critique> \n"
        critique += "Advice: <Advice to improve> \n"
        critique += "Persona Improvement: <Persona Improvement> \n"

        ending = "You should now use this feedback to create a new and improved persona which must begin with <persona> and end with </persona>, and should be in the first person. \n"

        prompt += critique
        prompt += ending

        messages = [
            SystemMessage(content=self.optim_task),
            HumanMessage(content=prompt),
        ]

        result = ""


        if args.use_crfm:
            result = self.model.generate([messages], stop=["\end"]).generations[0][0].text
        elif args.model_name == "openai":
            result = self.model.invoke(messages).content
        elif args.model_name == "claude":
            result = self.model.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                system=self.optim_task,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ]
                    }
                ]
            ).content[0].text

        new_instruction = self.process_output(result)


        return result, new_instruction


    
    # def set_key_questions(self, key_questions):
    #     self.key_questions = key_questions

    # def add_instruction_score(self, instruction):
    #     self.instruction_history.append(instruction)

    def process_output(self, output):
        # Define the pattern to search for the content between the <instruction> tags
        pattern = r"<persona>(.*?)</persona>"

        # Search for the pattern
        match = re.search(pattern, output, re.DOTALL)

        if match is None:
            print("An error occurred, here's what we got:")
            print(output)
            return output

        # Extract the matched content and strip leading/trailing whitespace
        instruction_content = match.group(1).strip()
        
        return instruction_content


    # def optimize(self, transcripts, key_questions, key_answer_choices, instruction, responses, max_score):

    #     score, all_qs = score_responses(key_questions,responses, key_answer_choices)
    #     self.add_instruction_score((instruction, score))
        
    #     highest_score_tuple = max(self.instruction_history, key=lambda x: x[1])
    #     trajectory = highest_score_tuple[0] + "\n"

    #     updated_optim = f"Below is the last instruction you gave and its score:  \n \"{trajectory} \" \n"

    #     updated_optim += f"This instruction scored {round(highest_score_tuple[1], 2)} out of {max_score} points on the key questions. \n"

    #     # Here we give the optimizer the most missed questions

    #     if len(all_qs) != 0:

    #         missed_question_text = ""

    #         highest_entry = max(all_qs, key=lambda x: x[3])
    #         most_correct_question = highest_entry[0]
    #         most_correct_score = highest_entry[3]

    #         lowest_entry = min(all_qs, key=lambda x: x[3])
    #         most_missed_question = lowest_entry[0]
    #         most_missed_score = lowest_entry[3]

    #         if most_correct_score > most_missed_score:
    #             missed_question_text += "Here is an example of a key question that the assistant got most correct! You should attempt to maintain this performance \n"
                
    #             missed_question_text += "Most Correct Question: " + str(most_correct_question) + "\n"

    #             missed_question_text += "Assistant's Prediction: " + highest_entry[1] + "\n"
    #             missed_question_text += "Human's Preference: " + highest_entry[2] + "\n"

    #         if most_missed_score < 1.0:
    #             missed_question_text += "Here is an example of a key question that the assistant got wrong for a user it interviewed. This prediction from the assistant was after the interviewing phase (Hint: This question should help you learn about the domain). \n"

    #             missed_question_text += "Most Missed Question: " + str(most_missed_question) + "\n"
    #             missed_question_text += "Assistant's Prediction: " + lowest_entry[1] + "\n"
    #             missed_question_text += "Human's Preference: " + lowest_entry[2] + "\n"
    #             missed_question_text += "Here is the assistant’s full interview interview with that human: \n"
    #             missed_question_text += "'" + transcripts[lowest_entry[4]] + "'" + "\n"

    #         updated_optim += missed_question_text

    #         logger = logging.create_logger()
    #         logger.info("Missed Question Dictionary: " + str(all_qs))
    #         logger.info("Most Missed Question: " + str(most_missed_question))


    #         #Here, we give the optimizer a transcript that got this question wrong 
    #         #     print("We've reached an error")
    #         #     print(lowest_entry)
    #         #     print(len(transcripts))
    #         #     print(len(lowest_entry))

    #         # updated_optim += missed_interview_text

    #     # Here, we give the instructions to the optimizer
        
    #     updated_optim += "Generate new instructions for the assistant such that its questions will have a higher score than the set of instructions above, if possible. The question answer pairs between the asistant and the human should contain enough context for a seperate human to answer a set of chosen questions correctly. If you are already at the max score, the instructions should change as little as possible. Your new prompt must begin with <prompt> and end with </prompt>. Remember, the assistant will not have access to previous sets of instructions."

    #     # Critique Step
    #     critique =  "\nAnswer in the following format, focusing on the most missed question, and why that question was missed, as well as the most correct question, and how that performance can be preserved.:\n" 
    #     critique += "Critique: <Critique> \n"
    #     critique += "Advice: <Advice to improve> \n"
    #     critique += "New Instructions: <New instructions> \n"

    #     updated_optim += critique

    #     system_message = self.optim_task
    #     system_message += "\n"

    #     messages = [
    #         SystemMessage(content=system_message),
    #         HumanMessage(content=updated_optim),
    #     ]

    #     result = ""

    #     if args.use_crfm:
    #         result = self.model.generate([messages], stop=["\end"]).generations[0][0].text
    #     else:
    #         result = self.model.invoke(messages).content
    #     prompt = self.process_output(result)[0]

    #     print("\nRound Performance: ", score, "/", max_score)

    #     return result, prompt, score, len(responses), updated_optim

    

