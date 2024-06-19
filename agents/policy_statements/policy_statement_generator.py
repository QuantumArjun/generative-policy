"""
Module: policy_statement_generator.py
Author: akaranam and mhelabd
Description: This module contains the classes for the policy statement generator agent.
"""

import sys
sys.path.append(".")
import re

from agents.agent import Agent
from agents.policy_statements.policy_axes_generator import PolicyAxesGenerator
from agents.policy_statements.policy_stakeholder_generator import PolicyStakeholderGenerator
from enum import Enum
from utils.llm_wrapper import LLMWrapper
from config import Config
import re

AXIS_LIMIT = 5
STAKEHOLDER_LIMIT = 5

class PolicyStatementMethod(Enum):
    BASE = 1
    CHAINING = 2
    AXIS = 3
    STAKEHOLDER = 4

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
    
    def create_policy_statements(self, domain, statement_limit=-1, model_call_limt=20, generation_method=PolicyStatementMethod.BASE) -> list:
        """
        Call the policy statement generator agent to generate policy statements
        :param domain: The domain to generate policy statements for
        :param statement_limit: The maximum number of policy statements to generate (-1 for unlimited)
        :param model_call_limt: The maximum number of model calls to make (-1 for unlimited)
        return: List of policy statements
        """
        if generation_method == PolicyStatementMethod.BASE:
            return self.create_policy_statements_base(domain)
        elif generation_method == PolicyStatementMethod.CHAINING:
            return self.create_policy_statements_chaining(domain, statement_limit, model_call_limt)
        elif generation_method == PolicyStatementMethod.AXIS:
            return self.create_policy_statements_along_axis(domain, statement_limit, model_call_limt)
        elif generation_method == PolicyStatementMethod.STAKEHOLDER:
            return self.create_policy_statements_along_axis_and_stakeholder(domain, statement_limit, model_call_limt)
        else:
            raise ValueError(f"Invalid generation method: {generation_method}")
    
    def create_policy_statements_base(self, domain) -> list: 
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
    
    def create_policy_statements_chaining(self, domain, statement_limit=20, model_call_limt=20) -> list: 
        """
        Given a domain, create as many unique policy statements as possible. 
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        
        policy_set = set("Do Nothing")
        num_model_calls = 0
        
        assistant_system_prompt = "You are an assistant helping come up with creative policy solutions to the domain of {}.".format(domain)
        
        # Initial Prompt for the LLM
        user_message = "Come up with policy statements. Make sure to begin each policy statement with <Statement>" 
        
        response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
        policy_list = [statement.strip() for statement in response.split("<Statement>") if statement.strip()]
        num_model_calls += 1
        
        for policy_statement in policy_list:
            if self.is_unique(policy_statement, policy_set):
                policy_set.add(policy_statement)
            else: 
                print("Policy statement already exists: ", policy_statement)
        
        # Chaining to get more responses 
        while not self.is_limit_reached(len(policy_set), num_model_calls, statement_limit, model_call_limt):
            user_message = f"""Your goal is to come up with policy statements that are creative and innovative.
                So far, you have come up with the following policy statements: {", ".join(policy_list)}.
                Please come up with additional policy statements.
                Make sure to begin each policy statement with <Statement>
            """
            
            response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
            policy_list = [statement.strip() for statement in response.split("<Statement>") if statement.strip()]
            num_model_calls += 1
            
            for policy_statement in policy_list:
                if self.is_unique(policy_statement, policy_set):
                    policy_set.add(policy_statement)
                else: 
                    print("Policy statement already exists: ", policy_statement)
        
        print(list(policy_set))
        return list(policy_set)
    
    def create_policy_statements_along_axis(self, domain, statement_limit=20, model_call_limt=20) -> list: 
        """
        Given a domain, create as many unique policy statements as possible, exploring along pre-defined axes.
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        
        policy_set = set()
        num_model_calls = 0
        
        assistant_system_prompt = f"You are an assistant helping come up with creative policy solutions to the domain of {domain}."
        user_message = f"""
            Come up axes by which we evaluate a policy in the domain {domain}. 
            Make sure each policy statement is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
            Policy statements should be sentence long description of the policy for the domain.
        """       
        response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
        policy_list = re.findall('<statement>(.*)</statement>', response.lower())
        num_model_calls += 1

        for policy_statement in policy_list:
            if self.is_unique(policy_statement, policy_set):
                policy_set.add(policy_statement)
            else: 
                print("Policy statement already exists: ", policy_statement)
        
        # Policy Axes
        policy_axes_gen = PolicyAxesGenerator(self.model_config)
        policy_axes = policy_axes_gen.create_policy_axes(domain, statement_limit=AXIS_LIMIT)
        while not self.is_limit_reached(len(policy_axes), num_model_calls, statement_limit, model_call_limt):
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
                num_model_calls += 1
                for policy_statement in policy_list:
                    if self.is_unique(policy_statement, policy_set):
                        policy_set.add(policy_statement)
                    else: 
                        print("Policy statement already exists: ", policy_statement)
                # If limit is reached when not done with axis, we should still break.
                if self.is_limit_reached(len(policy_set), num_model_calls, statement_limit, model_call_limt):
                    return list(policy_set)
                print("Policy Statements", policy_set)
        
        print(list(policy_set))
        return list(policy_set)

    def create_policy_statements_along_axis_and_stakeholder(self, domain, statement_limit=20, model_call_limt=20) -> list: 
        """
        Given a domain, create as many unique policy statements as possible, exploring along pre-defined axes and stakeholders.
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        
        policy_set = set()
        num_model_calls = 0
        
        assistant_system_prompt = f"You are an assistant helping come up with creative policy solutions to the domain of {domain}."
        user_message = f"""
            Come up axes by which we evaluate a policy in the domain {domain}. 
            Make sure each policy statement is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
            Policy statements should be sentence long description of the policy for the domain.
        """       
        response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
        policy_list = re.findall('<statement>(.*)</statement>', response.lower())
        num_model_calls += 1

        for policy_statement in policy_list:
            if self.is_unique(policy_statement, policy_set):
                policy_set.add(policy_statement)
            else: 
                print("Policy statement already exists: ", policy_statement)
        
        # Policy Axes
        policy_axes_gen = PolicyAxesGenerator(self.model_config)
        policy_axes = policy_axes_gen.create_policy_axes(domain, statement_limit=AXIS_LIMIT)
        policy_stakeholders = PolicyStakeholderGenerator(self.model_config)
        policy_stakeholders = policy_stakeholders.create_policy_stakeholders(domain, statement_limit=STAKEHOLDER_LIMIT)
        while not self.is_limit_reached(len(policy_axes), num_model_calls, statement_limit, model_call_limt):
            for axis in policy_axes:
                for stakeholder in policy_stakeholders:
                    user_message = f"""
                        Your goal is to come up with policy statements that are creative and innovative.
                        Each policy statement has to fit under this axis: {axis}
                        Each policy statement has to be helping this stakeholder: {stakeholder}
                        So far, you have come up with the following policy statements: {", ".join(policy_list)}
                        Do not repeat any of these policy statements again.
                        Please come up with additional policy statements.
                        Make sure each policy axis is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
                    """
                    response = LLMWrapper(self.model_config).generate_text(system_prompt=assistant_system_prompt, user_message=user_message)
                    policy_list = re.findall('<statement>(.*)</statement>', response.lower())
                    num_model_calls += 1
                    for policy_statement in policy_list:
                        if self.is_unique(policy_statement, policy_set):
                            policy_set.add(policy_statement)
                        else: 
                            print("Policy statement already exists: ", policy_statement)
                    # If limit is reached when not done with axis, we should still break.
                    if self.is_limit_reached(len(policy_set), num_model_calls, statement_limit, model_call_limt):
                        return list(policy_set)
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
            Give these current policy statements: {', '.join(statement_list)}
            and the new policy statement: {policy_statement}
            output true if the new policy statement different than all of the current policies, or false if it is a duplicate. Also output false if the policy is not a valid policy. Output only one of two words: 'true' or 'false'.
            """
        response = LLMWrapper(self.model_config).generate_text(system_prompt=uniqueness_system_prompt, user_message=user_message)        
        if response.lower() == "true":
            return True
        else:
            return False

    def is_limit_reached(self, num_policies, num_model_calls, statement_limit, model_call_limit):
        """
        A function to check if the limit is reached based on the number of policies, model calls, statement limits, and model call limits.
        
        Args:
            num_policies: The number of policies.
            num_model_calls: The number of model calls.
            statement_limit: The limit for the number of statements.
            model_call_limit: The limit for the number of model calls.
        
        Returns:
            True if the limit is reached, False otherwise.
        """
        if statement_limit == -1 and model_call_limit == -1:
            raise ValueError("Only one of statement_limit or model_call_limit can be -1")
        if statement_limit == -1:
            # Number of model calls does not exceed the model call limit
            return num_model_calls >= model_call_limit
        elif model_call_limit == -1:
            # Number of policies does not exceed the policy statement limit
            return num_policies >= statement_limit
        else:
            # Both statement limit and model call limit are specified
            assert ValueError("Both statement_limit and model_call_limit are specified. Only one of them can be -1.")

if __name__ == "__main__":
    # Module Testing
    model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    agent = PolicyStatementGenerator(model_config)
    agent.create_policy_statements("Social media and Children safety", statement_limit=50, generation_method=PolicyStatementMethod.STAKEHOLDER)