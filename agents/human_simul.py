"""
Module: human_simul.py
Author: akaranam
Description: This module simulates a human agent interacting with the system.
"""

from agents.agent import Agent

class HumanSimulator(Agent):
    def __init__(self, system_prompt, model_config):
        super().__init__(system_prompt=system_prompt, model_config=model_config)
        self.history = []
        self.initial_opinion = ""
        self.final_opinion = ""
    
    def rate_opinion(self, opinion) -> str:
        """
        Rate an opinion
        """
        user_message = f"Based on your beliefs, please rate the following opinion: {opinion}. Output only one of two options: 'agree' or 'disagree'."
        response = self.respond(user_message=user_message)

        if response == "agree":
            return 1
        elif response == "disagree":
            return 0
        else:
            return -1
    
    