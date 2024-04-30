"""
Module: config.py
Author: akaranam
Description: This module contains the configuration for the models used in the project.
"""

import os 

class Config:
    def __init__(self, model_type, model_name):
        self.model_type = model_type
        self.model_name = model_name

    @property
    def model_config(self):
        if self.model_type == "OpenAI":
            return {
                "api_key": os.environ.get("OPENAI_API_KEY"),
                "model": self.model_name
            }
        elif self.model_type == "Claude":
            return {
                "api_key": os.environ.get("CLAUDE_API_KEY"),
                "model": self.model_name
            }
        else:
            raise ValueError("Invalid model type specified.")