"""
Module: digital_representative.py
Author: akaranam
Description: This module contains the classes for the digital representatives of the original humans.
"""

from agents.agent import Agent

class DigitalRepresentative(Agent):
    def __init__(self, system_prompt, model_config, human_agent):
        super().__init__(system_prompt=system_prompt, model_config=model_config)
        self.human_agent = human_agent
        self.history = []
    
    def initialize_representative():
        """
        Use the human's conversation to create a digital representative
        """



