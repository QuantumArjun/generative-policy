"""
Module: persona_sampler.py
Author: akaranam
Description: This module contains the classes for the persona sampler agent.
"""

import sys
import os
import ast

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persona_research.create_participant import sample_participant_external
from persona_research.data.data_processor import (
    anes_key_question, w26_key_question, w27_key_question, w29_key_question, w32_key_question,
    w34_key_question, w36_key_question, w41_key_question, w42_key_question, w43_key_question,
    w45_key_question, w49_key_question, w50_key_question, w54_key_question, w82_key_question,
    w92_key_question, anes_key_fields, w26_key_fields, w27_key_fields, w29_key_fields,
    w32_key_fields, w34_key_fields, w36_key_fields, w41_key_fields, w42_key_fields,
    w43_key_fields, w45_key_fields, w49_key_fields, w50_key_fields, w54_key_fields,
    w82_key_fields, w92_key_fields
)

class PersonaSampler:
    def __init__(self, num_to_sample, dataset, **kwargs):
        self.num_to_sample = num_to_sample
        self.dataset = dataset
        self.raw_personas = []
        self.processed_personas = []
        self.final_personas = []

    def sample_personas(self):
        self.raw_personas = sample_participant_external(self.num_to_sample, self.dataset)
        print("Sampled")
        self.process_personas()
        self.format_personas()
        
        return self.final_personas

    def format_personas(self):
        for p in self.processed_personas:
            persona = "\n".join(p)
            self.final_personas.append(persona)
        

    def process_personas(self):
        processor = PersonaProcessor(self.raw_personas, self.dataset)
        self.processed_personas = processor.process_personas()
        for p in self.processed_personas:
            print(p)
            exit()

class PersonaProcessor:
    def __init__(self, personas, dataset):
        self.personas = personas
        self.dataset = dataset
        self.questions = self.get_key_questions()

    def get_key_questions(self):
        dataset_mapping = {
            "ANES": (anes_key_question, anes_key_fields),
            "oqa_guns": (w26_key_question, w26_key_fields),
            "oqa_work": (w27_key_question, w27_key_fields),
            "oqa_gender": (w29_key_question, w29_key_fields),
            "oqa_community": (w32_key_question, w32_key_fields),
            "oqa_science": (w34_key_question, w34_key_fields),
            "oqa_glass_ceiling": (w36_key_question, w36_key_fields),
            "oqa_gov_role": (w41_key_question, w41_key_fields),
            "oqa_expert_sources": (w42_key_question, w42_key_fields),
            "oqa_race": (w43_key_question, w43_key_fields),
            "oqa_online_sources": (w45_key_question, w45_key_fields),
            "oqa_social_media": (w49_key_question, w49_key_fields),
            "oqa_family": (w50_key_question, w50_key_fields),
            "oqa_econ_inequality": (w54_key_question, w54_key_fields),
            "oqa_international_affairs": (w82_key_question, w82_key_fields),
            "oqa_2020_general": (w92_key_question, w92_key_fields),
        }

        if self.dataset not in dataset_mapping:
            raise ValueError(f"Dataset {self.dataset} not supported")

        master_list, key_fields = dataset_mapping[self.dataset]
        return [master_list[field][0] for field in key_fields]

    def process_personas(self):
        processed_personas = []
        for persona in self.personas:
            qa_pairs = []
            for index, question in enumerate(self.questions):
                answer = persona.all_fields[index]
                print(question)
                print(answer)
                if answer is not None and answer != "" and answer != " ":
                    qa_pairs.append(f"Question: {question}\nMy Answer: {answer}")
                else:
                    qa_pairs.append(f"Question: {question}\nAnswer: No answer provided")
            qa_pairs.insert(0, "A bit about me: " + persona.identityParagraph())
            processed_personas.append(qa_pairs)
        return processed_personas

    def _extract_field_from_question(self, question):
        words = question.split()
        for word in words:
            if word.isupper():  # Assuming field names are in all caps
                return word
        return None  # If no field is found

# Usage example
if __name__ == "__main__":
    sampler = PersonaSampler(num_to_sample=2, dataset="w29")
    sampler.sample_personas()
    sampler.process_personas()

    for i, persona in enumerate(sampler.processed_personas):
        print(f"Persona {i+1}:")
        for qa in persona:
            print(qa)
        print()