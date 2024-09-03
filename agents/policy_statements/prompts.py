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
        You are an assistant tasked with generating creative and impactful policy objectives and strategies for the domain of {domain}.
        
        A policy objective is a clear, specific goal or desired outcome that a policy aims to achieve. 
        It should be measurable, achievable, relevant, and time-bound (SMART).
        
        A policy strategy is a high-level approach or plan designed to accomplish a policy objective.
        It outlines the general course of action to be taken, without specifying detailed tactics or implementation steps.
        
        Objectives and strategies should be:

        - Specific: Clearly defined and focused.
        - Measurable: Quantifiable or observable.
        - Achievable: Realistic and attainable.
        - Relevant: Aligned with the domain's goals.
        - Time-bound: Indicating a timeframe for completion.
        - High-level: Avoiding detailed implementation steps.
        - Concise: Using clear and succinct language.
        
        Additionally, you should ensure that the generated policy objectives are diverse. You want to make sure that your policies capture the entire space of possible policies, even (and especially) those that might be unpopular or controversial. 

        Good Examples:
        <Statement>Objective: Reduce greenhouse gas emissions, Strategy: Invest in renewable energy infrastructure and promote energy efficiency.</Statement>
        <Statement>Objective: Reduce particulate matter pollution in urban areas, Strategy: Enhance public transportation systems.</Statement>
        <Statement>Objective: Increase organic farming practices, Strategy: Provide financial incentives and technical support for organic farmers.</Statement>
        <Statement> Objective: Increase renewable energy production, Strategy: Mandate the shut down of fossil fuel power plants.</Statement>
        <Statement>Objective: Make healthcare more affordable, Strategy: Nationalize healthcare and move to a single player system.</Statement>
        
        Bad Examples:
        <Statement>Objective: Make social media safer for children.</Statement> (Lacks policy strategy)
        <Statement>Strategy: Develop a government-funded app that monitors children's social media activity and alerts parents to potential dangers.</Statement> (Focuses on implementation details, not the general approach)
        <Statement>Objective: Improve Child Safety online, Strategy: Establish a grant program to support the creation of engaging and interactive online safety resources specifically tailored for children, ensuring that they are informative and age-appropriate, with funding sourced from the national budget.</Statement> (Focuses on implementation details, not the general approach)
        """

    def _get_domain_prompt(self, domain):
        """
        Generates the domain prompt for policy statements

        Args:
            domain (str): The domain for which policy statements are being generated

        Returns:
            str: The domain prompt for policy statements
        """
        return f"Provide a list of creative and impactful policy objectives and strategies for the domain of {domain}."

    def _get_formatting_prompt(self):
        """
        Generates the formatting prompt for policy statements

        Returns:
            str: The formatting prompt for policy statements
        """
        return f"""
        Format each policy objective and strategy as follows: <Statement>Objective: (The Policy Objective), Strategy: (The policy strategy)</Statement>
        """

    def _get_policy_statement_explanation_prompt(self):
        """
        Generates the policy statement explanation prompt for policy statements

        Returns:
            str: The policy statement explanation prompt for policy statements
        """
        # This is not needed anymore
        return ""
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
                So far, you have come up with the following policy (objectives, strategies) pairs: {", ".join(policy_set)}. 
                Please come up with new policy objectives and strategies that are completely different from the ones outlined above.
            """

    def _get_policy_axis_prompt(self, axis):
        """
        Generates the policy axis prompt for policy statements

        Args:
            axis (str): The axis for which policy statements are being generated

        Returns:
            str: The policy axis prompt for policy statements
        """
        return f"Each policy (objective, strategy) pair has to go either up or down this axis: {axis}. 
                For example, if the policy is: Objective: Reduce greenhouse gas emissions, Strategy: Invest in renewable energy infrastructure and promote energy efficiency, and the axis is cost, then you should generate policies that either increase the cost or decrease the cost."

    def _get_policy_axes_prompt(self, axes):
        """
        Generates the policy axis prompt for policy statements

        Args:
            axis (str): The axis for which policy statements are being generated

        Returns:
            str: The policy axis prompt for policy statements
        """
        return f"Each policy (objective, strategy) pair has to contribute to one of the following axis: {", ".join(axes)}. 
                For example, if the policy is: Objective: Reduce greenhouse gas emissions, Strategy: Invest in renewable energy infrastructure and promote energy efficiency, and the axis is cost, then you should generate policies that either increase the cost or decrease the cost."

    def _get_policy_stakeholder_prompt(self, stakeholder):
        """
        Generates the policy stakeholder prompt for policy statements

        Args:
            stakeholder (str): The stakeholder for which policy statements are being generated

        Returns:
            str: The policy stakeholder prompt for policy statements
        """
        return f"Each policy (objective, strategy) pair has to be helping this stakeholder: {stakeholder}. 
                 For example, if the policy is: Objective: Reduce greenhouse gas emissions, Strategy: Invest in renewable energy infrastructure and promote energy efficiency, and the stakeholder is fossil fuel companies, then you should generate policies that that a fossil fuel executive may write."

    def _get_policy_stakeholders_prompt(self, stakeholders):
        """
        Generates the policy stakeholder prompt for policy statements

        Args:
            stakeholder (str): The stakeholder for which policy statements are being generated

        Returns:
            str: The policy stakeholder prompt for policy statements
        """
        return f"Each policy (objective, strategy) pair has to be helping at least one of these stakeholders: {", ".join(stakeholders)}."

    def _get_policy_problem_prompt(self, problem):
        """
        Generates the policy problem prompt for policy statements

        Args:
            problem (str): The problem for which policy statements are being generated

        Returns:
            str: The policy problem prompt for policy statements
        """
        return f"Each policy (objective, strategy) pair has to be an effective solution to the following problem: {problem}."

    def _get_policy_problems_prompt(self, problems):
        """
        Generates the policy problem prompt for policy statements

        Args:
            problem (str): The problem for which policy statements are being generated

        Returns:
            str: The policy problem prompt for policy statements
        """
        return f"Each policy (objective, strategy) pair has to solve at least one of the following problems: {", ".join(problems)}."

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
        return "You are an assistant that helps decide if a new policy (objective, strategy) pair is valid and unique from those already generated."

    def get_uniqueness_user_message_prompt(self, statement_list, policy_statement):
        """
        Generates the uniqueness user message prompt for policy statements

        Returns:
            str: The uniqueness user message prompt for policy statements
        """
        return f"""
            Give these current policy (objectives, strategy) pairs: {', '.join(statement_list)}
            and the new policy (objective, strategy) pair: {policy_statement}
            output true if the new policy (objective, strategy) pair is different than all of the current policy pairs, or false if it is a duplicate.
            
            Use the following criteria to determine if it's a duplicate: 
            - The new policy (objective, strategy) pair is allowed to have the same objective, but not the same (objective, strategy) as another pair in the list.
            - The new policy (objective, strategy) may be different from another pair in the list, but would have the same effect as another policy (objective, strategy) pair in the list. For example, if the new policy would "partner with mental health organizations to create and disseminate positive online content that encourages healthy self-image and wellbeing", and another policy already in the list would "partner with mental health organizations to integrate resource-sharing features directly into popular social media platforms targeting children", consider this as a duplicate, since the generated policy would have the same effect as the other policy.
            
            Also output false if the new policy (objective, strategy) pair is not valid, where valid means it adheres to defined criteria for policy objectives and strategies. 
            
            Think step by step, first finding the most similar policies in the list to the new policy, and then compare the new policy with each of those policies, seeing if it is a duplicate.
            
            After reasoning if the new policy is a duplicate, output only one of two words: 'true' or 'false', surrounded by <answer>. For example, every output should end with <answer>true</answer>, or <answer>false</answer>.
            """


if __name__ == "__main__":
    # python3 agents/policy_statements/prompts.py
    print(PromptsForPolicyStatementGenerator().get_system_prompt("Social Media and Child Safety"))
    print(PromptsForPolicyStatementGenerator().get_user_messsage_base("Social Media and Child Safety"))
