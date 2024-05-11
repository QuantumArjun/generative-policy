import random

class NameGenerator:
    def __init__(self):
        """
        Initializes the name generator with a list of gender-neutral first names.
        """
        self.names = ['Alex', 'Jordan', 'Taylor', 'Casey', 'Riley', 'Jamie', 'Morgan', 'Robin', 'Dakota', 'Skyler']
        self.shuffle_names()

    def shuffle_names(self):
        """
        Shuffles the names and creates an iterator.
        """
        random.shuffle(self.names)
        self.name_iterator = iter(self.names)

    def generate_random_first_name(self):
        """
        Generates a random first name without repeating until all names have been used.
        Returns to the start and reshuffles once all names are exhausted.
        """
        try:
            return next(self.name_iterator)
        except StopIteration:
            print("All names have been used. Reshuffling.")
            self.shuffle_names()
            return next(self.name_iterator)