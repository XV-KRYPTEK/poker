from Main import Main
from Flop import Flop


class Calcul:
    nbCarteVariable = 0

    def __init__(self,main,flop,nbJ):
        self.main = main
        self.flop = flop
        self.nbJ = nbJ
        self.nbCarteVariable = 2*nbJ

    def getValeurMain(self):
        return self.main.getValeurMain()
    
    def getChance(self):
        pass

    def listeMainGagnates(self):
        self.listeMainGagnantes.append()
    
    def contientPaire(self):
        tab =[]
        res = []
        for i in self.flop.getCartes():
            tab.append(i)
        for y in self.main.getCartes():
            tab.append(y)
        for carte1 in tab:
            for carte2 in tab:
                if carte1 != carte2:
                    print(f"carte1.getSymbole() {carte1.getSymbole()} carte2.getSymbole() {carte2.getSymbole()}")
                    print(f"res.__ge__((carte1.getSymbole(),carte2.getSymbole())) {res.__ge__((carte1.getSymbole(),carte2.getSymbole()))}")
                    if carte1.getSymbole() == carte2.getSymbole() and not res.count((carte1.getSymbole(),carte2.getSymbole())):
                        res.append((carte1.getSymbole(),carte2.getSymbole())) #faut pas qu'il y ait plusieur fois la paire dans la liste
                        
        if len(res) == 0:
            return False
        else:
            return res

    def contientDoublePaire(self, parameter_list):
        return False
    
    def contientBrelan(self):
        tab =[]
        res = []
        for i in self.flop.getCartes():
            tab.append(i)
        for y in self.main.getCartes():
            tab.append(y)
        for carte1 in tab:
            for carte2 in tab:
                for carte3 in tab:
                    if carte1 != carte2 and carte1 != carte3 and carte2 != carte3:
                        if carte1.getSymbole() == carte2.getSymbole() == carte3.getSymbole():
                            res.append((carte1.getSymbole(),carte2.getSymbole(),carte3.getSymbole()))
        
        if len(res) == 0:
            return False
        else:
            return res 
        
    def contientFull(self):
        return False

    def contientSuite(self):
        return False

    def contientSuiteCouleur(self):
        return False

    def contientSuiteRoyale(self):
        return False

    def contientCouleur(self):
        return False

    def contientCarre(self):
        return False

    def topCarte(self): #TODO faut voir si c'est important de savoir si la carte est dans la main ou dans le flop
        max = 0
        carte = None
        for i in self.main.getCartes():
            if max<i.getSymbole():
                max = i.getSymbole()
                carte = i
        return carte

    def toutTest(self):
        if self.contientSuiteRoyale() is True:
            return "SuiteRoyale : ",self.contientSuiteRoyale()
        elif self.contientSuiteCouleur() is True:
            return "SuiteCouleur : ",self.contientSuiteCouleur()
        elif self.contientCarre() is True:
            return "Carre : ",self.contientCarre()
        elif self.contientFull() is True:
            return "Full : ",self.contientFull()
        elif self.contientCouleur() is True:
            return "Couleur : ",self.contientCouleur()
        elif self.contientSuite() is True:
            return "Suite : ",self.contientSuite()
        elif self.contientBrelan() is True:
            return "Brelan : ",self.contientBrelan()
        elif self.contientDoublePaire() is True:
            return "DoublePaire : ",self.contientDoublePaire()
        elif self.contientPaire() is True:
            return "Paire : ",self.contientPaire()
        else:
            return self.topCarte()
        