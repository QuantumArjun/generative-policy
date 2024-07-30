"""
Module: policy_problem_generator.py
Author: mhelabd
Description: This is the general module for the policy problem agent, which generates policy problems for the given domain. 
"""
import sys
sys.path.append(".")

from config import Config
from utils.llm_wrapper import LLMWrapper
from agents.agent import Agent
import logging
import re


class PolicyProblemGenerator(Agent):
    def __init__(self, model_config):
        """
        Initializes the Policymaker agent with the given model configuration.

        Args:
            model_config: The configuration for the model.
        """
        system_prompt = "You are a policymaker. Your job is to identify the set of policy problems by which a policy should be evaluated."
        super().__init__(model_config=model_config, system_prompt=system_prompt)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        self.predefined_policy_problem = []

    def create_policy_problems(self, domain: str,  statement_limit: int = 20) -> list:
        """
        Given a domain, create as many unique policy statements as possible. 
        :param domain: The domain to create policy statements for
        return: List of policy statements
        """
        problem_set = set(self.predefined_policy_problem)
        # Initial Prompt for the LLM
        assistant_system_prompt = f"You are an assistant helping come up with policy problems to the domain of {domain}."
        user_message = f"""
            Come up with policy problems that would be affected by a policy in the domain {domain}. 
            Make sure each problem is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
            Please limit response to the problems name without including any description or explanation of why you chose that problem.
        """

        response = LLMWrapper(self.model_config).generate_text(
            system_prompt=assistant_system_prompt, user_message=user_message)
        problem_list = re.findall('<statement>(.*)</statement>', response.lower())

        for problem_statement in problem_list:
            problem_statement = problem_statement.strip()
            if self.is_unique(problem_statement, problem_set):
                problem_set.add(problem_statement)
        self.logger.info(f"\t\t Set of Problems: \n \t\t\t{problem_set}")

        # Chaining to get more responses
        while len(problem_set) < statement_limit:
            user_message = f"""
                Your goal is to come up with policy problems that are creative and innovative.
                So far, you have come up with the following policy problems: {", ".join(problem_list)}
                Do not repeat any of these problems again.
                Please come up with additional policy problems.
                Make sure each policy problem is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end.
                Please limit response to the problem name without including any description or explanation of what the problem means.
        """

            response = LLMWrapper(self.model_config).generate_text(
                system_prompt=assistant_system_prompt, user_message=user_message)
            problem_list = re.findall('<statement>(.*)</statement>', response.lower())
            for problem_statement in problem_list:
                problem_statement = problem_statement.strip()
                if self.is_unique(problem_statement, problem_set):
                    problem_set.add(problem_statement)
            self.logger.info(f"\t\t Set of Problems: \n \t\t\t{problem_set}")
        return list(problem_set)

    def is_unique(self, policy_statement, statement_list):
        """
        Given a set of policy statements, check if the new policy statement is unique
        :param: policy_statement: The new policy statement to check
        :param: statement_list: The set of policy statements
        :return: True if the policy statement is unique, False otherwise
        """
        if policy_statement in statement_list:
            return False
        uniqueness_system_prompt = "You are an assistant that helps decide if a new policy problem is different those already generated."
        user_message = f"""
        Give these current policy problems, {statement_list} and the new policy problem, {policy_statement},
        output true if the new policy statement different than all of the current policies, or false if it is a duplicate.
        Also output false if the policy is not a valid policy. Output only one of two words: 'true' or 'false'.
        """
        response = LLMWrapper(self.model_config).generate_text(
            system_prompt=uniqueness_system_prompt, user_message=user_message)
        if response.lower() == "true":
            return True
        else:
            return False


if __name__ == "__main__":
    # Module Testing
    model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    agent = PolicyProblemGenerator(model_config)
    problems = agent.create_policy_problems("Social media and Children safety", statement_limit=20)
    print(problems)

