"""
Class: PromptsForPolicyCuration
Author: mhelabd
Description: This class is used to generate prompts for policy curation.
"""
import sys
sys.path.append(".")
from agents.policy_statements.prompts import PromptsForPolicyStatementGenerator

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


class PromptsForPolicyRefinment:
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

    def _get_formatting_prompt(self):
        """
        Generates the formatting prompt for policy statements

        Returns:
            str: The formatting prompt for policy statements
        """
        return f"""
        Format each policy objective and strategy as follows: <Statement>Objective: (The Policy Objective), Strategy: (The policy strategy)</Statement>
        """
    
    def _get_contentious_policy_prompt(self, p1, p2):
        return f"""
        You have the following two policies that are contentious. Make a comprised policy where the original purpose of the policy is kept in-tact.
        Policy 1: {p1}
        Policy 2: {p2}
        """

    def get_contentious_policy_prompt(self, domain, p1, p2):
        prompts = PromptsForPolicyStatementGenerator()
        return f"""
        {prompts._get_policy_statement_explanation_prompt()}
        {prompts._get_domain_prompt(domain)}
        {self._get_contentious_policy_prompt(p1, p2)}
        {prompts._get_formatting_prompt()}
        """

    def get_feedback_prompt(self, domain, policy):
        return f"""
        In this domain: {domain}
        You voted against the following policy: "{policy}"
        Based on your beliefs, please provide a detailed explanation for your vote.
        """

    def _get_refinement_prompt(self, policy, feedback):
        return f"""
        Refine the following policy while preserving its original intent: "{policy}"

        Consider the following feedback from the voters: 
        "{feedback}"
        """

    def get_refinement_prompt(self, domain, policy, feedback):
        prompts = PromptsForPolicyStatementGenerator()
        return f"""
        {prompts._get_policy_statement_explanation_prompt()}
        {prompts._get_domain_prompt(domain)}
        {self._get_refinement_prompt(policy, feedback)}
        {prompts._get_formatting_prompt()}
        """

