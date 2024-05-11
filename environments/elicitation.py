import logging
import numpy as np
"""
Module: elicitation.py
Author: akaranam
Description: This module contains the classes for the overall elicitation environment.
"""

from agents.questioner import Questioner
from utils.llm_wrapper import LLMWrapper
import random

class ElicitationEnvironment:
    def __init__(self, domain, key_question, instruction_model_config, questioner_model_config, agent_list, num_rounds = 5, num_polis_rounds=3):
        self.domain = domain
        self.key_question = key_question
        self.instruction_model_config = instruction_model_config
        self.questioner_model_config = questioner_model_config
        self.agent_list = agent_list
        self.num_rounds = num_rounds
        self.num_polis_rounds = num_polis_rounds

        self.questioner_instructions = None
        self.questioner_agent = None
 
        self.ratings_matrix = None
    
    def run_elicitation(self) -> None:
        """
        Run the overall elicitation process
        """
        print("Running Question Session")
        self.run_question_session(self.num_rounds)

        print("Eliciting Opinions")
        self.elicit_initial_opinions()

        print("Gathering neighbor opinions")
        self.ratings_matrix = self.run_neighbor_opinions()

        print("Eliciting Final Opinions")
        self.elicit_final_opinions()


    def elicit_initial_opinions(self) -> None:
        """
        Elicit initial opinions from the agents
        """
        ask_key_question = f"Please provide your opinion on the following question: {self.key_question}"
        for agent in self.agent_list:
            agent.initial_opinion = agent.respond(ask_key_question, q_tag = "<Initial Opinion Question>", a_tag = "<Initial Opinion>") 

    def elicit_final_opinions(self) -> None:
        """
        Elicit final opinions from the agents
        """
        ask_key_question = f"After seeing those other opinions, please reflect on your original opinion, and provide your final opinion on the following question: {self.key_question}. Feel free to explain your thoughts."
        for agent in self.agent_list:
            agent.final_opinion = agent.respond(ask_key_question, q_tag = "<Final Opinion Question>", a_tag = "<Final Opinion>") 

    
    def run_neighbor_opinions(self) -> np.ndarray:
        """
        Run the neighbor opinion elicitation process (Similar to Pol.is)
        :return: A matrix of ratings between agents
        """
        n_agents = len(self.agent_list)

        # Initialize the matrix with None, indicating no rating
        ratings = np.full((n_agents, n_agents), None)

        for round_index in range(self.num_polis_rounds):
            # Create a random shuffle of agents to determine who rates whom in this round
            indices = np.arange(n_agents)
            np.random.shuffle(indices)

            # Assign each agent to rate the next in the shuffled list
            for i in range(n_agents):
                rater_index = indices[i]
                ratee_index = indices[(i + 1) % n_agents]  # Wrap around to the start
                if rater_index != ratee_index:
                    rater_agent = self.agent_list[rater_index]
                    ratee_agent = self.agent_list[ratee_index]
                    rating = rater_agent.rate_opinion(ratee_agent.initial_opinion)

                    ratings[rater_index, ratee_index] = rating

        return ratings

    def run_question_session(self, num_rounds: int) -> None:
        """
        Run a question session with the provided agent
        :param agent: The agent to question
        :param num_rounds: The number of rounds to question the agent
        """

        self.create_instructions()
        self.create_questioner()
        for agent in self.agent_list:
            self.question_agent(agent, num_rounds)
            self.questioner_agent.reset_history()
    
    def create_instructions(self) -> None:
        """
        Create instructions for the LLM-based questioner
        """
        llm = LLMWrapper(self.instruction_model_config)
        
        system_prompt = f"""You are creating the instructions for an LLM-based questioner for the domain: {self.domain}. Your task is to provide clear and concise instructions for the questioner to follow. You should ensure that the questioner concise questions that elicit useful information from the user. The questions should require minimal effort to answer (e.g., yes/no questions, multiple-choice questions, etc.). Additionally, the questions should not repeat information already provided by the user."""
        user_message = f""" Create the instructions for the LLM-based questioner for the domain: {self.domain}."""

        response = llm.generate_text(system_prompt=system_prompt, user_message=user_message)

        self.questioner_instructions = response

    def create_questioner(self) -> None:
        """
        Create the LLM-based questioner
        """
        questioner = Questioner(self.questioner_instructions, self.questioner_model_config)
        self.questioner_agent = questioner


    def question_agent(self, agent, num_rounds):
        """
        Question the agent and return the response
        :param agent: The agent to question
        """

        response = ""
        
        for _ in range(num_rounds):
            question = self.questioner_agent.respond(response)
            response = agent.respond(question,  q_tag = "<Question>", a_tag = "<Your Answer>")
    



