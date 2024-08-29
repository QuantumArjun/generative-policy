"""
Module: policy_curation.py
Author: mhelabd
Description: This is the general module for the policy curation agent, which generates policy statements for the given domain.
"""
import sys
sys.path.append(".")

from enum import Enum
from config import Config
from utils.llm_wrapper import LLMWrapper
from agents.policy_statements.policy_statement_generator import PolicyStatementGenerator, PolicyStatementMethod
from agents.policy_curation.prompts import PromptsForPolicyCuration
from agents.human_simul import HumanSimulator
from agents.digital_representative import DigitalRepresentative
from agents.agent import Agent
import random
import logging
import csv
import numpy as np


class PolicyCurationtMethod(Enum):
		"""This enum is used to specify the policy curation method."""
		RANDOM = 1
		ALL_POLICIES = 2


class PolicyCuration(Agent):
		def __init__(self, model_config, digital_representatives: list = [], policy_goals: list = []):
				"""
				Initializes the Policy Curation agent with the given model configuration.

				Args:
					model_config: The configuration for the model.
				"""
				self.prompts = PromptsForPolicyCuration()
				system_prompt = self.prompts.get_system_prompt()
				super().__init__(model_config=model_config, system_prompt=system_prompt)
				self.logger = logging.getLogger(__name__)
				self.digital_representatives = digital_representatives
				self.policy_goals = policy_goals

		def choose_policy_goals(self, num_policy_goals: int, policy_curation_method=PolicyCurationtMethod.RANDOM) -> list:
				if policy_curation_method == PolicyCurationtMethod.RANDOM:
						return self.choose_policy_randomly(num_policy_goals)
				elif policy_curation_method == PolicyCurationtMethod.ALL_POLICIES:
						return self.policy_goals
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
				for digital_representative in self.digital_representatives:
						vote = digital_representative.rate_opinion(policy_goal)
						votes.append(vote)
				return votes

		def get_vote_matrix(self, policy_votes: dict) -> np.array:
				num_humans = len(list(policy_votes.values())[0])
				num_policies = len(policy_votes)

				vote_matrix = np.zeros((num_humans, num_policies), dtype=int)

				for i, votes in enumerate(policy_votes.values()):
						vote_matrix[:, i] = votes

				return vote_matrix

		def get_popular_policy_goals(self, policy_votes: dict, num_goals: int = 2) -> list:
				vote_matrix = self.get_vote_matrix(policy_votes)
				popular_indices = np.argsort(np.sum(vote_matrix, axis=0))[::-1][:num_goals]
				return [list(policy_votes.keys())[i] for i in popular_indices]

		def get_controversial_policy_goals(self, policy_votes: dict, num_goals: int = 2) -> list:
				vote_matrix = self.get_vote_matrix(policy_votes)
				variances = np.var(vote_matrix, axis=0)
				controversial_indices = np.argsort(variances)[::-1][:num_goals]
				return [list(policy_votes.keys())[i] for i in controversial_indices]

		def get_contentious_policy_goals(self, policy_votes: dict, min_corr: float = -0.5) -> list:
				vote_matrix = self.get_vote_matrix(policy_votes)
				corr_matrix = np.corrcoef(vote_matrix, rowvar=False)
				indices = np.where(corr_matrix < min_corr)
				policy_goals = list(policy_votes.keys())
				contentious_pairs = [(policy_goals[i], policy_goals[j]) for i, j in zip(*indices)]
				return contentious_pairs

		def get_policy_goals(
				self,
				num_goals_to_choose: int,
				policy_curation_method=PolicyCurationtMethod.ALL_POLICIES,
				num_popular_policy_goals: int = 5,
				num_controversial_policy_goals: int = 5,
				min_contentious_corr: float = -0.5
		) -> dict:
				policy_goals = self.choose_policy_goals(num_goals_to_choose, policy_curation_method)
				policy_votes = self.vote_on_policy(policy_goals)
				pop_policies = self.get_popular_policy_goals(policy_votes, num_popular_policy_goals)
				cont_policies = self.get_controversial_policy_goals(policy_votes, num_controversial_policy_goals)
				cont_pairs = self.get_contentious_policy_goals(policy_votes, min_corr=min_contentious_corr)
				policy_goals = {"popular": pop_policies, "controversial": cont_policies, "contentious": cont_pairs}
				return policy_votes, policy_goals


