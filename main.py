import os
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from config import Config
from agents.create_agents import batch_create_agents
from agents.agent import Agent
from agents.human_simul import HumanSimulator
from agents.question_session import QuestionSession

def print_agents(agent_list):
    for agent in agent_list:
        print(f"Agent Arcehtype: {agent.system_prompt}")
        print(f"Agent Conversation History:")
        for message in agent.history:
            print(message)

if __name__ == "__main__":
    # Load environment variables and create config
    load_dotenv()
    model_config=Config(model_type="OpenAI", model_name="gpt-3.5-turbo")
    domain = "Gun Control in America"

    #Create model personas to simuulate humans in the elicitation process
    persona_list = PersonaGenerator(domain=domain, model_config=model_config, num_personas=5).generate_personas()
    agent_list = batch_create_agents(agent_class=HumanSimulator, model_config=model_config, system_prompts=persona_list)

    #Create a question session with the agents
    QuestionSession(domain=domain, instruction_model_config=model_config, questioner_model_config=model_config).run_question_session(agent_list=agent_list, num_rounds=5)

    print("Question session complete")

    print_agents(agent_list)
 

    #Put humans in Elicitation environment in order to create digital twins