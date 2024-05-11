"""
Module: policymaker.py
Author: akaranam
Description: This is the general module for the policymaker agent, which will interact with other agents in order to create multiple optimal policies. 
"""

from agents.agent import Agent
from enum import Enum


class Policymaker(Agent):
    def __init__(self, model_config, system_prompt):
        super().__init__(model_config, system_prompt)

    def propose_policy(self):
        """
        Propose a policy based on the input from the human agent
        """
        pass

    def evaluate_policy(self, agent_list, policy, prompt_type):
        """
        Evaluate the proposed policy based on various criteria.
        :param agent_list: List of agents to interact with for evaluation.
        :param policy: The proposed policy to evaluate.
        :param prompt_type: The type of prompt to use for evaluation, from PromptType enum.
        """

        if prompt_type == PromptType.APPROVAL:
            return self.approval_scoring(agent_list, policy)
        elif prompt_type == PromptType.RANKING:
            return self.ranked_scored(agent_list, policy)
        else:
            raise ValueError("Invalid prompt type provided")

    def approval_scoring(self, agent_list, policy): 
        """
        Score the policy based on approval from other agents
        :param agent_list: List of agents to interact with for approval
        :param policy: The proposed policy to evaluate
        """
        prompt = "Please provide your opinion on the policy: use one of two words: 'Approve' or 'Disapprove'"

        response_dict = {}

        for agent in agent_list:
            response = agent.respond(prompt, q_tag="Proposed Policy", a_tag="Your Response")
            while response not in ["Approve", "Disapprove"]:
                response = agent.respond(prompt + "\n Invalid response, you must choose either 'Approve' or 'Disapprove'", q_tag="Proposed Policy", a_tag="Your Response")
            response_dict[agent.name] = response
        
        approval_percentage = sum(value.lower().count('approve') for value in response_dict.values())

        return response_dict, approval_percentage
        


            # Process response and assign scores

    def ranked_scoring():
        pass

    def scale_scoring():
        pass

    def refine_policy(self):
        """
        Refine the policy based on feedback and evaluation
        """
        pass

    def finalize_policy(self):
        """
        Finalize the policy and prepare for implementation
        """
        pass

class PromptType(Enum):
    APPROVAL = 1
    RANKING = 2