"""
Module: digital_representative.py
Author: akaranam
Description: This module contains the classes for the digital representatives of the original humans.
"""

from agents.agent import Agent
from utils.name_generator import NameGenerator

class DigitalRepresentative(Agent):
    def __init__(self, model_config, human_agent, name=None):
        """
        Initializes a DigitalRepresentative object with the given human agent.
        """
        super().__init__(system_prompt=self.initialize_representative(human_agent), model_config=model_config)
        self.history = []
        self.name = name
    
    def initialize_representative(self, human_agent):
        """
        Use the human's conversation to create a digital representative
        """

        system_prompt = "You are trying to how a specific human might respond policies. The human you are trying to emulate has answered the following way in an interview: \n. "
        for message in human_agent.history:
            system_prompt += f"{message}\n"
        
        return system_prompt

    def rate_opinion(self, opinion) -> int:
        """
        Rate an opinion based on the user's beliefs.
        
        Args:
            opinion (str): The opinion to be rated.
        
        Returns:
            int: The rating of the opinion. 1 for agree, 0 for disagree, -1 for other.
        """
        user_message = f"Based on the interview, please predict how the human would rate following opinion: {opinion}. Output only one of two words, and nothing else: 'agree' or 'disagree'. Be conservative with agree - only agree if you are very confident that the human would agree."
        response = self.respond(user_message=user_message, q_tag="<Someone Else's Opinion> ", a_tag="<Your Rating>")

        if response == "agree":
            return 1
        elif response == "disagree":
            return 0
        else:
            return -1
    
    def ask_about_policy(self, policy_prompt) -> str:
        return self.respond(policy_prompt)




