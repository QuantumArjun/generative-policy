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
        return f"""
        You are an assistant tasked with generating creative and impactful policy objectives for the domain of {domain}.
        A policy objective is a clear, specific goal or desired outcome that an organization aims to achieve.
        These objectives should be high-level statements that outline the intended direction or desired impact of policies within the domain.
        For example, a policy objective might be: "Increase access to affordable housing for low-income families within urban areas."
        
        Your task is to develop policy objectives that are:
        - Specific: Clearly defined and focused on a particular goal or outcome.
        - Measurable: Able to be tracked and assessed for progress and effectiveness.
        - Achievable: Realistic and attainable within the given resources and constraints.
        - Relevant: Directly related to the domain and addressing key issues or opportunities.
        - Time-bound: Set within a clear timeframe for implementation and review.
        - High-level: No implementation details.
        - Concise: Use a limited number of words.

        """

    def _get_domain_prompt(self, domain):
        """
        Generates the domain prompt for policy statements

        Args:
            domain (str): The domain for which policy statements are being generated

        Returns:
            str: The domain prompt for policy statements
        """
        return f"Provide a list of creative and impactful policy objectives for the domain of {domain}."

    def _get_formatting_prompt(self):
        """
        Generates the formatting prompt for policy statements

        Returns:
            str: The formatting prompt for policy statements
        """
        return f"Make sure each policy objective is wrapped with <Statement> at the beginning and a </Statement> followed by new line at the end."

    def _get_policy_statement_explanation_prompt(self):
        """
        Generates the policy statement explanation prompt for policy statements

        Returns:
            str: The policy statement explanation prompt for policy statements
        """
        return """A policy objective is essentially the big-picture objective that a policy aims to achieve.
                It's a broad statement that outlines the desired outcome or direction.
                Policy objectives should be a sentence long description.
                Here are a couple of examples of policy objectives:
                - Improve literacy rates among children
                - Reduce the prevalence of diabetes among adults
                - Reduce greenhouse gas emissions in the transportation sector
                - Increase the employment rate for recent college graduates
                - Expand public transportation infrastructure in rural areas
                Here are examples of policy statements that are too specific to be called policy objectives:
                - Establish a grant program to support the creation of engaging and interactive online safety 
                 resources specifically tailored for children, ensuring that they are informative 
                 and age-appropriate, with funding sourced from the national budget.
                -  Allocate a portion of the national budget to establish a research institute
                  dedicated to studying the impact of social media on children's mental health 
                  and well-being, with the aim of informing evidence-based policy decisions.  
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
                So far, you have come up with the following policy objectives: {", ".join(policy_set)}. 
                Please come up with new policy objectives that are completely different from the ones outlined above.
            """

    def _get_policy_axis_prompt(self, axis):
        """
        Generates the policy axis prompt for policy statements

        Args:
            axis (str): The axis for which policy statements are being generated

        Returns:
            str: The policy axis prompt for policy statements
        """
        return f"Each policy objective has to contribute to the following axis: {axis}."

    def _get_policy_axes_prompt(self, axes):
        """
        Generates the policy axis prompt for policy statements

        Args:
            axis (str): The axis for which policy statements are being generated

        Returns:
            str: The policy axis prompt for policy statements
        """
        return f"Each policy objective has to contribute to one of the following axis: {", ".join(axes)}."

    def _get_policy_stakeholder_prompt(self, stakeholder):
        """
        Generates the policy stakeholder prompt for policy statements

        Args:
            stakeholder (str): The stakeholder for which policy statements are being generated

        Returns:
            str: The policy stakeholder prompt for policy statements
        """
        return f"Each policy objective has to be helping this stakeholder: {stakeholder}."

    def _get_policy_stakeholders_prompt(self, stakeholders):
        """
        Generates the policy stakeholder prompt for policy statements

        Args:
            stakeholder (str): The stakeholder for which policy statements are being generated

        Returns:
            str: The policy stakeholder prompt for policy statements
        """
        return f"Each policy objective has to be helping at least one of these stakeholders: {", ".join(stakeholders)}."

    def _get_policy_problem_prompt(self, problem):
        """
        Generates the policy problem prompt for policy statements

        Args:
            problem (str): The problem for which policy statements are being generated

        Returns:
            str: The policy problem prompt for policy statements
        """
        return f"Each policy objective has to solve the following problem: {problem}."

    def _get_policy_problems_prompt(self, problems):
        """
        Generates the policy problem prompt for policy statements

        Args:
            problem (str): The problem for which policy statements are being generated

        Returns:
            str: The policy problem prompt for policy statements
        """
        return f"Each policy objective has to solve at least one of the following problems: {", ".join(problems)}."

    def get_user_messsage_base(self, domain):
        """
        Generates the user message for base policy statement generation

        Returns:
            str: The user message for base policy statement generation
        """
        return f"""
            {self._get_policy_statement_explanation_prompt()}
            {self._get_domain_prompt(domain)}
            {self._get_formatting_prompt()}
        """

    def get_user_message_chaining(self, domain, policy_set):
        """
        Generates the user message for policy statement generation using chaining

        Args:
            policy_set (set): The set of policy statements generated so far

        Returns:
            str: The user message for policy statement generation using chaining
        """
        return f"""
                    {self._get_policy_statement_explanation_prompt()}
                    {self._get_domain_prompt(domain)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_formatting_prompt()}
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
                    {self._get_policy_statement_explanation_prompt()}
                    {self._get_domain_prompt(domain)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_policy_axis_prompt(axis)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_formatting_prompt()}
                """

    def get_user_message_along_axis_and_stakeholder(self, domain, policy_set, axes, stakeholder):
        """
        Generates the user message for policy statement generation using along stakeholder

        Args:
            policy_set (set): The set of policy statements generated so far

        Returns:
            str: The user message for policy statement generation using along stakeholder
        """
        return f"""
                    {self._get_policy_statement_explanation_prompt()}
                    {self._get_domain_prompt(domain)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_policy_axes_prompt(axes)}
                    {self._get_policy_stakeholder_prompt(stakeholder)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_formatting_prompt()}
                """

    def get_user_message_along_axis_and_stakeholder_and_problems(self, domain, policy_set, axes, stakeholders, problem):
        """
        Generates the user message for policy statement generation using along stakeholder

        Args:
            policy_set (set): The set of policy statements generated so far

        Returns:
            str: The user message for policy statement generation using along stakeholder
        """
        return f"""
                    {self._get_policy_statement_explanation_prompt()}
                    {self._get_domain_prompt(domain)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_policy_axes_prompt(axes)}
                    {self._get_policy_stakeholder_prompt(stakeholders)}
                    {self._get_policy_problem_prompt(problem)}
                    {self._get_generated_policy_statements_prompt(policy_set)}
                    {self._get_formatting_prompt()}
                """

    def get_uniqueness_system_prompt(self):
        """
        Generates the uniqueness system prompt for policy statements

        Returns:
            str: The uniqueness system prompt for policy statements
        """
        return "You are an assistant that helps decide if a new policy objective is different those already generated."

    def get_uniqueness_user_message_prompt(self, statement_list, policy_statement):
        """
        Generates the uniqueness user message prompt for policy statements

        Returns:
            str: The uniqueness user message prompt for policy statements
        """
        return f"""
            Give these current policy objectives: {', '.join(statement_list)}
            and the new policy objective: {policy_statement}
            output true if the new policy objective different than all of the current policy objectives, or false if it is a duplicate.
            Also output false if the policy objective is not a valid policy objective. Output only one of two words: 'true' or 'false'.
            """
    
if __name__ == "__main__":
    print(PromptsForPolicyStatementGenerator().get_system_prompt("Social Media and Child Safety"))
    print(PromptsForPolicyStatementGenerator().get_user_messsage_base("Social Media and Child Safety"))
