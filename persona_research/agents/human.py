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

class human_LLM:
    def __init__(self, model_name):
        if model_name == "openai" and not args.use_crfm:
            os.environ["OPENAI_API_KEY"] = openai_key
            self.model = ChatOpenAI(model_name=args.model_version)
        # elif model_name == "openai" and args.use_crfm:
        #     CRFM_API_KEY = os.getenv("CRFM_API_KEY")
        #     self.model = crfmChatLLM(model_name="openai/gpt-4-0314", max_tokens=args.question_answering_max_tokens, temperature=args.temperature)
        elif model_name == "claude":
            self.model = anthropic.Anthropic(api_key=claude_key)

            
        self.identity = ""
        self.base_identity = ""
        self.train_identity = ""
        self.participant_object = None

        #add new models here
    
    def set_identity(self, identity_paragraph):
        self.identity = identity_paragraph

    def set_train_identity(self, train_identity_paragraph):
        self.train_identity = train_identity_paragraph
    
    def set_base_identity(self, base_identity):
        self.base_identity = base_identity
    
    def set_participant_object(self, participant_object):
        self.participant_object = participant_object
    
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

    def answer_key_questions(self, key_questions, key_answer_choices, use_extended_identity=False):
        answers = []

        answer_choices_text = ""

        for i, key_question in enumerate(key_questions):
            local_answer_choices_text = answer_choices_text
            local_answer_choices_text += key_question
            local_answer_choices_text += " ".join(f"{chr(97 + i)}) {item}" for i, item in enumerate(key_answer_choices[i]))
            local_answer_choices_text += "Answer using only the answer choice. For example, if your answer is 'a) Cat', respond with just 'Cat'.\n"

            if use_extended_identity:
                messages = [
                    SystemMessage(content=self.identity),
                    HumanMessage(content=local_answer_choices_text),
                ]
            else: 
                messages = [
                    SystemMessage(content=self.base_identity),
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
                    system=self.base_identity,
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