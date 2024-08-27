class HumanGlobal:
    def __init__(self, country, question, option, selection):
        self.question = question
        self.country = country
        self.option = option
        self.selection = selection
        
    def getAttributes(self):
        return self.__dict__
    
    def identityParagraph(self, datas): 
        identity_paragraph = "I describe myself as " + self.country 
        for data in datas:
            identity_paragraph += ". In response to " + data.question + ", given these selection, " + data.option + ", I give back " + data.selection

        return identity_paragraph