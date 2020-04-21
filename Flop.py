


class Flop:
    carte1 = ""
    carte2 = ""
    carte3 = ""
    listeMainGagnantes=[]

    def __init__(self,carte1,carte2,carte3):
        self.carte1 = carte1
        self.carte2 = carte2
        self.carte3 = carte3

    def getCartes(self):
        return [self.carte1,self.carte2,self.carte3]



        