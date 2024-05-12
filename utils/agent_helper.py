
"""
Module: create_agents.py
Author: akaranam
Description: This module batch creates agents
"""

import os
import json
from typing import List
from agents.agent import Agent
from agents.digital_representative import DigitalRepresentative
from utils.name_generator import NameGenerator
from config import Config

def batch_create_agents(agent_class, system_prompts, model_config, *args, **kwargs):
    """
    Batch create agents based on the system prompts provided
    :param agent_class: Class of the agent to create
    :param system_prompts: List of system prompts for each agent
    :return: List of agents
    """
    agents = []
    for prompt in system_prompts:
        agent = agent_class(prompt, model_config, *args, **kwargs)
        agents.append(agent)
    return agents

def batch_save_agents(agents: List[Agent]):
    """
    Batch save agents to files in a new folder for each batch.
    Folder naming follows 'saved_agents_batch_X' where X is an incrementing integer.
    :param agents: List of agents to save
    """
    base_folder = os.path.join(os.getcwd(), "saved_agents")
    if not os.path.exists(base_folder):
        os.makedirs(base_folder, exist_ok=True)

    # Find the highest existing batch number
    max_batch_number = -1
    for folder_name in os.listdir(base_folder):
        if folder_name.startswith("batch_"):
            try:
                batch_number = int(folder_name.split('_')[-1])
                if batch_number > max_batch_number:
                    max_batch_number = batch_number
            except ValueError:
                continue  # Skip folders with non-integer suffixes

    # Create a new folder for the current batch
    new_batch_number = max_batch_number + 1
    folder_path = os.path.join(base_folder, f"batch_{new_batch_number}")
    os.makedirs(folder_path, exist_ok=True)

    # Save each agent in the new folder
    for i, agent in enumerate(agents):
        agent_path = os.path.join(folder_path, f"agent_{i}.json")
        agent.save_agent(agent_path)

def batch_load_agents(batch_folder: str):
    """
    Batch load agents from a folder
    :param batch_folder: The folder containing the agents
    :return: List of agents
    """
    agents = []
    for file_name in os.listdir(batch_folder):
        file_path = os.path.join(batch_folder, file_name)
        agent = Agent(load_from=file_path)
        agents.append(agent)
    return agents

def batch_create_representatives(agent_list: List[Agent], model_config: Config) -> List[DigitalRepresentative]:
    """
    Batch create digital representatives based on the given list of agents.
    :param agent_list: List of agents to create digital representatives for.
    :param model_config: The model configuration to use for the digital representatives.
    :return: List of digital representatives.
    """
    rep_list = []
    name_gen = NameGenerator()
    for agent in agent_list:
        digital_rep = DigitalRepresentative(model_config = model_config, human_agent=agent, name=name_gen.generate_random_first_name())
        rep_list.append(digital_rep)
    
    return rep_list

def print_agents(agent_list: List[Agent]) -> None:
    """
    Prints information about each agent in a given list of agents.

    Args:
        agent_list (List[Agent]): A list of agent objects.

    Returns:
        None. The function only prints the information about each agent.
    """
    if agent_list is not None and len(agent_list) > 0:
        for agent in agent_list:
            print("Agent Archetype: {}\n".format(agent.system_prompt))
            if hasattr(agent, 'initial_opinion'):
                print("Agent Initial Opinion: {}".format(agent.initial_opinion))
            if hasattr(agent, 'final_opinion'):
                print("Agent Final Opinion: {}\n".format(agent.final_opinion))
            if hasattr(agent, 'history'):
                print("Agent History: {}\n".format(agent.history))
