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
    
    