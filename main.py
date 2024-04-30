import os
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from config import Config
from agents.create_agents import batch_create_agents
from agents.agent import Agent
from agents.human_simul import HumanSimulator

if __name__ == "__main__":
    # Load environment variables and create config
    load_dotenv()
    model_config=Config(model_type="OpenAI", model_name="gpt-3.5-turbo")

    #Create model personas to simuulate humans in the elicitation process
    persona_list = PersonaGenerator(domain="Technology", model_config=model_config, num_personas=5).generate_personas()
    agent_list = batch_create_agents(agent_class=HumanSimulator, system_prompts=persona_list)

    #Put humans in Elicitation environment in order to create digital twins