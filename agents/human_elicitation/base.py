"""
Module: human_elicitation.py
Author: mhelabd
Description: This module contains the classes for the human elicitation environment.
"""

from agents.questioner import Questioner
from utils.llm_wrapper import LLMWrapper


class BaseHumanElicitation:
  def __init__(self, model_config, domain):
    self.model_config = model_config
    self.domain = domain
    self.initial_statements = ""
    self.create_instructions()
    self.create_questioner()

  def create_instructions(self) -> None:
    """
    Create instructions for the LLM-based questioner
    """
    llm = LLMWrapper(self.model_config)

    system_prompt = f"""You are creating the instructions for an LLM-based questioner that is going to question people about their stance on a political issue. The transcript of this conversation will be used to make "digital representatives" on people's behalf. Here is the list of policies that those "digital representatives" will be asked about: {self.initial_statements}.

    Your goal is to write a set of instructions for the questioner to follow.

    Here is the list of policies that the questioner. Keep in mind, the questioner WILL NOT have access to the list of policies. It is your responsibility to ensure that your instructions contain the broad themes of this set of policies, as well as capture the main disagreements that the people may have, such that the questioner can find areas of disagreement.

    Your task is to provide clear and concise instructions for the questioner to follow. You should ensure that the questioner concise questions that elicit useful information from the user. The questions should require minimal effort to answer (e.g., yes/no questions, multiple-choice questions, etc.). Additionally, the questions should not repeat information already provided by the user."""
    user_message = f""" Create the instructions for the LLM-based questioner for the domain: {
      self.domain}."""

    response = llm.generate_text(
      system_prompt=system_prompt, user_message=user_message)

    print(f"Instructions: {response}")

    self.questioner_instructions = response

  def create_questioner(self) -> None:
    """
    Create the LLM-based questioner
    """
    questioner = Questioner(self.questioner_instructions, self.model_config)
    self.questioner_agent = questioner

  def question_human(self):
    """
    Question the human and return the response
    """
    question = self.questioner_agent.respond("")
    return question

  def update_human_response(self, human_response):
    response = human_response
    return response
