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

class meta_questioner_llm:
    def __init__(self, model_name):
        if model_name == "openai" and not args.use_crfm:
            os.environ["OPENAI_API_KEY"] = openai_key
            self.model = ChatOpenAI(model_name=args.model_version)
        # elif model_name == "openai" and args.use_crfm:
        #     CRFM_API_KEY = os.getenv("CRFM_API_KEY")
        #     self.model = crfmChatLLM(model_name="openai/gpt-4-0314", max_tokens=args.question_answering_max_tokens, temperature=args.temperature)
        elif model_name == "claude":
            self.model = anthropic.Anthropic(api_key=claude_key)
        
        self.domain = ""
        self.prompt = "" 
    
    def generate_question_instructions(self):
        messages = [
            SystemMessage(content=self.prompt),
            HumanMessage(content="Generate the set of instructions:"),
        ]
        if args.use_crfm:
            return self.model.generate([messages], stop=["\end"]).generations[0][0].text
        elif args.model_name == "openai":
            return self.model.invoke(messages).content
        elif args.model_name == "claude":
            return self.model.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                system=self.prompt,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Generate the set of instructions:"
                            }
                        ]
                    }
                ]
            ).content[0].text

    def set_domain(self, domain=None, task="general_domain"):
        self.domain = domain
        self.prompt = f"Your goal is to create an interactive assistant that elicits the preferences and opinions of the user to accurately reflect them. \
            To create the assistant, you can provide instructions to it. There is a cost to the effort the user needs to answer the questions, \
            so you should make sure that the assistant does not ask questions that you already know the answer to or that require too much effort \
            from the user to answer. \n The interactive assistant will only have the opportunity to ask {args.num_questions} questions overall. \n \
            You should ensure that the instructions DO NOT ask the questions from the interaction that you receive. \n"
        
        #Add Context 
        if task == "general_domain":
            self.prompt += f"Here are examples of questions that digital twin might be asked. Note, the actual questions will be different, \
            but these just indicate the type of questions that will be asked. \n {self.domain} \n"

        elif task == "PRISM_domain":
            self.prompt += f"Here is the domain of the questions that the digital twin wil be required to answer. \
                    The digital twin will be required to pick between two models responses, and the reasoning as to why. \
                    The reasoning will be based on picking two of the following qualities: values, creativity, fluency, factuality, diversity, safety \
                    personalization, and helpfulness. \n"
