from typing import List
import os
import sys
import csv
import numpy as np
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from agents.persona_sampler import PersonaSampler
from config import Config
from utils.agent_helper import batch_create_agents, batch_save_agents, batch_load_agents, print_agents, batch_create_representatives
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from agents.policy_statements.policy_statement_generator import PolicyStatementGenerator, PolicyStatementMethod
from agents.policy_curation.policy_curation import PolicyCuration
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

    #------------------------------------------------------------------------------
    # Step 1: Personas. 
    # Code to Create Personas, or Sample Personas from OpinionQA

    print("Creating personas...")
    # persona_list = PersonaGenerator(domain=domain, model_config=model_config, num_personas=5).generate_personas()
    
    persona_list = PersonaSampler(num_to_sample=5, dataset="oqa_guns").sample_personas()
    agent_list = batch_create_agents(agent_class=HumanSimulator, model_config=model_config, system_prompts=persona_list)
    
    print("Personas created!\n")
    
    # batch_save_agents(agent_list)
    # agent_list = batch_load_agents("saved_agents/batch_10")
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 2: Policy Statement Generation
    # Code to create initial set of policy statements
    
    # policy_statement_agent = PolicyStatementGenerator(model_config)
    # initial_statements = policy_statement_agent.create_policy_statements("Gun Legislation in the United States", statement_limit=75,
    #                                             generation_method=PolicyStatementMethod.PROBLEM)
    
    
    # Save initial statements to file
    # with open("initial_statements.txt", "w") as f:
    #     for statement in initial_statements:
    #         f.write(statement + "\n")
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 3: Elicitation of preferences
    # Use the initial set of policies to elicit preferences from the humans 
    
    # Load initial statements
    with open("initial_statements.txt", "r") as f:
        initial_statements = f.read().split("\n")
    initial_statements = [x.strip() for x in initial_statements if x.strip() != ""]
    
    
    # Create and run elicitation environment
    print("Spinning up elicitation environment...")
    
    elicitation_environment = ElicitationEnvironment(domain=domain, initial_statements=initial_statements, instruction_model_config=model_config, questioner_model_config=model_config, agent_list=agent_list)
    updated_agent_list = elicitation_environment.run_elicitation()
    
    print("Elicitation complete!\n")
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 4: Creating Digital Representatives
    
    print("Creating digital representatives...")
    digital_representatives = batch_create_representatives(updated_agent_list, model_config)
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 5: Creating Initial Vote Matrix
    
    num_to_choose = 20
    
    print("Running Initial Round of Votes...")
    
    policy_curator = PolicyCuration(model_config, list(digital_representatives), initial_statements)
    policy_votes, policy_goals = policy_curator.get_policy_goals(num_to_choose)
    
    print("Initial round of votes complete!\n")
    
    # Save vote matrix to file
    with open('./agents/policy_curation/data/policy_voting.csv', 'w+', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Policy Goal Type", "Policy", ", ".join([rep.name for rep in digital_representatives]), "Vote %"])
        for policy_goal_type, policies in policy_goals.items():
                for policy in policies:
                    if policy_goal_type == "contentious":
                        votes = policy_votes.get(policy[0]) + policy_votes.get(policy[1])
                    else:
                        votes = policy_votes.get(policy, [])
                    popularity = sum(votes) / len(votes)
                    csv_writer.writerow([policy_goal_type, policy, votes, popularity])
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 6: Policy Refinement
    
    #TODO 
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # (Optional) Step 7: Evolutionary Algorithm
    
    #TODO
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 8: Iterate (Goal -> Strategy -> Implementation)
    
    #TODO
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 9: Write Policy Memo 
    
    #TODO
    #------------------------------------------------------------------------------
    
    



    







 

    #Put humans in Elicitation environment in order to create digital twins