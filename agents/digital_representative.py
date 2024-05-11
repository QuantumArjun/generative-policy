"""
Module: digital_representative.py
Author: akaranam
Description: This module contains the classes for the digital representatives of the original humans.
"""

from agents.agent import Agent
from utils import name_generator as NameGenerator

class DigitalRepresentative(Agent):
    def __init__(self, model_config, human_agent, name=None):
        """
        Initializes a DigitalRepresentative object with the given human agent.
        """
        super().__init__(system_prompt=self.initialize_representative(human_agent), model_config=model_config)
        self.history = []
        if name:
            self.name = name
        else:  
            self.name = NameGenerator.generate_random_first_name()
    
    def initialize_representative(human_agent):
        """
        Use the human's conversation to create a digital representative
        """

        system_prompt = "You are trying to emulate a human agent. The human agent you are trying to emulate has the following conversation history: \n"
        for message in human_agent.history:
            system_prompt += f"{message}\n"
        
        return system_prompt




