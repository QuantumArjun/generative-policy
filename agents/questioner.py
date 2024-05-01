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