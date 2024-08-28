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

        system_prompt = "You are trying to how a specific human might respond policies. The human you are trying to emulate has the following conversation history: \n. "
        for message in human_agent.history:
            system_prompt += f"{message}\n"
        
        return system_prompt




