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

    def get_system_prompt(self, domain):
        """
        Generates the system prompt for policy curation

        Args:
            domain (str): The domain for which policy curation are being generated

        Returns:
            str: The system prompt for policy curation
        """
        prompts = PromptsForPolicyStatementGenerator()
        return prompts.get_system_prompt(domain)


class PromptsForPolicyRefinment:
    def __init__(self):
        """Initializes the PromptsForPolicyStatementGenerator agent"""

    def get_system_prompt(self, domain):
        """
        Generates the system prompt for policy curation

        Args:
            domain (str): The domain for which policy curation are being generated

        Returns:
            str: The system prompt for policy curation
        """
        prompts = PromptsForPolicyStatementGenerator()
        return prompts.get_system_prompt(domain)

    
    def _get_contentious_policy_prompt(self, p1, p2):
        return f"""
        You have the following two policy (Objective, Strategy) that are contentious. Make a comprised policy (Objective, Strategy) where the original purpose of the policy is kept in-tact.
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
        You voted against the following policy (Objective, Strategy): "{policy}"
        Based on your beliefs, please provide a detailed explanation for your vote.
        """

    def _get_refinement_prompt(self, policy, feedback):
        return f"""
        Refine the following policy (Objective, Strategy) while preserving its original intent: "{policy}"

        Consider the following feedback from the voters: 
        "{feedback}"
        """

    def get_refinement_prompt(self, domain, policy, feedback):
        prompts = PromptsForPolicyStatementGenerator()
        return f"""
        {prompts._get_policy_statement_explanation_prompt()}
        {self._get_refinement_prompt(policy, feedback)}
        {prompts._get_formatting_prompt()}
        """

