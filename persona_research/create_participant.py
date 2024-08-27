import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from .data.data_processor import participants_anes
from .data.data_processor import participants_w26
from .data.data_processor import participants_w27
from .data.data_processor import participants_w29
from .data.data_processor import participants_w32
from .data.data_processor import participants_w34
from .data.data_processor import participants_w36
from .data.data_processor import participants_w41
from .data.data_processor import participants_w42
from .data.data_processor import participants_w43
from .data.data_processor import participants_w45
from .data.data_processor import participants_w49
from .data.data_processor import participants_w50
from .data.data_processor import participants_w54
from .data.data_processor import participants_w82
from .data.data_processor import participants_w92
from .data.data_processor import participants_global
from . import args

'''
# mock participant dataset for testing
participant_list = [
    {
        "Participant_1": [
            {
                "race": "white",
                "gender": "male",
                "age": "young",
                "ideology": "conservative", 
                "party": "Republican",
                "political_interest": "medium",
                "church": "often",
                "discussing_politics": "sometimes", 
                "flag_patriotism": "high", 
                "state": "Texas"
                "year": "2012" 
            },
            {
                "election_2012": "Romney"
            }
        ],
    },
    {

        "Participant_2": [
            {
                "race": "asian",
                "gender": "male",
                "age": "mom",
                "ideology": "communist", 
                "party": "republican",
                "political_interest": "high",
                "church": "always",
                "discussing_politics": "never", 
                "flag_patriotism": "high", 
                "state": "Nevada"
            },
            {
                "election_2012": "Romney"
            }
        ]
    }
]
'''

def has_answered_key_questions(human, indices):
    # checks if all of the key fields are answered for a participant 
    for i in indices:
        if (human.all_fields[i] == "Missing" or human.all_fields[i] == "" or human.all_fields[i] == " " or human.all_fields[i] == "Refused"):
            return False
    return True

def sample_participant_external(num_to_sample, dataset):
    #Take in the participant list, and sample n participants
    dataset_participants = None
    global_participants = {
        "ANES": participants_anes,
        "oqa_guns": participants_w26,
        "oqa_work": participants_w27,
        "oqa_gender": participants_w29,
        "oqa_community": participants_w32,
        "oqa_science": participants_w34,
        "oqa_glass_ceiling": participants_w36,
        "oqa_gov_role": participants_w41,
        "oqa_expert_sources": participants_w42,
        "oqa_race": participants_w43,
        "oqa_online_sources": participants_w45,
        "oqa_social_media": participants_w49,
        "oqa_family": participants_w50,
        "oqa_econ_inequality": participants_w54,
        "oqa_international_affairs": participants_w82,
        "oqa_2020_general": participants_w92,
    }
    dataset_participants = global_participants.get(dataset)

    chosen_participants = np.array([])  # To keep track of chosen participants
    attempted_participants = set()  # To keep track of attempted participants

    print("Sampling participants...")
    print("Total Number of Participants: " + str(len(dataset_participants)))
    print("Number of Participants Chosen: " + str(len(chosen_participants)))

    while (len(chosen_participants)) < (num_to_sample):
        if len(attempted_participants) % 100 == 0:
            print("Number of Participants Attempted: " + str(len(attempted_participants)))
        if len(attempted_participants) >= 3000:
            print("All participants have been tried.")
            return False, [], []

        chosen_participant = np.random.choice(list(dataset_participants))

        attempted_participants.add(chosen_participant)

        if chosen_participant not in chosen_participants:
            if len(chosen_participants) < num_to_sample:
                chosen_participants = np.append(chosen_participants, chosen_participant)
            
            print("Number of Participants Chosen: " + str(len(chosen_participants)))

    return chosen_participants

def sample_participant(indices):
    #Take in the participant list, and sample n participants
    dataset_participants = None
    if args.dataset.value[0] == "ANES":
        dataset_participants = participants_anes
    elif args.dataset.value[0] == "w26":
        dataset_participants = participants_w26
    elif args.dataset.value[0] == "w27":
        dataset_participants = participants_w27
    elif args.dataset.value[0] == "w29":
        dataset_participants = participants_w29
    elif args.dataset.value[0] == "w32":
        dataset_participants = participants_w32
    elif args.dataset.value[0] == "w34":
        dataset_participants = participants_w34
    elif args.dataset.value[0] == "w36":
        dataset_participants = participants_w36
    elif args.dataset.value[0] == "w41":
        dataset_participants = participants_w41
    elif args.dataset.value[0] == "w42":
        dataset_participants = participants_w42
    elif args.dataset.value[0] == "w43":
        dataset_participants = participants_w43
    elif args.dataset.value[0] == "w45":
        dataset_participants = participants_w45
    elif args.dataset.value[0] == "w49":
        dataset_participants = participants_w49
    elif args.dataset.value[0] == "w50":
        dataset_participants = participants_w50
    elif args.dataset.value[0] == "w54":
        dataset_participants = participants_w54
    elif args.dataset.value[0] == "w82":
        dataset_participants = participants_w82
    elif args.dataset.value[0] == "w92":
        dataset_participants = participants_w92

    chosen_participants_train = np.array([])  # To keep track of chosen participants
    chosen_participants_test = np.array([])  # To keep track of chosen participants
    attempted_participants = set()  # To keep track of attempted participants

    print("Sampling participants...")
    print("Total Number of Participants: " + str(len(dataset_participants)))
    print("Number of Participants Chosen: " + str(len(chosen_participants_train) + len(chosen_participants_test)))

    while (len(chosen_participants_train) + len(chosen_participants_test)) < (args.num_participants_train + args.num_participants_test):
        if len(attempted_participants) % 100 == 0:
            print("Number of Participants Attempted: " + str(len(attempted_participants)))
        if len(attempted_participants) >= 3000:
            print("All participants have been tried.")
            return False, [], []

        chosen_participant = np.random.choice(list(dataset_participants))

        attempted_participants.add(chosen_participant)

        if chosen_participant not in chosen_participants_train and chosen_participant not in chosen_participants_test and has_answered_key_questions(chosen_participant, indices):
            if len(chosen_participants_train) < args.num_participants_train:
                chosen_participants_train = np.append(chosen_participants_train, chosen_participant)
            elif len(chosen_participants_test) < args.num_participants_test:
                chosen_participants_test = np.append(chosen_participants_test, chosen_participant)
            
            print("Number of Participants Chosen: " + str(len(chosen_participants_train) + len(chosen_participants_test)))

    return True, chosen_participants_train, chosen_participants_test


