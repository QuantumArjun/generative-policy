"""
Module: llm_wrapper.py
Author: akaranam
Description: This module contains a wrapper class for interacting with various language models.
"""

from config import Config
from langchain_community.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
import anthropic

class LLMWrapper:
    def __init__(self, model_config):
        self.model_config = model_config
        self.model_type = self.model_config.model_type
        self.model_name = self.model_config.model_name

    def generate_text(self, system_prompt, user_message, max_tokens=4096) -> str:
        """
        Generate text based on the prompt using the specified language model.
        :param prompt: The input prompt for text generation
        :param max_tokens: The maximum number of tokens to generate
        :return: The generated text
        """

        if self.model_type == "OpenAI":
            # Call OpenAI API to generate text
            model = ChatOpenAI(model_name=self.model_name)
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_message),
            ]
            response = model.invoke(messages, max_tokens=max_tokens).content
       
        elif self.model_type == "Claude":
            # Call Claude API to generate text
            anthropic.Anthropic(api_key=self.model_config.api_key)
            response = model.messages.create(
                model=self.model_name,
                max_tokens=max_tokens,
                temperature=0,
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": user_message
                            }
                        ]
                    }
                ]
            ).content[0].text
        else:
            response = "Invalid model type specified."
        
        return response

    def clean_response(self, response, open, close) -> list:
        """
        Clean the response by extracting text between open and close tags.
        :param response: The generated response
        :param open: The opening tag
        :param close: The closing tag
        :return: List of cleaned responses
        """
        cleaned_responses = []
        start = response.find(open)
        while start != -1:
            end = response.find(close, start + len(open))
            if end == -1:
                break
            cleaned_responses.append(response[start + len(open):end])
            start = response.find(open, end + len(close))
        return cleaned_responses