"""
Module: policymaker.py
Author: mhelabd
Description: This is the general module for the policy axes agent, which generates policy axes for the given domain (+ ). 
"""

import sys
sys.path.append(".")
import re

from agents.agent import Agent
from utils.llm_wrapper import LLMWrapper
from config import Config



class PolicyAxesGenerator(Agent):
    def __init__(self, model_config, predefined_policy_axes=[]):
        """
        Initializes the Policymaker agent with the given model configuration.
        
        Args:
            model_config: The configuration for the model.
        """
        system_prompt = "You are a policymaker. Your job is to identify the set of axes by which a policy should be evaluated."
        super().__init__(model_config=model_config, system_prompt=system_prompt)
        if predefined_policy_axes:
            self.predefined_policy_axes = predefined_policy_axes
        else:
            self.predefined_policy_axes = [
                'budget',
                'safety',
                'freedom',
                'privacy',
                'inclusion',
                'equality',
                'transparency'
            ]

    def create_policy_axes(self, domain: str,  statement_limit:int=20) -> list: 
        """
        Given a domain, create as many unique policy statements as possible. 
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        axis_set = set(self.predefined_policy_axes)
        # Initial Prompt for the LLM
        assistant_system_prompt = f"You are an assistant helping come up with creative policy solutions to the domain of {domain}."
        user_message = f"""
            Come up axes by which we evaluate a policy in the domain {domain}. 
            Make sure each policy axis is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
            General axis include budget, safety, freedom, privacy, inclusion, equality, transparency.
            Please limit response to the axis name without including any description or explanation of what the axis means.
        """

        response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
        axis_list = re.findall('<statement>(.*)</statement>', response.lower())

        for axis_statement in axis_list:
            if self.is_unique(axis_statement, axis_set):
                axis_set.add(axis_statement)
            else: 
                print("Axis already exists: ", axis_statement)

        print("Axis List", axis_set)            
        
        # Chaining to get more responses 
        while len(axis_set) < statement_limit:
            user_message = f"""
                Your goal is to come up with policy evaluation criteria (or axes) that are creative and innovative.
                So far, you have come up with the following policy axes: {", ".join(axis_list)}
                Do not repeat any of these axes again.
                Please come up with additional policy evaluation criteria or axes.
                Make sure each policy axis is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
                Please limit response to the axis name without including any description or explanation of what the axis means.
        """
            
            response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
            axis_list = re.findall('<statement>(.*)</statement>', response.lower())
            for axis_statement in axis_list:
                if axis_statement not in axis_set or self.is_unique(axis_statement, axis_set):
                    axis_set.add(axis_statement)
                else: 
                    print("Axis already exists: ", axis_statement)
            print("Axis List", axis_set)            
        return list(axis_set)
        
    
    def is_unique(self, policy_statement, statement_list):
        """
        Given a set of policy statements, check if the new policy statement is unique
        :param: policy_statement: The new policy statement to check
        :param: statement_list: The set of policy statements
        :return: True if the policy statement is unique, False otherwise
        """
        
        uniqueness_system_prompt = "You are an assistant that helps decide if a new policy statement is different those already generated."
        user_message = f"""
        Give these current policy statements, {statement_list} and the new policy statement, {policy_statement}, output true if the new policy statement different than all of the current policies, or false if it is a duplicate. Also output false if the policy is not a valid policy. Output only one of two words: 'true' or 'false'.
        """
        response = LLMWrapper(self.model_config).generate_text(system_prompt=uniqueness_system_prompt, user_message=user_message)        
        if response.lower() == "true":
            return True
        else:
            return False

if __name__ == "__main__":
    # Module Testing
    model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    agent = PolicyAxesGenerator(model_config)
    agent.create_policy_axes("Social media and Children safety", statement_limit=20)