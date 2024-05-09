from typing import List
import os
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from config import Config
from agents.create_agents import batch_create_agents
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from environments.elicitation import ElicitationEnvironment

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
            print("Agent Initial Opinion: {}".format(agent.initial_opinion))
            print("Agent Final Opinion: {}\n".format(agent.final_opinion))

if __name__ == "__main__":
    # Load environment variables and create config
    load_dotenv()
    model_config=Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    domain = "Gun Control in America"
    key_question = "What is your opinion on gun control in America?"

    #Create model personas to simuulate humans in the elicitation process
    print("Creating personas...")
    persona_list = PersonaGenerator(domain=domain, model_config=model_config, num_personas=5).generate_personas()
    agent_list = batch_create_agents(agent_class=HumanSimulator, model_config=model_config, system_prompts=persona_list)

    #Create a question session with the agents
    print("Spinning up elicitation environment...")
    elicitation_environment = ElicitationEnvironment(domain=domain, key_question=key_question, instruction_model_config=model_config, questioner_model_config=model_config, agent_list=agent_list)
    elicitation_environment.run_elicitation()

    print_agents(agent_list)

    print(elicitation_environment.ratings_matrix)

    #TODO - Elicitaiton Part:
    #Implement Logging 
    #Implement saving along different parts of the process
    #Fix rating so that you can pass an arg to rate the max 
    #Log all agent interactions, and see where we can fix 
    #Tone down the archetypes, none of them change their opinion 

    #TODO - Creating Digital Representatives:
    #Create a digital twin for each agent


    







 

    #Put humans in Elicitation environment in order to create digital twins