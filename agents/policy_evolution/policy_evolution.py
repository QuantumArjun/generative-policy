"""
Module: policy_evolution.py
Author: kanishk with modifications by akaranam
Description: This is the general module for the evolutionary algorithm for policy evolution.
"""

import os
import random
import tqdm
import requests
import concurrent.futures
from typing import List, Tuple, Optional

import numpy as np
import editdistance

from utils import llm_generate, parse_response

class Message:
    def __init__(self, content: str, selected: str, edited: str, reasons: str, thought: str,
                 score: float, parent1: Optional['Message'] = None, parent2: Optional['Message'] = None, operation: Optional[str] = None):
        self.content = content
        self.selected = selected
        self.edited = edited
        self.reasons = reasons
        self.thought = thought
        self.score = score
        self.parents = []
        self.children = []
        for parent in [parent1, parent2]:
            if parent:
                self.parents.append(parent)
                parent.children.append(self)
        self.operation = operation

    def get_history(self) -> List[Tuple[str, str, float]]:
        history = []
        current = self
        while current:
            history.append((current.content, current.operation or "Initial", current.score))
            if current.parent2:
                history.extend(current.parent2.get_history())
            current = current.parent1
        return history[::-1]  # Reverse to get

class Constraint:
    def __init__(self, description: str, predicate: callable):
        self.description = description
        self.predicate = predicate

class PredictiveModel:
    def __init__(self, model_name: str, model_id: str, baseten_api_key: str):
        self.baseten_api_key = baseten_api_key
        self.model_name = model_name
        self.model_id = model_id

    @staticmethod
    def parse_llama(x: str):
        return x.content.decode().split("<|end_header_id|>")[-1].split("<|eot_id|>")[0].strip()

    def run(self, prompt:str, max_tokens:int = 2000):
        messages = [{"role": "user", "content": prompt}]
        data = {
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": 1.0,
        }
        
        resp = requests.post(
            f"https://model-{model_id}.api.baseten.co/production/predict",
            headers={"Authorization": f"Api-Key {self.baseten_api_key}"},
            json=data
        )
        return self.parse_llama(resp)

    def predict(self, message: str, target_audience: str, target_attitude: str) -> float:
        """
        Predict the score for a given message, target audience, and target attitude.
        
        Example:
        message = "<message about a political campaign, like gun rights>"
        target_audience = "republicans in texas"
        target_attitude = "How likely are you to support gun regulations? 1(no)-5(yes) target 5."
        return score (float)
        """
        prompt_scale = [
            (f"""Imagine you're {target_audience}, reading the following message. To what extent do you think it would change your opinion on the topic, {target_attitude}?
            {message}
            Score the message on a scale of 0-{scale}, where 0 is not at all effective and {scale} is extremely effective. Return only the number. No talk, just the numberRemember: the target audience is {target_audience}.""",
            scale)
            for scale in [3, 5, 10, 20, 100]
        ]
        
        def parse_number(x):
            try:
                return float(x)
            except:
                return None
            
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures_scale = {executor.submit(self.run, prompt): scale for prompt, scale in prompt_scale}
            vals = [parse_number(future.result()) / scale for future, scale in futures_scale.items() if parse_number(future.result()) is not None]
        return np.mean(vals)

