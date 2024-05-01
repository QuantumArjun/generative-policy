"""
Module: questioner.py
Author: akaranam
Description: This module creates a questioner agent for generating questions in a conversation.
"""

from utils.llm_wrapper import LLMWrapper
from agents.agent import Agent

class Questioner(Agent):
    def __init__(self, instructions, model_config):
        super().__init__(instructions, model_config)
        self.history = []

    
    # def generate_question(self) -> str:
    #     """
    #     Generate a question for the conversation
    #     :return: The generated question
    #     """
    #     question_system_prompt = f"""You are an expert questioner in the domain of {self.domain}. Your task is to generate a question that elicits useful information from the user."""
    #     question_message_prompt = f"""Generate a question that elicits useful information from the user in the domain of {self.domain}."""
        
    #     llm = LLMWrapper(self.model_config)
        
    #     response = llm.generate_text(system_prompt=question_system_prompt, user_message=question_message_prompt)

    #     self.history.append(response)

    #     return response