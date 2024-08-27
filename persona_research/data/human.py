class Human:
    def __init__(self, number, vote, year, race, gender, age, view, party, interest, church, discuss_disc, predicted_vote = None, flag = None, state=None):
        self.vote = vote # "Who did you vote for"
        self.race = race # Race / Ethnicity 
        self.year = year # Year of Public data
        self.predicted_vote = predicted_vote # Predicted vote 
        self.gender = gender # Gender of respondent
        self.age = age # Age
        self.view = view # Liberal / Conservative 
        self.party = party # Party affiliation 
        self.interest = interest # Interest in politics 
        self.church = church # Church affiliation 
        self.discuss_disc = discuss_disc # Do you have political discussion with your family
        self.flag = flag # Relating flag with patriotism 
        self.state = state # US state of respondent 
        self.number = number # the participant number
        self.all_fields = [vote, race, year, predicted_vote, gender, age, view, party, interest, church, discuss_disc, flag, state, number]
    
    def getAttributes(self):
        return self.__dict__
    
    def identityParagraph(self): 
        identity_paragraph = "Ideologically, I describe myself as " + self.view 
        identity_paragraph += ". Politically, I am " + self.view + ". Racially, I am " + self.race 
        identity_paragraph += ". I am " + self.gender + ". " + "In terms of my age, I am " + self.age
        identity_paragraph += ". I am from " + self.state + ". I have " + self.interest + " interest in politics"
        identity_paragraph += ". I go to church: " + self.church + ". I discuss politics: " + self.discuss_disc
        identity_paragraph += ". I associate " + self.flag + " patriotism with the American flag."
        identity_paragraph += "Be concise in your response. Do not reveal your demographic information in the answers."

        return identity_paragraph

