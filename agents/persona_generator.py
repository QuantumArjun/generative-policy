"""
Module: persona_generator.py
Author: akaranam
Description: This module takes in a domain, and creates plausible archetypes for the domain.
"""

from llm_wrapper import LLMWrapper
import os
import pickle

class PersonaGenerator:
    def __init__(self, domain, model_config, num_personas=5, should_save_personas=False):
        self.domain = domain
        self.model_config = model_config
        self.num_personas = num_personas
        self.archetype_strings = []
        self.should_save_personas = should_save_personas

    def generate_personas(self) -> list:
        """
        Generate personas for the domain
        :return: List of personas
        """

        archetype_system_prompt = f"""You are an expert in generating personas and archetypes for various domains. Your task is to create a diverse set of archetypes for the domain provided."""

        archetype_message_prompt = f"""
        Given Domain: {self.domain}

        Please generate {self.num_personas} distinct archetypes for the provided domain. Each archetype should include the following information:

        1. Archetype Name/Title: A descriptive and concise name for the archetype.
        2. Description: A brief paragraph describing the key characteristics, motivations, and behaviors of the archetype within the given domain.
        3. Goals/Needs: A bullet list of 3-5 primary goals, needs, or desires that drive this archetype's actions and decisions in the domain.
        4. Demographics (optional): Any relevant demographic information (age, gender, location, etc.) that helps define the archetype.
        5. Quotes/Sayings (optional): 1-2 sample quotes or sayings that capture the essence of the archetype's mindset or values.

        Begin each archetype with <archetype>, and end each archetype with </archetype> Please format the archetypes clearly, with each section labeled appropriately. Ensure that the archetypes are distinct, well-developed, and capture a diverse range of perspectives and behaviors within the given domain.
        """

        llm = LLMWrapper(self.model_config)

        response = llm.generate_text(system_prompt=archetype_system_prompt, user_message=archetype_message_prompt)
        cleaned_responses = llm.clean_response(response, open="<archetype>", close="</archetype>")

        self.archetype_strings = cleaned_responses

        if self.should_save_personas:
            self.save_personas()
    
        return self.archetype_strings
    
    def save_personas(self) -> str:
        """
        Save the generated archetypes to a file
        :param domain: The domain for which the archetypes are generated
        """

        index = 2
        filename = f"personas/{self.domain}_archetypes.pkl"
        while os.path.exists(filename):
            filename = f"personas/{self.domain}_archetypes_{index}.pkl"
            index += 1
        
        with open(filename, 'wb') as f:
            pickle.dump(self.archetype_strings, f)

        return filename
    
    def load_personas(self, filename) -> list:
        """
        Load the archetypes from a list
        :param filename: file to load from
        """
        with open(filename, 'rb') as f:
            loaded_list = pickle.load(f)
        
        self.archetype_strings = loaded_list

        return loaded_list

