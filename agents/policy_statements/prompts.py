"""
Class: PromptsForPolicyStatementGenerator
Author: mhelabd
Description: This class is used to generate prompts for policy statements
"""


class PromptsForPolicyStatementGenerator:
    def __init__(self):
        """Initializes the PromptsForPolicyStatementGenerator agent"""

    def get_system_prompt(self, domain):
        """
        Generates the system prompt for policy statements

        Args:
            domain (str): The domain for which policy statements are being generated

        Returns:
            str: The system prompt for policy statements
        """
        return f"You are an assistant helping come up with creative policy solutions to the domain of {domain}."

    def _get_domain_prompt(self, domain):
        """
        Generates the domain prompt for policy statements

        Args:
            domain (str): The domain for which policy statements are being generated

        Returns:
            str: The domain prompt for policy statements
        """
        return f"Your goal is to come up with policy goals that are creative and innovative in the domain {domain}"

    def _get_formatting_prompt(self):
        """
        Generates the formatting prompt for policy statements

        Returns:
            str: The formatting prompt for policy statements
        """
        return f"Make sure each policy goal is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end."

    def _get_policy_statement_explanation_prompt(self):
        """
        Generates the policy statement explanation prompt for policy statements

        Returns:
            str: The policy statement explanation prompt for policy statements
        """
        return """A policy goal is essentially the big-picture objective that a policy aims to achieve.
                It's a broad statement that outlines the desired outcome or direction.
                Policy goals should be a sentence long description.
            """

    def _get_generated_policy_statements_prompt(self, policy_set):
        """
        Generates the generated policy statements prompt for policy statements

        Args:
            policy_set (set): The set of policy statements generated so far

        Returns:
            str: The generated policy statements prompt for policy statements
        """
        return f"""
                So far, you have come up with the following policy goals: {", ".join(policy_set)}. 
                Please come up with additional policy goals.
            """

    def _get_policy_axis_prompt(self, axis):
        """
        Generates the policy axis prompt for policy statements

        Args:
            axis (str): The axis for which policy statements are being generated

        Returns:
            str: The policy axis prompt for policy statements
        """
        return f"Each policy goal has to contribute to the following axis: {axis}."

    def _get_policy_stakeholder_prompt(self, stakeholder):
        """
        Generates the policy stakeholder prompt for policy statements

        Args:
            stakeholder (str): The stakeholder for which policy statements are being generated

        Returns:
            str: The policy stakeholder prompt for policy statements
        """
        return f"Each policy goal has to be helping this stakeholder: {stakeholder}."

    def get_user_messsage_base(self, domain):
        """
        Generates the user message for base policy statement generation

        Returns:
            str: The user message for base policy statement generation
        """
        return f"""
            {self._get_domain_prompt(domain)}
            {self._get_formatting_prompt()}
            {self._get_policy_statement_explanation_prompt()}
        """

    def get_user_message_chaining(self, domain, policy_set):
        """
        Generates the user message for policy statement generation using chaining

        Args:
            policy_set (set): The set of policy statements generated so far

        Returns:
            str: The user message for policy statement generation using chaining
        """
        return f"""{self._get_domain_prompt(domain)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_formatting_prompt()}
                    {self._get_policy_statement_explanation_prompt()}
                """

    def get_user_message_along_axis(self, domain, policy_set, axis):
        """
        Generates the user message for policy statement generation using along axis

        Args:
            policy_set (set): The set of policy statements generated so far

        Returns:
            str: The user message for policy statement generation using along axis
        """
        return f"""
                    {self._get_domain_prompt(domain)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_policy_axis_prompt(axis)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_formatting_prompt()}
                    {self._get_policy_statement_explanation_prompt()}
                """

    def get_user_message_along_axis_and_stakeholder(self, domain, policy_set, axis, stakeholder):
        """
        Generates the user message for policy statement generation using along stakeholder

        Args:
            policy_set (set): The set of policy statements generated so far

        Returns:
            str: The user message for policy statement generation using along stakeholder
        """
        return f"""
                    {self._get_domain_prompt(domain)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_policy_axis_prompt(axis)}
                    {self._get_policy_stakeholder_prompt(stakeholder)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_formatting_prompt()}
                    {self._get_policy_statement_explanation_prompt()}
                """

    def get_uniqueness_system_prompt(self):
        """
        Generates the uniqueness system prompt for policy statements

        Returns:
            str: The uniqueness system prompt for policy statements
        """
        return "You are an assistant that helps decide if a new policy statement is different those already generated."
    
    def get_uniqueness_user_message_prompt(self, statement_list, policy_statement):
        """
        Generates the uniqueness user message prompt for policy statements

        Returns:
            str: The uniqueness user message prompt for policy statements
        """
        return f"""
            Give these current policy statements: {', '.join(statement_list)}
            and the new policy statement: {policy_statement}
            output true if the new policy statement different than all of the current policies, or false if it is a duplicate.
            Also output false if the policy is not a valid policy. Output only one of two words: 'true' or 'false'.
            """