"""
Module: utils.py
Author: kanishk
Description: This is the general module for the evolutionary algorithm for policy evolution.
"""

import re
import requests
from openai import OpenAI

baseten_api_key = ""
oai_client = OpenAI(api_key="")

def llm_generate(model_name: str, system: str, user:str, temperature: float, max_tokens: int) -> str:
    if model_name == "Llama 3 8B":
        model_id = "yqvpjyjq"
        messages = [{"role":"system", "content":system}, {"role": "user", "content": user}]
        data = {
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        parse = lambda x: x.content.decode().split("<|end_header_id|>")[-1].split("<|eot_id|>")[0].strip()
    elif model_name == "Llama 3 70B":
        model_id = "7qrdl253"
        messages = [{"role":"system", "content":system}, {"role": "user", "content": user}]
        data = {
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        parse = lambda x: x.content.decode().split("<|end_header_id|>")[-1].split("<|eot_id|>")[0].strip()
    elif model_name == "gpt-4o":
        messages = [{"role":"system", "content":system}, {"role": "user", "content": user}]
        completion = oai_client.chat.completions.create(
            model=model_name,
            messages=messages
        )
        return completion.choices[0].message.content
    else:
        raise NotImplementedError(f"Model {model_name} not implemented")

    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json=data
    )

    return parse(resp)

def parse_response(response: str) -> dict[str, str]:
    original = re.search(r"<original>(.*?)</original>", response, re.DOTALL).group(1)
    thought = re.search(r"<thought>(.*?)</thought>", response, re.DOTALL).group(1)
    selected = re.search(r"<selected>(.*?)</selected>", response, re.DOTALL).group(1)
    edited = re.search(r"<edited>(.*?)</edited>", response, re.DOTALL).group(1)
    reasons = re.search(r"<reasons>(.*?)</reasons>", response, re.DOTALL).group(1)
    # return a dictionary with the parsed values
    return {
        "original": original,
        "thought": thought,
        "reasons": reasons,
        "selected": selected,
        "edited": edited,
    }
