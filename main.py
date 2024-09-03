from typing import List
import os
import sys
import csv
import json 
import numpy as np
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from agents.persona_sampler import PersonaSampler
from config import Config
from utils.agent_helper import batch_create_agents, batch_save_agents, batch_save_humans, batch_load_agents, batch_load_humans, print_agents, batch_create_representatives
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from agents.policy_statements.policy_statement_generator import PolicyStatementGenerator, PolicyStatementMethod
from agents.policy_curation.policy_curation import PolicyCuration
from agents.policy_curation.policy_refinement import PolicyRefinement
from agents.policymaker import Policymaker, ScoringSystem
from agents.digital_representative import DigitalRepresentative
from evals.representative_comparison import RepresentativeComparison
from utils.name_generator import NameGenerator
from environments.elicitation import ElicitationEnvironment

if __name__ == "__main__":
    # Load environment variables and create config
    load_dotenv(dotenv_path='/.env')

    model_config = Config(model_type="OpenAI", model_name="gpt-4o")
    domain = "How Might We Make Gun Laws More Effective in the United States?"
    key_question = "What is your opinion on gun control in America?"
    num_to_choose = 20

    #------------------------------------------------------------------------------
    # Step 1: Personas. 
    # Code to Create Personas, or Sample Personas from OpinionQA

    print("Creating personas...")
    # persona_list = PersonaGenerator(domain=domain, model_config=model_config, num_personas=5).generate_personas()
    persona_list = PersonaSampler(num_to_sample=5, dataset="oqa_guns").sample_personas()
    base_humans = batch_create_agents(agent_class=HumanSimulator, model_config=model_config, system_prompts=persona_list)
    print("Personas created!\n")
    
    # Save Resulting Agents
    save_path = batch_save_humans(base_humans)
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 2: Policy Statement Generation
    # Code to create initial set of policy statements
    
    # Load Resulting Agents
    persona_list = batch_load_humans(save_path)
    print("Recreating base humans...")
    base_humans = batch_create_agents(agent_class=HumanSimulator, model_config=model_config, system_prompts=persona_list)
    
    print("Creating Policy Statements...")
    policy_statement_agent = PolicyStatementGenerator(model_config)
    initial_statements = policy_statement_agent.create_policy_statements(domain, statement_limit=30,
                                                generation_method=PolicyStatementMethod.PROBLEM)
    print("Policy Statements created!\n")
    
    
    # Save initial statements to file
    with open("initial_statements.txt", "w") as f:
        for statement in initial_statements:
            f.write(statement + "\n")
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 3: Elicitation of preferences
    # Use the initial set of policies to elicit preferences from the humans 
    
    # Load initial statements
    with open("initial_statements.txt", "r") as f:
        initial_statements = f.read().split("\n")
    initial_statements = [x.strip() for x in initial_statements if x.strip() != ""]
    
    
    # Create and run elicitation environment
    # print("Spinning up elicitation environment...")
    # elicitation_environment = ElicitationEnvironment(domain=domain, initial_statements=initial_statements, instruction_model_config=model_config, questioner_model_config=model_config, agent_list=base_humans)
    # raw_representatives = elicitation_environment.run_elicitation()
    # print("Elicitation complete!\n")
    
    # Save Resulting Agents
    # batch_save_agents(raw_representatives, save_path)
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 4: Creating Digital Representatives
    
    # Load agents
    raw_representatives = batch_load_agents("saved_agents/batch_13")
    
    print("Creating digital representatives...")
    digital_representatives = batch_create_representatives(raw_representatives, model_config)
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 5: Creating Initial Vote Matrix
    
    print("Running Initial Round of Votes...")
    policy_curator = PolicyCuration(model_config, domain, list(digital_representatives.values()), initial_statements)
    policy_votes, policy_goals = policy_curator.get_policy_goals(num_to_choose)
    print("Initial round of votes complete!\n")
    
    
    #save policy goals and policy votes to file
    with open('./agents/policy_curation/data/policy_goals.json', 'w+') as f:
        json.dump(policy_goals, f, indent=4)
    
    # Save vote matrix to file
    with open('./agents/policy_curation/data/policy_voting.csv', 'w+', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Policy Goal Type", "Policy", ", ".join(list(digital_representatives.keys())), "Vote %"])
        for policy_goal_type, policies in policy_goals.items():
                for policy in policies:
                    if policy_goal_type == "contentious":
                        votes = policy_votes.get(policy[0]) + policy_votes.get(policy[1])
                    else:
                        votes = policy_votes.get(policy, [])
                    popularity = sum(votes) / len(votes)
                    csv_writer.writerow([policy_goal_type, policy, votes, popularity])
    print("We have written to the file")
    exit() 
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    #Eval: Comparing the base human to the human representative on a set of policy statements
    
    comparisonEvaluator = RepresentativeComparison()
    comparisonEvaluator.evaluate(base_humans, digital_representatives, policy_goals)
    exit()
    
    
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 6: Policy Refinement
    
    #Read in policy goals from file
    policy_goals = None
    with open('./agents/policy_curation/data/policy_goals.json', 'r') as f:
        policy_goals = json.load(f)
    
    policy_votes = None
    #Read policy votes from file 
    with open('./agents/policy_curation/data/policy_voting.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        policy_votes = {row[1]: [float(x) for x in row[3].split(",")] for row in reader}
        
    print("Running Policy Refinement...")
    policy_refinement = PolicyRefinement(model_config, domain, list(digital_representatives.values()))
    new_policy_goals = policy_refinement.update_policy_goals(policy_votes, policy_goals)
    
    #save new policy goals to file
    with open('./agents/policy_curation/data/policy_goals_after_refinement.json', 'w+') as f:
        json.dump(new_policy_goals, f, indent=4)
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # (Optional) Step 7: Evolutionary Algorithm
    
    #TODO
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Step 8: Iterate (Goal -> Strategy -> Implementation)
    
    #Read in policy goals from file
    new_policy_goals = None
    with open('./agents/policy_curation/data/policy_goals_after_refinement.json', 'r') as f:
        new_policy_goals = json.load(f)
    
    print("Running Policy Iteration...")
    policy_curator = PolicyCuration(model_config, domain, list(digital_representatives.values()), new_policy_goals)
    policy_votes, policy_goals = policy_curator.get_policy_goals(num_to_choose)
    
    with open('./agents/policy_curation/data/policy_voting_after_iteration.csv', 'w+', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Policy Goal Type", "Policy", ", ".join(list(digital_representatives.keys())), "Vote %"])
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
    # Step 9: Write Policy Memo 
    
    #TODO
    #------------------------------------------------------------------------------
    
    



    







 

    #Put humans in Elicitation environment in order to create digital twins