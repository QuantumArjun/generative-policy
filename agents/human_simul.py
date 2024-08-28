"""
Module: human_simul.py
Author: akaranam
Description: This module simulates a human agent interacting with the system.
"""

from agents.agent import Agent

class HumanSimulator(Agent):
    def __init__(self, system_prompt, model_config):
        """
        Initializes a HumanSimulator object with the given system prompt and model configuration.
        
        Args:
            system_prompt (str): The system prompt for the conversation.
            model_config (dict): The configuration for the model.
        """
        super().__init__(system_prompt=system_prompt, model_config=model_config)
        self.history = []
        self.initial_opinion = ""
        self.final_opinion = ""
    
    def rate_opinion(self, opinion) -> int:
        """
        Rate an opinion based on the user's beliefs.
        
        Args:
            opinion (str): The opinion to be rated.
        
        Returns:
            int: The rating of the opinion. 1 for agree, 0 for disagree, -1 for other.
        """
        user_message = f"Based on your beliefs, please rate the following opinion: {opinion}. Output only one of two words, and nothing else: 'agree' or 'disagree'."
        response = self.respond(user_message=user_message, q_tag="<Someone Else's Opinion> ", a_tag="<Your Rating>")

        if response == "agree":
            return 1
        elif response == "disagree":
            return 0
        else:
            return -1
    
    def ask_about_policy(self, policy_prompt) -> str:
        return self.respond(policy_prompt)
    