class SimpleGenerativeModel:
    def __init__(self, predictive_model: PredictiveModel, system_path: str = None, user_path: str = None, model_name: str = None, temperature: float = 0.7, max_tokens: int = 512, constraints: List[Constraint] = []):
        self.predictive_model = predictive_model

        with open(f"prompts/{system_path}.txt", "r") as f:
            self.system_template = f.read()
        with open(f"prompts/{user_path}.txt", "r") as f:
            self.user_template = f.read()

        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.constraints = constraints

    def generate(self, message: str, target_audience: str, target_attitude: str, verbose: bool = False) -> Tuple[str, str, float]:
        """
        Generate an improved message based on the input and target.
        """
        old_score = self.predictive_model.predict(message, target_audience, target_attitude)
        if verbose:
            print("Old Score:", old_score)
        
        system = self.system_template
        user = self.user_template.format(message=message, target_audience=target_audience, target_attitude=target_attitude)
        if verbose:
            print("System:", system)
            print("User:", user)
        
        llm_response = llm_generate(self.model_name, system, user, temperature=self.temperature, max_tokens=self.max_tokens)
        if verbose:
            print("LLM Response:", llm_response)
        parsed_response = parse_response(llm_response)
        if verbose:
            print(parsed_response)
        selected, edited = parsed_response["selected"], parsed_response["edited"]
        new_message = initial_message.replace(selected, edited)

        for constraint in self.constraints:
            if not constraint.predicate(new_message):
                return "Constraint not satisfied", None, None, None, None
            
        new_score = self.predictive_model.predict(new_message, target_audience, target_attitude)
        if verbose:
            print("New Score:", new_score)
        
        if new_score > old_score:
            return parsed_response["selected"], parsed_response["edited"], new_message, parsed_response["reasons"], new_score
        else:
            return "Score not improved", None, None, None, None

class BestOfNGenerativeModel:
    def __init__(
        self,
        predictive_model: PredictiveModel,
        system_path: str = None,
        user_path: str = None,
        model_name: str = None,
        temperature: float = 0.7,
        max_tokens: int = 512,
        constraints: List[Constraint] = [],
        n_candidates: int = 5
    ):
        self.simple_model = SimpleGenerativeModel(
            predictive_model,
            system_path,
            user_path,
            model_name,
            temperature,
            max_tokens,
            constraints
        )
        self.n_candidates = n_candidates

    def generate(
        self,
        message: str,
        target_audience: str,
        target_attitude: str,
        verbose: bool = False
    ) -> Tuple[str, str, str, List[str], float]:
        """
        Generate multiple candidates and select the best one based on the predictive model's score.
        """
        best_candidate = None
        best_score = float('-inf')
        
        for _ in range(self.n_candidates):
            result = self.simple_model.generate(message, target_audience, target_attitude, verbose=verbose)
            
            if result[0] != "Constraint not satisfied" and result[0] != "Score not improved":
                selected, edited, new_message, reasons, new_score = result
                
                if new_score > best_score:
                    best_candidate = result
                    best_score = new_score
            
            if verbose:
                print(f"Candidate {_ + 1}: {result}")
        
        if best_candidate is None:
            return "No improvement found", None, None, None, None
        
        return best_candidate

