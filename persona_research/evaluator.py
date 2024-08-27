from data.data_processor import participants_data
import re

# The definition of words that belong to each category. 
Affiliation_list = {
    "R2012": ["romney", "mitt", "republican", "conservative", "2012"],
    "D2012": ["obama", "barack", "democrat", "democratic", "liberal", "2012"],
    "R2016": ["trump", "donald", "republican", "conservative", "2016"], 
    "D2016": ["clinton", "hillary", "rodham", "senator", "democrat", "democratic", "liberal", "2016"],
    "R2020": ["trump", "donald", "republican", "conservative", "2020"], 
    "D2020": ["joe", "joseph", "biden", "democratic", "democrat", "liberal", "2020"],
}

Voted_list = {
    "R2012": "Romney",
    "D2012": "Obama",
    "R2016": "Donald Trump",
    "D2016": "Hillary Clinton",
    "R2020": "Donald Trump",
    "D2020": "Joe Biden"
}

# A helper function that will help sort participants into buckets. 
def add_participant(data, participant, year, response):
    if participant not in data:
        data[participant] = []
    data[participant].append([year, response])

# A helper function that will parse the given sentence and find which categorty it is most aligned to. 
def find_most_affiliation(sentence):
    sentence = sentence.lower()  # Convert sentence to lowercase for case-insensitive comparison
    affiliation_counts = {key: 0 for key in Affiliation_list}
    
    for key, keywords in Affiliation_list.items():
        for value in keywords:
            if value in sentence:
                affiliation_counts[key] += 1
    
    most_affiliation = max(affiliation_counts, key=affiliation_counts.get)
    return most_affiliation

def find_last_number(input_string):
    numbers = re.findall(r'\d+', input_string)  # Find all numbers in the string
    if numbers:
        return int(numbers[-1])  # Return the last number found as an integer

def Simulate_Data(textfile):
    Simulated_Data = {}

    with open(textfile) as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            year = find_last_number(lines[i + 1])
            line = find_most_affiliation(lines[i] + str(year))
            Participant = "Participant_" + str(i // 2 + 1)
            add_participant(Simulated_Data, Participant, year, Voted_list[line])
    return Simulated_Data

def SimulatedDemographic(Data):
    # Then we have to find a way to parse through every demographic. 
    pass

def PercentageVote(textfile):
    Simulated_Data = Simulate_Data(textfile)
    correctResponses = 0 
    amountOfResponses = 0

    Incorrect = []

    for i in range(len(Simulated_Data)):
        Participant = str(list(Simulated_Data.keys())[i])
        if not participants_data[i].vote.find("Missing") or not participants_data[i].vote.find("Refused") or not participants_data[i].vote.find("Inapplicable") or not participants_data[i].vote.find("No"):
            continue

        if participants_data[i].vote == Simulated_Data[Participant][0][1]:
            correctResponses += 1

        else:
            Incorrect.append((Participant, participants_data[i].vote, Simulated_Data[Participant][0][1]))
        amountOfResponses += 1
        
    print(correctResponses/amountOfResponses)

# Given a demographic (race, gender, etc.) sample from human class and see if voting percentages align 
# def demographic_test(textfile, demographic):
PercentageVote("results/all_results.txt")