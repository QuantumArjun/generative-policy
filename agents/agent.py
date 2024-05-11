"""
Module: agent.py
Author: akaranam
Description: This module defines the base class for agents in the system.
"""

from utils.llm_wrapper import LLMWrapper
import json

class Agent:
    def __init__(self, system_prompt, model_config, load_from=None):
        if load_from is not None:
            self.load_agent(load_from)
        else: 
            self.system_prompt = system_prompt
            self.model_config = model_config
    
    def respond(self, user_message="", use_history=True, add_to_history=True) -> str:
        """
        Generate a response to the user message
        :param user_message: The message from the user
        :return: The response from the agent
        """
        if add_to_history and user_message != "":
            self.history.append(user_message)

        if use_history and len(self.history) > 0:
            user_message = "This is the history of the conversation so far: ".join(self.history) + "------------------\n New message: " + user_message
        
        response = LLMWrapper(self.model_config).generate_text(system_prompt=self.system_prompt, user_message=user_message)

        if add_to_history:
            self.history.append(response)
        
        return response
    
    def reset_history(self) -> None:
        """
        Reset the conversation history
        """
        self.history = []
    
    def save_agent(self, path):
        """
        Save the agent to a file in JSON format.
        :param path: The path to save the agent
        """
        agent_data = {
            "system_prompt": self.system_prompt,
            "model_config": self.model_config.serialize,
            "history": self.history
        }
        with open(path, "w") as file:
            json.dump(agent_data, file, indent=4)
    
    def load_agent(self, path):
        """
        Load the agent from a file
        :param path: The path to load the agent
        """
        with open(path, "r") as f:
            lines = f.readlines()
            self.system_prompt = lines[0].strip()
            self.history = lines[1].strip().split("\n")
            self.model_config = eval(lines[2])

