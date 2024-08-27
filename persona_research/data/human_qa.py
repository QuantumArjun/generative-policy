class HumanQA:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def getAttributes(self):
        return self.__dict__

