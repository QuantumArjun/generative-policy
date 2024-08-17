"""
Module: policy_stakeholder_generator.py
Author: mhelabd
Description: This is the general module for the policy stakeholder agent, which generates policy stakeholders for the given domain. 
"""

import sys
sys.path.append(".")

from config import Config
from utils.llm_wrapper import LLMWrapper
from agents.agent import Agent
import logging
import re


class PolicyStakeholderGenerator(Agent):
    def __init__(self, model_config, predefined_policy_stakeholder=[]):
        """
        Initializes the Policymaker agent with the given model configuration.

        Args:
            model_config: The configuration for the model.
        """
        system_prompt = "You are a policymaker. Your job is to identify the set of stakeholders by which a policy should be evaluated."
        super().__init__(model_config=model_config, system_prompt=system_prompt)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        if predefined_policy_stakeholder:
            self.predefined_policy_stakeholder = predefined_policy_stakeholder
        else:
            self.predefined_policy_stakeholder = [
                'Government',
                'Citizens',
                'Tax Payers',
            ]

    def create_policy_stakeholders(self, domain: str,  statement_limit: int = 20) -> list:
        """
        Given a domain, create as many unique policy statements as possible. 
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        stakeholder_set = set(self.predefined_policy_stakeholder)
        # Initial Prompt for the LLM
        assistant_system_prompt = f"You are an assistant helping come up with creative policy solutions to the domain of {domain}."
        user_message = f"""
            Come up with stakeholders that would be affected by a policy in the domain {domain}. 
            Make sure each stakeholder is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
            Please limit response to the stakeholder name without including any description or explanation of why you chose that stakeholder.
        """

        response = LLMWrapper(self.model_config).generate_text(
            system_prompt=assistant_system_prompt, user_message=user_message)
        stakeholder_list = re.findall('<statement>(.*)</statement>', response.lower())

        for stakeholder_statement in stakeholder_list:
            stakeholder_statement = stakeholder_statement.strip()
            if self.is_unique(stakeholder_statement, stakeholder_set):
                stakeholder_set.add(stakeholder_statement)
        self.logger.info(f"\t\t Set of Stakeholders: \n \t\t\t{stakeholder_set}")

        # Chaining to get more responses
        while len(stakeholder_set) < statement_limit:
            user_message = f"""
                Your goal is to come up with policy stakeholders that are creative and innovative.
                So far, you have come up with the following policy stakeholders: {", ".join(stakeholder_list)}
                Do not repeat any of these stakeholders again.
                Please come up with additional policy stakeholders.
                Make sure each policy stakeholder is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
                Please limit response to the stakeholder name without including any description or explanation of what the stakeholder means.
        """

            response = LLMWrapper(self.model_config).generate_text(
                system_prompt=assistant_system_prompt, user_message=user_message)
            stakeholder_list = re.findall('<statement>(.*)</statement>', response.lower())
            for stakeholder_statement in stakeholder_list:
                stakeholder_statement = stakeholder_statement.strip()
                if self.is_unique(stakeholder_statement, stakeholder_set):
                    stakeholder_set.add(stakeholder_statement)
            self.logger.info(f"\t\t Set of Stakeholders: \n \t\t\t{stakeholder_set}")
        return list(stakeholder_set)

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
        Give these current policy stakeholders, {statement_list} and the new policy stakeholder, {policy_statement}, 
        output true if the new policy stakeholders are different than all of the current stakeholders, 
        or false if it is a duplicate. Also output false if the stakeholder is not a valid one. 
        Output only one of two words: 'true' or 'false'.
        """
        response = LLMWrapper(self.model_config).generate_text(
            system_prompt=uniqueness_system_prompt, user_message=user_message)
        if response.lower() == "true":
            return True
        else:
            return False


if __name__ == "__main__":
    # Module Testing
    model_config = Config(model_type="OpenAI", model_name="gpt-4o-mini")
    agent = PolicyStakeholderGenerator(model_config)
    agent.create_policy_stakeholders("Social media and Children safety", statement_limit=20)
