from typing import List
import os
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from config import Config
from utils.agent_helper import batch_create_agents, batch_save_agents
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from agents.digital_representative import DigitalRepresentative
from environments.elicitation import ElicitationEnvironment

if __name__ == "__main__":
    # Load environment variables and create config
    load_dotenv()

    model_config = Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    domain = "Gun Control in America"
    key_question = "What is your opinion on gun control in America?"

    print("Creating personas...")
    persona_list = PersonaGenerator(domain=domain, model_config=model_config, num_personas=5).generate_personas()
    agent_list = batch_create_agents(agent_class=HumanSimulator, model_config=model_config, system_prompts=persona_list)
    print("Personas created!\n")

    print("Spinning up elicitation environment...")
    elicitation_environment = ElicitationEnvironment(domain=domain, key_question=key_question, instruction_model_config=model_config, questioner_model_config=model_config, agent_list=agent_list)
    elicitation_environment.run_elicitation()
    print("Elicitation complete!\n")

    batch_save_agents(agent_list)

    exit()

    print("Creating digital representatives...")
    digital_representatives = []
    for agent in agent_list:
        digital_rep = DigitalRepresentative(system_prompt=agent.system_prompt, model_config=model_config, human_agent=agent)
        digital_rep.initialize_representative(agent)
        digital_representatives.append(digital_rep)

    print_agents(agent_list)

    print(elicitation_environment.ratings_matrix)

    #TODO - Elicitaiton Part:
    #Tone down the archetypes, none of them change their opinion 
    #Think of how and if I should demarcate the agents 

    # Implement loading of agents 
    # Wrap questions being asked in question tags, and answers in answer tags 
    # Convert elicitiation to the history (add a new variable for history, and update the save component to add this)
    #Fix rating so that you can pass an arg to rate the max 

    #TODO - Creating Digital Representatives:
    #Create a digital twin for each agent


    







 

    #Put humans in Elicitation environment in order to create digital twins