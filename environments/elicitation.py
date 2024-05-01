"""
Module: elicitation.py
Author: akaranam
Description: This module contains the classes for the overall elicitation environment.
"""

class ElicitationEnvironment:
    def __init__(self, agents):
        self.all_agents = agents
    
    def run_questioner(self):
        for agent in self.all_agents:
            agent.ask_question()
    



