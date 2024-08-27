from enum import Enum

class DatasetLabels(Enum):
    anes = ("ANES", 10)
    oqa_guns = ("w26", 78, "Gun Rights")
    oqa_work = ("w27", 78, "Technology in the Workplace")
    oqa_gender = ("w29", 70, "Gender Issues")
    oqa_community = ("w32", 78, "Community Issues")
    oqa_science = ("w34", 78) # Has an issue with the dataset
    oqa_glass_ceiling = ("w36", 78)
    oqa_gov_role = ("w41", 78)
    oqa_expert_sources = ("w42", 78) # Not enough finished entries
    oqa_race = ("w43", 78, "Race")
    oqa_online_sources = ("w45", 78)
    oqa_social_media = ("w49", 78)
    oqa_family = ("w50", 78)
    oqa_econ_inequality = ("w54", 78, "Economic Inequality")
    oqa_international_affairs = ("w82", 78)
    oqa_2020_general = ("w92", 78, "Issues in the 2020 Election")

dataset = DatasetLabels.oqa_guns

model_name = "openai"    # name of the model to use [openai,claude]
model_version = "chatgpt-4o-latest"    # version of the model to use: gpt-3.5-turbo, gpt-4-1106-preview, gpt-4-0314, gpt-4-turbo-preview
optimizer_model_version = "chatgpt-4o-latest"    # version of the model to use: gpt-3.5-turbo, gpt-4-1106-preview, gpt-4-0314, gpt-4-turbo-preview
steps = 1               # number of steps to run the optimizer
num_questions = 15        # number of questions alloted to question creator
num_participants_train = 2        # number of participants to sample from the dataset
num_participants_test = 0        # number of participants to sample from the dataset
run_test = False         # whether to run the test population or not
scoring = "quadratic" # scoring function to use: exponential, quadratic, linear

num_train_questions = 0
num_val_questions = 5
num_optimizer_context = 5
domain = dataset.value[2]

#CRFM Args
use_crfm = False         # whether to use the CRFM model or not
max_tokens = 30          # maximum number of tokens to generate
temperature = 0.9        # temperature for the CRFM model
question_asking_max_tokens = 64 # maximum number of tokens to generate for the questioner
question_answering_max_tokens = 128 # maximum number of tokens to generate for the digital twin
question_prompt_max_tokens = 640 # maximum number of tokens to generate for the question prompt

#Overall args
debug = False            # Whether to turn on debug mode

if debug:
    print("Debug mode activated")
    model_version = "gpt-3.5-turbo"
    optimizer_model_version = "gpt-3.5-turbo" 
    steps = 2
    num_questions = 2
    num_participants_train = 2
    num_participants_test = 0
    run_test = False  

    num_train_questions = 2
    num_val_questions = 2
    num_optimizer_context = 2   

Optimizer_Task = \
f"Your goal is to optimize the the persona text for a digital twin. You will receive two sets of transcripts - \
one answered by the real human, and one answered by the digital twin. You will also recieve the digital twin's persona text. Your goal is to improve \
the persona text provided to the digital twin, such that the digital twin can answer as similarly to the human as possible. Remember that the digital twin \
    cannot see the human's responses. It can only see the persona you provide. \n\n"