class EvolutionaryModel:
    def __init__(self, predictive_model: PredictiveModel, user_path: str = None, model_name: str = None, temperature: float = 0.7, max_tokens: int = 1024, max_edit_distance: float = 0.5):
        self.predictive_model = predictive_model
        
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

        # Load mutation and breeding prompts from files
        with open("prompts/mutation_template.txt", "r") as f:
            self.mutation_template = f.read()
        with open("prompts/breeding_template.txt", "r") as f:
            self.breeding_template = f.read()
        
        self.mutation_prompts = []
        with open(f"prompts/strategies.txt", "r") as f:
            mutations = f.readlines()
            self.mutation_prompts = [self.mutation_template.format(strategy=mutation) for mutation in mutations]

        self.breeding_prompts = []

        with open(f"prompts/{user_path}.txt", "r") as f:
            self.user_template = f.read()
        with open(f"prompts/breeding_gen.txt", "r") as f:
            self.user_breed_template = f.read()

    def mutate(self, message: Message, prompt: str, target_audience: str, target_attitude: str) -> Message:
        """
        Mutate the message based on the given prompt.
        """
        system = prompt
        old_content = message.content
        user = self.user_template.format(message=message.content, target_audience=target_audience, target_attitude=target_attitude)
        
        llm_response = llm_generate(self.model_name, system, user, temperature=self.temperature, max_tokens=self.max_tokens)
        try:
            parsed_response = parse_response(llm_response)
        except AttributeError as e:
            print("warning: failed to parse response", llm_response)
            print(e)
            return None
        
        selected = parsed_response["selected"]
        edited = parsed_response["edited"]
        new_content = old_content.replace(selected, edited)

        try:
            new_score = self.predictive_model.predict(new_content, target_audience, target_attitude)
        except ValueError as e:
            print("warning: failed to predict score", new_content)
            new_score = 0.0
        return Message(new_content, selected=parsed_response["selected"],
                       edited=parsed_response["edited"], reasons=parsed_response["reasons"], thought=parsed_response["thought"],
                       score=new_score, parent1=message, operation=f"Mutation: {prompt}")

    def breed(self, message1: Message, message2: Message, prompt: str, target_audience: str, target_attitude: str) -> Message:
        """
        Combine properties of two messages based on the prompt.
        """
        system = prompt
        old_content = message1.content
        user = self.user_breed_template.format(message1=message1.content, message2=message2.content, target_audience=target_audience, target_attitude=target_attitude)

        llm_response = llm_generate(self.model_name, system, user, temperature=self.temperature, max_tokens=self.max_tokens)
        parsed_response = parse_response(llm_response)
        
        selected = parsed_response["selected"]
        edited = parsed_response["edited"]
        new_content = old_content.replace(selected, edited)
        new_score = self.predictive_model.predict(new_content, target_audience, target_attitude)

        return Message(new_content, new_score, parent1=message1, parent2=message2, operation=f"Breeding: {prompt}")

    def generate(self, initial_message: str, target_audience: str, target_attitude: str, mutation: bool, breeding: bool,
                 num_generations: int = 10, population_size: int = 5, constraints: List[Constraint] = [], num_reps: int=2,
                 verbose:bool = True, diversity_threshold: float = 0.3) -> List[Message]:
        """
        Generate an improved message using an evolutionary strategy.
        """
        initial_score = self.predictive_model.predict(initial_message, target_audience, target_attitude)
        all_generated = [Message(initial_message, selected="", edited="", reasons="", thought="", score=initial_score)]
        population = [Message(initial_message, selected="", edited="", reasons="", thought="", score=initial_score)]

        for g in tqdm.tqdm(range(num_generations)):
            new_population = []
            
            # Mutation
            if mutation:
                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    mutation_futures = []
                    for msg in population:
                        for _ in range(num_reps):
                            for prompt in self.mutation_prompts:
                                mutation_futures.append(executor.submit(self.mutate, msg, prompt, target_audience, target_attitude))
                    
                    for future in concurrent.futures.as_completed(mutation_futures):
                        if future.result():
                            new_population.append(future.result())

            # Breeding
            if breeding:
                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    breeding_futures = []
                    for i in range(len(population)):
                        for j in range(i+1, len(population)):
                            for prompt in self.breeding_prompts:
                                breeding_futures.append(executor.submit(self.breed, population[i], population[j], prompt, target_audience, target_attitude))
                    
                    
                    for future in concurrent.futures.as_completed(breeding_futures):
                        new_population.append(future.result())

            if verbose:
                print(f"len(new_population): {len(new_population)}")
            all_generated.extend(new_population)

            # apply constraints
            for constraint in constraints:
                edit_distances = [editdistance.eval(msg.content, initial_message) for msg in new_population]
                print(f"sample message: {new_population[0].content}")
                print(len(initial_message))
                print(f"edit_distances: {edit_distances}")
                new_population = [msg for msg in new_population if constraint.predicate(msg.content)]

            if verbose:
                print(f"len(new_population) after constraints: {len(new_population)}")
                if len(new_population) > 0:
                    print(f"Generation {g + 1} - Best Score: {max(new_population, key=lambda x: x.score).score}")
                    print(f"Best Message: {max(new_population, key=lambda x: x.score).content}")
            new_population = population + new_population
            # Select top individuals
            # population = sorted(new_population, key=lambda x: x.score, reverse=True)[:population_size//2]
            # add a few random individuals from the new population
            # population.extend(random.sample(new_population, population_size//2))
            
            # Select top individuals
            diverse_population = []
            diversity_threshold = len(initial_message) * 0.1 
            for new_msg in sorted(new_population, key=lambda x: x.score, reverse=True):
                if all(self.is_diverse(new_msg.content, existing_msg.content, diversity_threshold) for existing_msg in diverse_population):
                    diverse_population.append(new_msg)
                    if len(diverse_population) == population_size:
                        break
            population = diverse_population
        # best_message = max(population, key=lambda x: x.score)
        # return best_message
        return population
    
    @staticmethod
    def is_diverse(message1: str, message2: str, threshold: float) -> bool:
        """
        Check if two messages are diverse based on edit distance.
        """
        distance = editdistance.eval(message1, message2)
        return distance < threshold

