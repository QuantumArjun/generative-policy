from typing import List
import os
import sys
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from agents.persona_sampler import PersonaSampler
from config import Config
from utils.agent_helper import batch_create_agents, batch_save_agents, batch_load_agents, print_agents, batch_create_representatives
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from agents.policy_statements.policy_statement_generator import PolicyStatementGenerator, PolicyStatementMethod
from agents.policymaker import Policymaker, ScoringSystem
from agents.digital_representative import DigitalRepresentative
from utils.name_generator import NameGenerator
from environments.elicitation import ElicitationEnvironment

if __name__ == "__main__":
    # Load environment variables and create config
    load_dotenv(dotenv_path='/.env')

    model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    domain = "Gun Control in America"
    key_question = "What is your opinion on gun control in America?"

    # Step 1: Personas. 
    # Code to Create Personas, or Sample Personas from OpinionQA

    print("Creating personas...")
    # persona_list = PersonaGenerator(domain=domain, model_config=model_config, num_personas=5).generate_personas()
    persona_list = PersonaSampler(num_to_sample=5, dataset="oqa_guns").sample_personas()
    agent_list = batch_create_agents(agent_class=HumanSimulator, model_config=model_config, system_prompts=persona_list)
    print("Personas created!\n")
    
    # Step 2: Policy Statement Generation
    # Code to create initial set of policy statements
    
    policy_statement_agent = PolicyStatementGenerator(model_config)
    initial_statements = policy_statement_agent.create_policy_statements("Gun Legislation in the United States", statement_limit=75,
                                                generation_method=PolicyStatementMethod.PROBLEM)
    
    # Step 3: Elicitation of preferences
    # Use the initial set of policies to elicit preferences from the humans 

    print("Spinning up elicitation environment...")
    elicitation_environment = ElicitationEnvironment(domain=domain, initial_statements=initial_statements, instruction_model_config=model_config, questioner_model_config=model_config, agent_list=agent_list)
    elicitation_environment.run_elicitation()
    print("Elicitation complete!\n")

    # batch_save_agents(agent_list)

    # agent_list = batch_load_agents("saved_agents/batch_10")

    # print("Creating digital representatives...")
    # digital_representatives = batch_create_representatives(agent_list, model_config)



    







 

    #Put humans in Elicitation environment in order to create digital twins