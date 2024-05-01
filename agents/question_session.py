"""
Module: question_session.py
Author: akaranam
Description: This module contains the general purpose questioner class
"""
from utils.llm_wrapper import LLMWrapper
from agents.questioner import Questioner

class QuestionSession:
    def __init__(self, domain, instruction_model_config, questioner_model_config):
        self.domain = domain
        self.instruction_model_config = instruction_model_config
        self.questioner_model_config = questioner_model_config
        self.questioner_instructions = None
        self.questioner_agent = None

    def run_question_session(self, agent_list, num_rounds) -> None:
        """
        Run a question session with the provided agent
        :param agent: The agent to question
        :param num_rounds: The number of rounds to question the agent
        """

        self.create_instructions()
        self.create_questioner()
        for agent in agent_list:
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


    def question_agent(self, agent, num_rounds) -> str:
        """
        Question the agent and return the response
        :param agent: The agent to question
        :return: The response from the agent
        """

        response = ""
        
        for _ in range(num_rounds):
            question = self.questioner_agent.respond(response)
            response = agent.respond(question)
