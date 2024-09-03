""""
Module: representative_comparison.py
Author: akaranam
Description: This serves as an evaluation for comparing the base human to the human representative on a set of policy statements
"""

class RepresentativeComparison:
    def __init__(self):
        self.policy_goals = None
    
    def vote_on_policy(self, agents) -> dict:
        policy_votes = {}
        for policy_goal in self.policy_goals:
                votes = self.vote_on_policy_goal(agents, policy_goal)
                policy_votes[policy_goal] = votes
        return policy_votes

    def vote_on_policy_goal(self, base_humans, policy_goal: str) -> list:
        votes = []
        for agent in base_humans:
                vote = agent.rate_opinion(policy_goal)
                votes.append(vote)
        return votes

    def evaluate(self, base_humans, digital_representatives, policy_goals):
        
        self.policy_goals = policy_goals
        
        base_human_matrix = self.vote_on_policy(base_humans)
        digital_representative_matrix = self.vote_on_policy(digital_representatives)
        
        print(base_human_matrix)
        print(digital_representative_matrix)
        
    
        