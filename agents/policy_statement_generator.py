"""
Module: policy_statement_generator.py
Author: akaranam and mhelabd
Description: This module contains the classes for the policy statement generator agent.
"""

import sys
sys.path.append(".")
import re

from agents.agent import Agent
from agents.policy_axes_generator import PolicyAxesGenerator
from enum import Enum
from utils.llm_wrapper import LLMWrapper
from config import Config
import re

class PolicyStatementMethod(Enum):
    BASE = 1
    CHAINING = 2
    AXIS = 3

class PolicyStatementGenerator(Agent):
    """
    Class: PolicyStatementGenerator
    Author: akaranam
    Description: This class is used to generate policy statements for a given domain.
    """

    def __init__(self, model_config):
        """
        Initializes the PolicyStatementGenerator agent with the given model configuration.
        
        Args:
            model_config: The configuration for the model.
        """
        system_prompt = "You are a policymaker. Your job is to create a list of policy statements for a given domain."
        super().__init__(model_config=model_config, system_prompt=system_prompt)
    
    def create_policy_statements(self, domain, statement_limit=20, generation_method=PolicyStatementMethod.BASE) -> list:
        """
        Call the policy statement generator agent to generate policy statements
        :param domain: The domain to generate policy statements for
        :param statement_limit: The maximum number of policy statements to generate
        return: List of policy statements
        """
        if generation_method == PolicyStatementMethod.BASE:
            return self.create_policy_statements_base(domain, statement_limit)
        elif generation_method == PolicyStatementMethod.CHAINING:
            return self.create_policy_statements_chaining(domain, statement_limit)
        elif generation_method == PolicyStatementMethod.AXIS:
            return self.create_policy_statements_axes(domain, statement_limit)
        else:
            raise ValueError(f"Invalid generation method: {generation_method}")
    
    def create_policy_statements_base(self, domain, statement_limit=20) -> list: 
        """
        Given a domain, create as many unique policy statements as possible. 
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        
        policy_set = set("Do Nothing")
        
        assistant_system_prompt = "You are an assistant helping come up with creative policy solutions to the domain of {}.".format(domain)
        
        # Initial Prompt for the LLM
        user_message = "Come up with policy statements. Make sure to begin each policy statement with <Statement>" 
        
        response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
        policy_list = [statement.strip() for statement in response.split("<Statement>") if statement.strip()]
        
        for policy_statement in policy_list:
            if self.is_unique(policy_statement, policy_set):
                policy_set.add(policy_statement)
            else: 
                print("Policy statement already exists: ", policy_statement)
        
        print(list(policy_set))
        return list(policy_set)
    
    def create_policy_statements_chaining(self, domain, statement_limit=20) -> list: 
        """
        Given a domain, create as many unique policy statements as possible. 
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        
        policy_set = set("Do Nothing")
        
        assistant_system_prompt = "You are an assistant helping come up with creative policy solutions to the domain of {}.".format(domain)
        
        # Initial Prompt for the LLM
        user_message = "Come up with policy statements. Make sure to begin each policy statement with <Statement>" 
        
        response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
        policy_list = [statement.strip() for statement in response.split("<Statement>") if statement.strip()]
        
        for policy_statement in policy_list:
            if self.is_unique(policy_statement, policy_set):
                policy_set.add(policy_statement)
            else: 
                print("Policy statement already exists: ", policy_statement)
        
        # Chaining to get more responses 
        while len(policy_set) < statement_limit:
            user_message = "Your goal is to come up with policy statements that are creative and innovative.  \
                So far, you have come up with the following policy statements: " + ", ".join(policy_list) + ". \
                Please come up with additional policy statements. \
                Make sure to begin each policy statement with <Statement>"
            
            response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
            policy_list = [statement.strip() for statement in response.split("<Statement>") if statement.strip()]
            
            for policy_statement in policy_list:
                if self.is_unique(policy_statement, policy_set):
                    policy_set.add(policy_statement)
                else: 
                    print("Policy statement already exists: ", policy_statement)
        
        print(list(policy_set))
        return list(policy_set)
    
    def create_policy_statements_along_axis(self, domain, statement_limit=50) -> list: 
        """
        Given a domain, create as many unique policy statements as possible, exploring along pre-defined axes.
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
    agent = PolicyStatementGenerator(model_config)
    agent.create_policy_statements("Social media and Children safety", statement_limit=50)