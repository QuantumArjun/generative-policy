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

class questioner_llm:
    def __init__(self, model_name):
        if model_name == "openai" and not args.use_crfm:
            os.environ["OPENAI_API_KEY"] = openai_key
            self.model = ChatOpenAI(model_name=args.model_version)
        # elif model_name == "openai" and args.use_crfm:
        #     CRFM_API_KEY = os.getenv("CRFM_API_KEY")
        #     self.model = crfmChatLLM(model_name="openai/gpt-4-0314", max_tokens=args.question_answering_max_tokens, temperature=args.temperature)
        elif model_name == "claude":
            self.model = anthropic.Anthropic(api_key=claude_key)

        self.prompt = ""
        self.history = ""
        self.prime_directive = "Use the following instructions to generate one question at a time."
    
    def set_prompt(self, prompt):
        self.prompt = prompt
    
    def set_history(self, history):
        self.history = history
    
    def generate_question(self):
        model_query = self.prompt
        if self.history != "":
            model_query = model_query + "\n" + "History \n" + self.history

        messages = [
            SystemMessage(content=self.prime_directive),
            HumanMessage(content=model_query),
        ]

        question = ""

        if args.use_crfm:
            question = self.model.generate([messages], stop=["\end"]).generations[0][0].text
        elif args.model_name == "openai":
            question = self.model.invoke(messages).content
        elif args.model_name == "claude":
            question = self.model.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                system=self.prime_directive,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": model_query
                            }
                        ]
                    }
                ]
            ).content[0].text
        return question

    
