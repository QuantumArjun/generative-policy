"""
Module: embed_wrapper.py
Author: mhelabd
Description: This module contains a wrapper class for interacting with various embedding models.
"""

from langchain_community.embeddings import OpenAIEmbeddings

class EmbedWrapper:
    def __init__(self, model_config):
        self.model_config = model_config
        self.model_type = self.model_config.model_type

    def embed_text(self, text: str):
        """
        Generate embedding based on specified language model.
        :param text: The input text
        :return: The embedding for text
        """

        if self.model_type == "OpenAI":
            # Call OpenAI API to generate text
            model = OpenAIEmbeddings()
            embedding = model.embed_query(text)
        elif self.model_type == "Claude":
            embedding = "Claude model not yet supported."
        else:
            embedding = "Invalid model type specified."
        return embedding

    def embed_documents(self, docs: list[str]) -> list:
        """
        Generate embedding for multiple text documents based on specified language model.
        :param docs: A list of strings for text embedding
        :return: The embedding of each text
        """
        if self.model_type == "OpenAI":
            # Call OpenAI API to generate text
            model = OpenAIEmbeddings()
            embedding = model.embed_documents(docs)
        elif self.model_type == "Claude":
            embedding = "Claude model not yet supported."
        else:
            embedding = "Invalid model type specified."
        return embedding

