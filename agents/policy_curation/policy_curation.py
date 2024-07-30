"""
Module: policy_curation.py
Author: mhelabd
Description: This is the general module for the policy curation agent, which generates policy statements for the given domain.
"""
import sys
sys.path.append(".")

import csv
import logging
import random
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from agents.policy_curation.prompts import PromptsForPolicyCuration
from agents.policy_statements.policy_statement_generator import PolicyStatementGenerator, PolicyStatementMethod
from utils.llm_wrapper import LLMWrapper
from config import Config
from enum import Enum



class PolicyCurationtMethod(Enum):
		"""This enum is used to specify the policy curation method."""
		RANDOM = 1


class PolicyCuration(Agent):
		def __init__(self, model_config, human_sims: list = [], policy_goals: list = []):
				"""
				Initializes the Policy Curation agent with the given model configuration.

				Args:
												model_config: The configuration for the model.
				"""
				self.prompts = PromptsForPolicyCuration()
				system_prompt = self.prompts.get_system_prompt()
				super().__init__(model_config=model_config, system_prompt=system_prompt)
				self.logger = logging.getLogger(__name__)
				self.human_sims = human_sims
				self.policy_goals = policy_goals

		def choose_policy_goals(self, num_policy_goals: int, policy_curation_method = PolicyCurationtMethod.RANDOM) -> list:
			if policy_curation_method == PolicyCurationtMethod.RANDOM:
				return self.policy_goals[:num_policy_goals]
			else:
				raise ValueError(f"Invalid policy curation method: {policy_curation_method}")

		def choose_policy_randomly(self, num_policy_goals: int) -> list:
				return random.shuffle(self.policy_goals)[:num_policy_goals]

		def vote_on_policy(self, policy: list) -> dict:
				policy_votes = {}
				for policy_goal in policy:
						votes = self.vote_on_policy_goal(policy_goal)
						policy_votes[policy_goal] = votes
				return policy_votes

		def vote_on_policy_goal(self, policy_goal: str) -> list:
				votes = []
				for human_sim in self.human_sims:
						vote = human_sim.rate_opinion(policy_goal)
						votes.append(vote)
				return votes


if __name__ == "__main__":
		# Module Testing
		logging.basicConfig(level=logging.WARNING)
		logger = logging.getLogger(PolicyStatementGenerator.__name__)
		logger.setLevel(level=logging.INFO)

		domain = "Social media and Children safety"
		searchable_policy_goals = 10
		chosen_policy_goals = 3
		model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")

		human_sims = {
				"Democratic Archtype": HumanSimulator(system_prompt="Are you Democratic? Yes", model_config=model_config),
				"Republican Archtype": HumanSimulator(system_prompt="Are you Republican? Yes", model_config=model_config),
				"Liberal Archtype": HumanSimulator(system_prompt="Are you Liberal? Yes", model_config=model_config),
				"Conservative Archtype": HumanSimulator(system_prompt="Are you Conservative? Yes", model_config=model_config)
		}

		policy_goals_gen = PolicyStatementGenerator(model_config)
		logger.info(f"Generating policies for domain: {domain} with limit: {searchable_policy_goals}")
		policy_goals = policy_goals_gen.create_policy_statements(
				domain, statement_limit=searchable_policy_goals, generation_method=PolicyStatementMethod.CHAINING)

		agent = PolicyCuration(model_config, list(human_sims.values()), policy_goals)

		# RANDOM SELECTION
		logger.info(f"Selecting policy for domain: {domain}")
		chosen_policy_goals = agent.choose_policy_goals(chosen_policy_goals, policy_curation_method=PolicyCurationtMethod.RANDOM)
		votes = agent.vote_on_policy(chosen_policy_goals)
		print(votes)
		logger.info(f"Voting on policy for domain: {domain}")


		with open('./agents/policy_curation/data/policy_voting.csv', 'w+', newline='', encoding='utf-8') as csvfile:
			csv_writer = csv.writer(csvfile)
			csv_writer.writerow(["Human Sim", "Policy Goal", "Votes"])
			for policy_goal, vote in votes.items():
				for human_sim, vote in zip(human_sims.keys(), vote):
					csv_writer.writerow([human_sim, policy_goal, vote])