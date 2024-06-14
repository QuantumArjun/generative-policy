"""
Module: policymaker.py
Author: mhelabd
Description: This is the general module for the policymaker agent, which will interact with other agents in order to create multiple optimal policies. 
"""

import sys
sys.path.append(".")
import re

from agents.agent import Agent
from agents.policy_axes_generator import PolicyAxesGenerator
from enum import Enum
from utils.llm_wrapper import LLMWrapper
from config import Config


class PolicymakerWithAxes(Agent):
    def __init__(self, model_config):
        """
        Initializes the Policymaker agent with the given model configuration.
        
        Args:
            model_config: The configuration for the model.
        """
        system_prompt = "You are a policymaker. Your job is to identify the set of policy statements to help craft a creative policy."
        super().__init__(model_config=model_config, system_prompt=system_prompt)

    def create_policy_statements(self, domain, statement_limit=50) -> list: 
        """
        Given a domain, create as many unique policy statements as possible. 
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        
        policy_set = set()
        
        assistant_system_prompt = f"You are an assistant helping come up with creative policy solutions to the domain of {domain}."
        user_message = f"""
            Come up axes by which we evaluate a policy in the domain {domain}. 
            Make sure each policy statement is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
            Policy statements should be sentence long description of the policy for the domain.
        """       
        response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
        policy_list = re.findall('<statement>(.*)</statement>', response.lower())

        for policy_statement in policy_list:
            if self.is_unique(policy_statement, policy_set):
                policy_set.add(policy_statement)
            else: 
                print("Policy statement already exists: ", policy_statement)

        print("Policy Statements", policy_set)

        # Policy Axes
        policy_axes_gen = PolicyAxesGenerator(self.model_config)
        policy_axes = policy_axes_gen.create_policy_axes(domain)
        while len(policy_axes) < statement_limit:
            for axis in policy_axes:
                user_message = f"""
                    Your goal is to come up with policy statements that are creative and innovative.
                    Each policy statement has to fit under this axis: {axis}
                    So far, you have come up with the following policy statements: {", ".join(policy_list)}
                    Do not repeat any of these policy statements again.
                    Please come up with additional policy statements.
                    Make sure each policy axis is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
                """
                response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
                policy_list = re.findall('<statement>(.*)</statement>', response.lower())
                for policy_statement in policy_list:
                    if self.is_unique(policy_statement, policy_set):
                        policy_set.add(policy_statement)
                    else: 
                        print("Policy statement already exists: ", policy_statement)
                print("Policy Statements", policy_set)
        print(list(policy_set))
        return list(policy_set)
        
    
    def is_unique(self, policy_statement, statement_list):
        """
        Given a set of policy statements, check if the new policy statement is unique
        :param: policy_statement: The new policy statement to check
        :param: statement_list: The set of policy statements
        :return: True if the policy statement is unique, False otherwise
        """
        if policy_statement in statement_list:
            return False
        uniqueness_system_prompt = "You are an assistant that helps decide if a new policy statement is different those already generated."
        user_message = f"""
        Give these current policy statements: {'\n'.join(statement_list)}
        and the new policy statement: {policy_statement}
        output true if the new policy statement different than all of the current policies, or false if it is a duplicate. Also output false if the policy is not a valid policy. Output only one of two words: 'true' or 'false'.
        """
        response = LLMWrapper(self.model_config).generate_text(system_prompt=uniqueness_system_prompt, user_message=user_message)        
        if response.lower() == "true":
            return True
        else:
            return False

if __name__ == "__main__":
    # Module Testing
    model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    agent = PolicymakerWithAxes(model_config)
    agent.create_policy_statements("Social media and Children safety", statement_limit=50)