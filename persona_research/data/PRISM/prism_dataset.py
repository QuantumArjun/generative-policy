from datasets import load_dataset
from data.PRISM.participant import Participant
from data.PRISM.conversation import Conversation

def get_prism_data():
    # Extract all the humans
    dataset_survey = load_dataset("HannahRoseKirk/prism-alignment", "survey")
    participants = []
    for row in dataset_survey['train']:
        participant = Participant(
            user_id=row['user_id'],
            survey_only=row['survey_only'],
            num_completed_conversations=row['num_completed_conversations'],
            consent=row['consent'],
            consent_age=row['consent_age'],
            lm_familiarity=row['lm_familiarity'],
            lm_indirect_use=row['lm_indirect_use'],
            lm_direct_use=row['lm_direct_use'],
            lm_frequency_use=row['lm_frequency_use'],
            self_description=row['self_description'],
            system_string=row['system_string'],
            age=row['age'],
            gender=row['gender'],
            employment_status=row['employment_status'],
            education=row['education'],
            marital_status=row['marital_status'],
            english_proficiency=row['english_proficiency'],
            study_id=row['study_id'],
            study_locale=row['study_locale'],
            religion=row['religion'],
            ethnicity=row['ethnicity'],
            location=row['location'],
            lm_usecases=row['lm_usecases'],
            stated_prefs=row['stated_prefs'],
            order_lm_usecases=row['order_lm_usecases'],
            order_stated_prefs=row['order_stated_prefs'],
            generated_datetime=row['generated_datetime'],
            timing_duration_s=row['timing_duration_s'],
            timing_duration_mins=row['timing_duration_mins'],
            included_in_US_REP=row['included_in_US_REP'],
            included_in_UK_REP=row['included_in_UK_REP'],
            included_in_balanced_subset=row['included_in_balanced_subset']
        )

        participants.append(participant)

    participant_dict = {human.user_id: human for human in participants}

    # Extract all the conversations
    dataset_conversations = load_dataset("HannahRoseKirk/prism-alignment", "conversations")
    for row in dataset_conversations['train']:
        conversation = Conversation(
            user_id=row['user_id'],
            conversation_id=row['conversation_id'],
            conversation_type=row['conversation_type'],
            opening_prompt=row['opening_prompt'],
            conversation_turns=row['conversation_turns'],
            conversation_history=row['conversation_history'],
            performance_attributes=row['performance_attributes'],
            choice_attributes=row['choice_attributes'],
            open_feedback=row['open_feedback'],
            generated_datetime=row['generated_datetime'],
            timing_duration_s=row['timing_duration_s'],
            timing_duration_mins=row['timing_duration_mins'],
            included_in_balanced_subset=row['included_in_balanced_subset']
        )
        if row['user_id'] in participant_dict:
            participant_dict[row['user_id']].conversations.append(conversation)
    

    # Create Identity Paragraphs 
    for participant in participants:
        participant.create_identity_paragraph()
        participant.create_stated_values_paragraph()
        participant.extact_conversation_preferences()
        participant.create_conversations_paragraph()

    return participants


participants = get_prism_data()
print(participants[0].conversation_preferences)