from typing import List
import os
import sys
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from config import Config
from utils.agent_helper import batch_create_agents, batch_save_agents, batch_load_agents, print_agents, batch_create_representatives
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from agents.policymaker import Policymaker, ScoringSystem
from agents.digital_representative import DigitalRepresentative
from utils.name_generator import NameGenerator
from environments.elicitation import ElicitationEnvironment

if __name__ == "__main__":
    # Load environment variables and create config
    load_dotenv()

    model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    domain = "Gun Control in America"
    key_question = "What is your opinion on gun control in America?"

    #Code to Create Personas, currently commented out

    # print("Creating personas...")
    # persona_list = PersonaGenerator(domain=domain, model_config=model_config, num_personas=5).generate_personas()
    # agent_list = batch_create_agents(agent_class=HumanSimulator, model_config=model_config, system_prompts=persona_list)
    # print("Personas created!\n")

    # print("Spinning up elicitation environment...")
    # elicitation_environment = ElicitationEnvironment(domain=domain, key_question=key_question, instruction_model_config=model_config, questioner_model_config=model_config, agent_list=agent_list)
    # elicitation_environment.run_elicitation()
    # print("Elicitation complete!\n")

    # batch_save_agents(agent_list)

    agent_list = batch_load_agents("saved_agents/batch_10")

    print("Creating digital representatives...")
    digital_representatives = batch_create_representatives(agent_list, model_config)

    for rep in digital_representatives:
        print(rep.name)
        print(rep.system_prompt)

    policymaker = Policymaker(model_config=model_config, system_prompt="You are a policymaker. You will be interacting with digital representatives to create optimal policies.")
    results_dict, result = policymaker.evaluate_policy(digital_representatives, "We should ban all guns in America and confiscate every gun", ScoringSystem.APPROVAL)

    print(results_dict)

    #TODO - Elicitaiton Part:
    #Minor 
    # Fix rating so that you can pass an arg to rate the max 
    # Pretty print the history for each agent 

    #Major
    #Tone down the archetypes, none of them change their opinion 
    #Think of how and if I should demarcate the agents 

    # Fix rating so that you can pass an arg to rate the max 
    # Pretty print the history for each agent 



    







 

    #Put humans in Elicitation environment in order to create digital twins