'''
Module: prism_participant.py
Author: akaranam
Description: Class to store the participants from the PRISM dataset
'''

from dataclasses import dataclass, field
from typing import List
from data.PRISM.conversation import Conversation


@dataclass
class Participant:
    user_id: int
    survey_only: bool
    num_completed_conversations: int
    consent: bool
    consent_age: int
    lm_familiarity: str
    lm_indirect_use: str
    lm_direct_use: str
    lm_frequency_use: str
    self_description: str
    system_string: str
    age: int
    gender: str
    employment_status: str
    education: str
    marital_status: str
    english_proficiency: str
    study_id: str
    study_locale: str
    religion: str
    ethnicity: str
    location: str
    lm_usecases: str
    stated_prefs: str
    order_lm_usecases: str
    order_stated_prefs: str
    generated_datetime: str
    timing_duration_s: int
    timing_duration_mins: float
    included_in_US_REP: bool
    included_in_UK_REP: bool
    included_in_balanced_subset: bool
    conversations: List[Conversation] = field(
        default_factory=list)  # List to store Conversation objects
    identity_paragraph: str = ""
    stated_values_paragrah: str = ""
    conversation_preferences: List[str] = field(default_factory=list)
    conversations_paragraph: str = ""

    def create_identity_paragraph(self) -> None:
        # Extract the relevant fields
        lm_familiarity = self.lm_familiarity
        lm_frequency_use = self.lm_frequency_use
        self_description = self.self_description
        system_string = self.system_string
        age = self.age
        gender = self.gender
        employment_status = self.employment_status
        education = self.education
        marital_status = self.marital_status
        religion = self.religion.get('categorized', 'not specified')
        ethnicity = self.ethnicity.get('categorized', 'not specified')
        location = self.location.get('birth_country', 'not specified')
        stated_prefs = self.stated_prefs

        # Construct the identity paragraph
        paragraph = (
            f"I am {age} years old and identify as {gender}. "
            f"I work as {employment_status}, and I have an education level of {education}. "
            f"My marital status is {marital_status}. I practice {religion} and belong to the {ethnicity} ethnic group. "
            f"I live in {location}. Regarding my familiarity with language models, I would describe myself as {lm_familiarity}, "
            f"and I use them {lm_frequency_use}."
        )

        # Store the paragraph in the identity_paragraph attribute
        self.identity_paragraph = paragraph

    def create_stated_values_paragraph(self) -> None:
        # Extract the relevant fields
        stated_prefs = self.stated_prefs
        lm_usecases = self.lm_usecases

        # Sort the stated preferences by their values
        sorted_prefs = sorted(
            self.order_stated_prefs.items(), key=lambda item: item[1])

        # Format the sorted preferences into a string
        sorted_prefs_str = ' > '.join([pref[0] for pref in sorted_prefs])

        # Construct the stated values paragraph
        paragraph = (
            f"Here are my beliefs about how language models should believe. "
            f"Overall, models should '{self.self_description}'. ",
            f"If I were to write a system string for a language model, it would be: '{self.system_string}'. "
            f"When it comes to the importance of different factors in evaluating language models, I view them in this order: {sorted_prefs_str}."
        )

        # Store the paragraph in the stated_values_paragraph attribute
        self.stated_values_paragraph = paragraph[0]

    def extact_conversation_preferences(self) -> List[str]:
        processed_conversations = []
        for conversation in self.conversations:
            conversation_history = conversation.conversation_history
            filtered_messages = [d for d in conversation_history if d.get(
                "turn") == 0 and d.get("role") == "model"]

            # Creating the conversation preferences dict, and extracting the opening prompt
            conversation_preferences_dict = {}
            conversation_preferences_dict["opening_prompt"] = conversation.opening_prompt

            # Soorting the accepted and rejected messages
            for message in filtered_messages:
                if message.get("if_chosen") == True:
                    conversation_preferences_dict["chosen"] = message.get(
                        "content")
                else:
                    conversation_preferences_dict["not_chosen"] = message.get(
                        "content")

            # Extracting the conversation preferences
            scored_preferences = conversation.choice_attributes
            conversation_preferences_dict["scored_preferences"] = scored_preferences

            # Rank the preferences
            scored_preferences = {k: (0 if v == None else v)
                                  for k, v in scored_preferences.items()}
            sorted_preferences = sorted(
                scored_preferences.items(), key=lambda item: item[1], reverse=True)
            ranked_preferences = [value[0] for value in sorted_preferences]
            conversation_preferences_dict["ranked_preferences"] = ranked_preferences

            processed_conversations.append(conversation_preferences_dict)

        self.conversation_preferences = processed_conversations
    
    def create_conversations_paragraph(self): 
        paragraphs = []
        
        for conversation in self.conversation_preferences:
            top_preferences = conversation['ranked_preferences'][:2]
            try: 
                paragraphs.append(
                    f"Given the prompt '{conversation['opening_prompt']}', I was given two choices: '{conversation['not_chosen']}' and '{conversation['chosen']}'. "
                    f"Of the two, I preferred '{conversation['chosen']}' because I believe it did well on {top_preferences[0]} and {top_preferences[1]}.\n"
                )
            except:
                pass
                #TODO - SOmething about that one example that doesn't have a not chosen tag

        # Join all paragraphs into a single text
        paragraph = " ".join(paragraphs)
        self.conversations_paragraph = paragraph

        