if __name__ == "__main__":
		# Module Testing
		# python3 ./agents/policy_curation/policy_curation.py
		logging.basicConfig(level=logging.WARNING)
		logger = logging.getLogger(PolicyStatementGenerator.__name__)
		logger.setLevel(level=logging.INFO)

		domain = "Social media and Children safety"
		searchable_policy_goals = 20
		chosen_policy_goals = 20
		model_config = Config(model_type="OpenAI", model_name="gpt-4o-mini")

		human_sims = {
				"Democratic Archtype 1": HumanSimulator(system_prompt="Are you a member of the American Democratic Party? Yes", model_config=model_config),
				"Democratic Archtype 2": HumanSimulator(system_prompt="Are you a member of the American Democratic Party? Yes", model_config=model_config),
				"Democratic Archtype 3": HumanSimulator(system_prompt="Are you a member of the American Democratic Party? Yes", model_config=model_config),
				"Republican Archtype 1": HumanSimulator(system_prompt="Are you a member of the American Republican Party? Yes", model_config=model_config),
				"Republican Archtype 2": HumanSimulator(system_prompt="Are you a member of the American Republican Party? Yes", model_config=model_config),
				"Republican Archtype 3": HumanSimulator(system_prompt="Are you a member of the American Republican Party? Yes", model_config=model_config),
				"Liberal Archtype 1": HumanSimulator(system_prompt="Do you care to promote individual rights, civil liberties, democracy, and free enterprise over anything else? Yes", model_config=model_config),
				"Liberal Archtype 2": HumanSimulator(system_prompt="Do you care to promote individual rights, civil liberties, democracy, and free enterprise over anything else? Yes", model_config=model_config),
				"Liberal Archtype 3": HumanSimulator(system_prompt="Do you care to promote individual rights, civil liberties, democracy, and free enterprise over anything else? Yes", model_config=model_config),
				"Government Hater Archtype 1": HumanSimulator(system_prompt="Should the government be involved in anything? No", model_config=model_config),
				"Government Hater Archtype 2": HumanSimulator(system_prompt="Should the government be involved in anything? No", model_config=model_config),
				"Government Hater Archtype 3": HumanSimulator(system_prompt="Should the government be involved in anything? No", model_config=model_config),
		}

		policy_goals_gen = PolicyStatementGenerator(model_config)
		logger.info(f"Generating policies for domain: {domain} with limit: {searchable_policy_goals}")
		policy_goals = policy_goals_gen.create_policy_statements(
				domain, statement_limit=searchable_policy_goals, generation_method=PolicyStatementMethod.CHAINING)

		policy_curator = PolicyCuration(model_config, list(human_sims.values()), policy_goals)
		policy_votes, policy_goals = policy_curator.get_policy_goals(chosen_policy_goals)

		with open('./agents/policy_curation/data/policy_voting.csv', 'w+', newline='', encoding='utf-8') as csvfile:
			csv_writer = csv.writer(csvfile)
			csv_writer.writerow(["Policy Goal Type", "Policy", ", ".join(list(human_sims.keys())), "Vote %"])
			for policy_goal_type, policies in policy_goals.items():
					for policy in policies:
						if policy_goal_type == "contentious":
							votes = policy_votes.get(policy[0]) + policy_votes.get(policy[1])
						else:
							votes = policy_votes.get(policy, [])
						popularity = sum(votes) / len(votes)
						csv_writer.writerow([policy_goal_type, policy, votes, popularity])
