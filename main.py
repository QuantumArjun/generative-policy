import os
from dotenv import load_dotenv
from agents.persona_generator import PersonaGenerator
from config import Config

load_dotenv()

print(os.environ.get("OPENAI_API_KEY"))
print(os.environ.get("CLAUDE_API_KEY"))

persona = PersonaGenerator(domain="Technology", model_config=Config(model_type="OpenAI", model_name="gpt-3.5-turbo"), num_personas=5)
personas = persona.generate_personas()