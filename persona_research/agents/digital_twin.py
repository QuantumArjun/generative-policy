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
# from crfm.crfm import crfmChatLLM
from api import *
from langchain.schema.messages import HumanMessage, SystemMessage
import args
import anthropic

class twin_LLM:
    def __init__(self, model_name):
        if model_name == "openai" and not args.use_crfm:
            os.environ["OPENAI_API_KEY"] = openai_key
            
            self.model = ChatOpenAI(model_name=args.model_version)
        # elif model_name == "openai" and args.use_crfm:
        #     CRFM_API_KEY = os.getenv("CRFM_API_KEY")
        #     self.model = crfmChatLLM(model_name="openai/gpt-4-0314", max_tokens=args.question_answering_max_tokens, temperature=args.temperature)
        elif model_name == "claude":
            self.model = anthropic.Anthropic(api_key=claude_key)
        
        self.identity = """
            Background and Personality:
            - Age: x
            - Education: x
            - Occupation: x
            - Personal Traits: x

            Public Behavior:
            - Communication Style: x
            - Community Engagement: x

            Political Beliefs and Ideology:
            - Core Beliefs: x
            - Political Alignment: x

            """

        #add new models here
    
    def append_persona_instructions(self, instructions):
        self.identity = instructions
    
    def update_persona_instructions(self, instructions):
        self.identity = instructions
    
    def set_identity(self, identity):
        self.identity = identity
    
    def get_identity(self):
        return self.identity
    
    def answer_question(self, question):
        messages = [
            SystemMessage(content=self.identity),
            HumanMessage(content="Answer the following question in the first person, and answer succinctly using just a few sentences: " + question),
        ]

        answer = ""

        if args.use_crfm:
            answer = self.model.generate([messages], stop=["\end"]).generations[0][0].text
        elif args.model_name == "openai":
            answer = self.model.invoke(messages).content
        elif args.model_name == "claude":
            answer = self.model.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                system=self.identity,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Answer the following question in the first person, and answer succinctly using just a few sentences: " + question
                            }
                        ]
                    }
                ]
            ).content[0].text

        
        answer = answer.strip('\n')
        return answer

    def answer(self, question): 
        messages = [
            SystemMessage(content=self.identity),
            HumanMessage(content=question),
        ]

        answer = ""

        if args.use_crfm:
            answer = self.model.generate([messages], stop=["\end"]).generations[0][0].text
        elif args.model_name == "openai":
            answer = self.model.invoke(messages).content
        elif args.model_name == "claude":
            answer = self.model.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                system=self.identity,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": question
                            }
                        ]
                    }
                ]
            ).content[0].text

        
        answer = answer.strip('\n')
        return answer

    def answer_key_questions(self, key_questions, key_answer_choices):
        answers = []

        answer_choices_text = ""

        for i, key_question in enumerate(key_questions):
            local_answer_choices_text = answer_choices_text
            local_answer_choices_text += key_question
            local_answer_choices_text += " ".join(f"{chr(97 + i)}) {item}" for i, item in enumerate(key_answer_choices[i]))
            local_answer_choices_text += "Answer using only the answer choice. For example, if your answer is 'a) Cat', respond with just 'Cat'.\n"

            messages = [
                SystemMessage(content=self.identity),
                HumanMessage(content=local_answer_choices_text),
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
                    system=self.identity,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": local_answer_choices_text
                                }
                            ]
                        }
                    ]
                ).content[0].text
                
            result = result.replace('\n', '')
            parts = result.split(') ')
            if len(parts) > 1:
                result = parts[1].strip()
            else:
                result = result.strip()
            
            answers.append(result)
        return answers

    def answer_prism_questions(self, participant):
        
        all_answers = []

        for conversation in participant.participant_object.conversation_preferences:
            #Question 1: Choosing the model response 
            question_1 = "You gave two language models the following prompt: " + conversation['opening_prompt'] + "\n"
            question_1 += "Of the two model responses, choose the model response that your prefer. Output only a) or b)\n" 
            question_1_choices = [f" a) '{conversation['chosen']}'", f" b) '{conversation['not_chosen']}'"]
            question_1_choices = "\n".join(f"{item}" for i, item in enumerate(question_1_choices))
            question_1 += question_1_choices

            answer_1 = self.answer_question(question_1)


            #Question 2: Ranking the model responses
            question_2 = "Of the following attributes, choose the two that were most important in your decision. Output only the two attributes. \n"
            question_2_choices = ", ".join(f"{item}" for i, item in enumerate(conversation['ranked_preferences']))
            question_2 += question_2_choices

            answer_2 = self.answer_question(question_2)

            correct_answer_1 = "a)"
            correct_answer_2 = [conversation['ranked_preferences'][0], conversation['ranked_preferences'][1]]
            
            all_answers.append((answer_1, correct_answer_1))
            all_answers.append((answer_2, correct_answer_2))

        return all_answers




        