# Example usage
if __name__ == "__main__":
    model_id = "yqvpjyjq"
    baseten_api_key = "H2vfMDp6.la70Hf7ilEqUu9PdWvixLHpiPUG9jbvE"
    max_edit_distance = 0.5
    predictive_model = PredictiveModel(model_name="gpt-4o", model_id=model_id, baseten_api_key=baseten_api_key)

    initial_message = "Fossil fuels make our planet sick; they’re like a cigarette to our lungs or alcohol to our liver. They make extreme weather events, like extreme heat waves, wildfires, and droughts, more frequent and severe. 2023 was another year of record-breaking heat. These changes threaten our health by affecting the food we eat, the water we drink, and the air we breathe. Most importantly, it’s putting our children’s futures at risk. It’s our responsibility to leave behind a safe, livable world for future generations. For our children’s sake - and their children’s sake, we must leave fossil fuels behind and move towards better, safer energy sources. The solutions we need already exist: it’s clean energy - like wind, solar, nuclear, and hydropower. We can’t let our leaders back down from reducing our carbon pollution. It’s our duty to protect the future for those we love - before it’s too late."
    target_audience = "US General Population"
    target_attitude = "I support immediate action by the government to address climate change."

    edit_distance_constraint = Constraint(
        description = "The message must not differ too much from the original message.",
        predicate = lambda message: editdistance.eval(initial_message, message) < len(initial_message)*max_edit_distance
    )
    length_constraint = Constraint(
        description="The message should not be too long or too short compared to the original message.",
        predicate=lambda message: len(message) < len(initial_message) * 1.2 and len(message) > len(initial_message) * 0.8
    )
        
    constraints = [edit_distance_constraint, length_constraint]

    initial_score = predictive_model.predict(initial_message, target_audience, target_attitude)
    print(f"Initial Score: {initial_score}")

    # simple_model = SimpleGenerativeModel(predictive_model, system_path="simple_gen_highlight", user_path="user_gen", model_name="Llama 3 70B", temperature=0.7, max_tokens=768, constraints=constraints)
    # selected, edited, improved_message, reasons, improved_score = simple_model.generate(initial_message, target_audience, target_attitude, verbose=True)

    # bestofn = BestOfNGenerativeModel(predictive_model, system_path="simple_gen_highlight", user_path="user_gen", model_name="Llama 3 70B", temperature=0.7, max_tokens=768, constraints=constraints, n_candidates=5)
    # selected, edited, improved_message, reasons, improved_score = bestofn.generate(initial_message, target_audience, target_attitude, verbose=True)

    # if edited is None:
    #     print(selected)
    # else:
    #     print(f"Initial Message: {initial_message}")
    #     print(f"Selected: {selected}")
    #     print(f"Edited: {edited}")
    #     print(f"Improved Message: {improved_message}")
    #     print(f"Reasons: {reasons}")
    #     print(f"Improved Score: {improved_score}, Initial Score: {initial_score}")
    evolutionary_model = EvolutionaryModel(
    predictive_model,
    user_path="user_gen",
    model_name="gpt-4o",
    temperature=0.7,
    max_tokens=512,
    max_edit_distance=max_edit_distance/5
    )

    best_messages = evolutionary_model.generate(
        initial_message, 
        target_audience, 
        target_attitude, 
        constraints=constraints,
        mutation=True,
        breeding=False,
        num_generations=5, 
        population_size=2
    )

    print(f"Initial Message: {initial_message}")
    print(f"Initial Score: {initial_score}")
    print()
    print(f"Best Messages: {len(best_messages)}")
    for message in best_messages:
        print(f"Message: {message.content}")
        print(f"Score: {message.score}")
        print(f"Reasons: {message.reasons}")
        print()


