"""
Module: policy_curation.py
Author: mhelabd
Description: This is the general module for the policy curation agent, which generates policy statements for the given domain.
"""
import sys
sys.path.append(".")

import numpy as np
import csv
import logging
import re
import random
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from agents.policy_curation.prompts import PromptsForPolicyRefinment
from agents.policy_statements.policy_statement_generator import PolicyStatementGenerator, PolicyStatementMethod
from utils.llm_wrapper import LLMWrapper
from config import Config
from enum import Enum


class PolicyRefinement(Agent):
		def __init__(self, model_config, domain, agents: list[HumanSimulator]):
				"""
				Initializes the Policy Curation agent with the given model configuration.

				Args:
					model_config: The configuration for the model.
				"""
				self.prompts = PromptsForPolicyRefinment()
				system_prompt = self.prompts.get_system_prompt(domain)
				super().__init__(model_config=model_config, system_prompt=system_prompt)
				self.logger = logging.getLogger(__name__)
				self.domain = domain
				self.agents = agents

		def update_policy_goals(self, agent_voting, curr_policy_goals):
			new_policy_goals = []
			new_policy_goals.extend(curr_policy_goals['popular'])
			controversial_policies = self.update_controversial_policy_goals(agent_voting, curr_policy_goals['controversial'])
			if controversial_policies != []:
				new_policy_goals.extend(controversial_policies)
			contentious_policies = self.update_contentious_policy_goals(curr_policy_goals['contentious'])
			if contentious_policies != []:
				new_policy_goals.extend(contentious_policies)
			return new_policy_goals

		def update_controversial_policy_goals(self, agent_voting, policy_goals) -> list:
			"""
			This function refines controversial policy goals based on agent feedback.

			Args:
					agent_voting: A dictionary mapping policies to lists of votes from agents.
					policy_goals: A list of controversial policy goals.

			Returns:
					A list of refined policy goals.
			"""
			new_policy_goals = []
			for policy in policy_goals:
				dissenting_voters = self.get_dissenting_voters(agent_voting, policy)

				feedback_prompt = self.prompts.get_feedback_prompt(self.domain, policy)
				feedback_responses = [agent.ask_about_policy(feedback_prompt) for agent in dissenting_voters]

				feedback = ', '.join(feedback_responses)
				refined_prompt = self.prompts.get_refinement_prompt(self.domain, policy, feedback)

				refined_policy = LLMWrapper(self.model_config).generate_text(
					system_prompt=self.prompts.get_system_prompt(domain),
					user_message=refined_prompt
				)

				new_policy_goal = re.findall('<statement>(.*)</statement>', refined_policy.lower())
				new_policy_goals.extend(new_policy_goal)
			return new_policy_goals

		def get_dissenting_voters(self, agent_voting, policy, max_num_voters=3):
			"""
			Gets a random sample of agents who voted against the policy.

			Args:
					agent_voting: A dictionary mapping policies to lists of votes from agents.
					policy: The policy to get dissenting voters for.

			Returns:
					A list of agents who voted against the policy.
			"""
			votes = agent_voting.get(policy, [])
			dissenting_voters = [voter for voter, vote in zip(agent_voting.keys(), votes) if vote == -1]
			return random.sample(dissenting_voters, min(len(dissenting_voters), max_num_voters))  # Sample at most 3 dissenting voters

		def update_contentious_policy_goals(self, policy_goals) -> list:
			new_policy_goals = []
			for p1, p2 in policy_goals:
				response = LLMWrapper(self.model_config).generate_text(
					system_prompt=self.prompts.get_system_prompt(domain),
					user_message=self.prompts.get_contentious_policy_prompt(self.domain, p1 ,p2))
				print(response)
				new_policy_goal = re.findall('<statement>(.*)</statement>', response.lower())
				print(new_policy_goal)
				new_policy_goals.extend(new_policy_goal)
			return new_policy_goals


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
		# Imported in main to prevent circular dependencies
		from agents.policy_curation.policy_curation import PolicyCuration
		policy_curator = PolicyCuration(model_config, domain, list(human_sims.values()), policy_goals)
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
		policy_refinement = PolicyRefinement(model_config, domain, list(human_sims.values()))
		new_policy_goals = policy_refinement.update_policy_goals(policy_votes, policy_goals)
		policy_curator = PolicyCuration(model_config, domain, list(human_sims.values()), new_policy_goals)
		policy_votes, policy_goals = policy_curator.get_policy_goals(chosen_policy_goals)
		with open('./agents/policy_curation/data/policy_voting_after_iteration.csv', 'w+', newline='', encoding='utf-8') as csvfile:
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
