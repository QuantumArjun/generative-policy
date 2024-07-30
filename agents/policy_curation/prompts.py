"""
Class: PromptsForPolicyCuration
Author: mhelabd
Description: This class is used to generate prompts for policy curation.
"""


class PromptsForPolicyCuration:
    def __init__(self):
        """Initializes the PromptsForPolicyStatementGenerator agent"""

    def get_system_prompt(self):
        """
        Generates the system prompt for policy curation

        Args:
            domain (str): The domain for which policy curation are being generated

        Returns:
            str: The system prompt for policy curation
        """
        return f"""
        You are an assistant helping come up with creative policy through curation.
        """
