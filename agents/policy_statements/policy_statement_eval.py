"""
Module: policy_statement_generator.py
Author: mhelabd and akaranam
Description: This module contains the classes for the policy statement generator agent.
"""

import sys
sys.path.append(".")
import re

from agents.agent import Agent
from agents.policy_statements.policy_statement_generator import PolicyStatementGenerator, PolicyStatementMethod
from enum import Enum
from utils.llm_wrapper import LLMWrapper
from config import Config
import re

class PolicyStatementEvalMethod(Enum):
    RAW_UNIQUENESS = 1

class PolicyStatementEvaluation(Agent):
    """
    Class: PolicyStatementEvaluator
    Author: mhelabd
    Description: This class is used to evaluate policy statements for a given domain.
    """

    def __init__(self, model_config):
        """
        Initializes the PolicyStatementEvaluation agent with the given model configuration.
        
        Args:
            model_config: The configuration for the model.
        """
        system_prompt = "You are a policymaker. Your job is to evaluate a list of policy statements for a given domain."
        super().__init__(model_config=model_config, system_prompt=system_prompt)
    
    def evaluate_policy_statements(self, domain, policy_statements_dict, evaluation_method=PolicyStatementEvalMethod.RAW_UNIQUENESS) -> list:
        """
        Generates policy statements for a given domain evaluate the number of unique policy statements generated.
        :param domain: The domain to generate policy statements for
        :param policy_statements_dict: The Dictionary of list of policy statements to evaluate 
          (where each key is an algorithm used to generate a policy statement)
        :param evaluation_method: The method to use for policy statement evaluation (default: RAW_UNIQUENESS)
        :type evaluation_method: PolicyStatementEvalMethod
        :return: Dictionary of Metrics of policy statement evaluation
        """
        if evaluation_method == PolicyStatementEvalMethod.RAW_UNIQUENESS:
            return self.evaluate_policy_statements_raw_uniqueness(domain, policy_statements_dict)
        else:
            raise ValueError(f"Invalid evaluation method: {evaluation_method}")
    
    def evaluate_policy_statements_raw_uniqueness(self, domain, policy_statements_dict) -> list: 
        """
        Given a domain, create as many unique policy statements as possible. 
        :param domain: The domain to create policy statements for
        :param policy_statements_dict: The Dictionary of list of policy statements to evaluate
        :return: Dictionary of Metrics of policy statement evaluation
        """
        return {k: len(v) for k, v in policy_statements_dict.items()}
 
if __name__ == "__main__":
    # Module Testing
    model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    agent = PolicyStatementGenerator(model_config)
    domain = "Social media and Children safety"
    statements_by_model_limit = {}
    for model_limit in [1, 5, 20]:
        policy_statements_base = agent.create_policy_statements(domain, model_call_limt=model_limit, generation_method=PolicyStatementMethod.BASE)
        policy_statements_chaining = agent.create_policy_statements(domain, model_call_limt=model_limit, generation_method=PolicyStatementMethod.CHAINING)
        policy_statements_axis = agent.create_policy_statements(domain, model_call_limt=model_limit, generation_method=PolicyStatementMethod.AXIS)
        policy_statements_stakeholder = agent.create_policy_statements(domain, model_call_limt=model_limit, generation_method=PolicyStatementMethod.STAKEHOLDER)
        statements_by_model_limit[model_limit] = {
            "base": policy_statements_base,
            "chaining": policy_statements_chaining,
            "axis": policy_statements_axis,
            "stakeholder": policy_statements_stakeholder
        }
    eval = PolicyStatementEvaluation(model_config)
    for model_limit, statement_dict in statements_by_model_limit.items():      
      results = eval.evaluate_policy_statements(domain, statement_dict, evaluation_method=PolicyStatementEvalMethod.RAW_UNIQUENESS)
      print(model_limit, results)