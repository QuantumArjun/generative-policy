"""
Module: create_agents.py
Author: akaranam
Description: This module batch creates agents
"""

def batch_create_agents(agent_class, system_prompts, *args, **kwargs):
    """
    Batch create agents based on the system prompts provided
    :param agent_class: Class of the agent to create
    :param system_prompts: List of system prompts for each agent
    :return: List of agents
    """
    agents = []
    for prompt in system_prompts:
        agent = agent_class(prompt, *args, **kwargs)
        agents.append(agent)
    return agents