import args
import math


def linear_scoring(index1, index2, num_questions):
    return 1.0 / (abs(index1 - index2) + 1)


def quadratic_scoring(index1, index2, num_questions):
    return 1.0 / ((abs(index1 - index2) + 1)**2)


def exponential_scoring(index1, index2, num_questions):
    return 1.0 / (math.exp(abs(index1 - index2) + 1))


def score_responses(key_questions, responses, key_answer_choices):
    total_score = 0
    max_score = 0
    all_questions = []

    for participant_num, participant in enumerate(responses):
        for i in range(len(participant[0])):
            correct_index = key_answer_choices[i].index(participant[1][i])
            score = None
            if participant[0][i] in key_answer_choices[i]:
                predicted_index = key_answer_choices[i].index(
                    participant[0][i])
                if args.scoring == "exponential":
                    score = exponential_scoring(
                        correct_index, predicted_index, len(key_answer_choices[i]))
                elif args.scoring == "quadratic":
                    score = quadratic_scoring(
                        correct_index, predicted_index, len(key_answer_choices[i]))
                elif args.scoring == "linear":
                    score = linear_scoring(
                        correct_index, predicted_index, len(key_answer_choices[i]))
            else:
                score = 0

            curr_question = key_questions[i]
            total_score += score
            max_score += 1

            all_questions.append(
                (curr_question, participant[0][i], participant[1][i], score, participant_num))

    return total_score, all_questions, max_score


def score_prism_responses(responses):
    total_score = 0
    max_score = 0

    for question in responses:
        if question[0] == "a)" or question[0] == "b)":
            # We have a binary choice
            if question[0] == question[1]:
                total_score += 1
            max_score += 1
        else:
            # We have the ranking question
            predicted_set = set(question[0].lower().split(","))
            correct_set = set(question[1])
            total_score += jaccard_similarity(predicted_set, correct_set)
            max_score += jaccard_similarity(correct_set, correct_set)
    
    return total_score, max_score


def jaccard_similarity(set_a, set_b):
    """
    Calculates the Jaccard similarity between two sets.

    Args:
        set_a (set): The first set.
        set_b (set): The second set.

    Returns:
        float: The Jaccard similarity between the two sets.
    """
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)

    if len(union) == 0:
        return 0.0
    else:
        return len(intersection) / len(union)
