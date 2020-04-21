from Carte import Carte

class Main:
    carte1 = ""
    carte2 = ""

    VALEUR_PROCHE = 10
    PAIRE = 1.2
    COULEUR = 10

    def __init__(self,carte1,carte2):
        self.carte1 = carte1
        self.carte2 = carte2

    def getValeurMain(self):
        value = self.carte1.symbole*self.carte2.symbole
        
        if self.carte1.symbole!=self.carte2.symbole:
            if self.estValeurProche(self.carte1,self.carte2):
                value += self.VALEUR_PROCHE
            if self.estCouleur(self.carte1,self.carte2):
                value += self.COULEUR
            return value 
        else:
            return value*self.PAIRE

    def estValeurProche(self,carte1,carte2):
        tmp=0
        val1 = carte1.getSymbole()
        val2 = carte2.getSymbole()
        if (val1>val2):
            tmp = val1
            val1 = val2
            val2 = tmp
        if (val1+1==val2 or val1+2==val2 or val1+3==val2):
            return True
        else: 
            return False

    def estCouleur(self,carte1,carte2):
        if carte1.getCouleur()==carte2.getCouleur():
            return True
        else:
            return False

    def getCartes(self):
        return [self.carte1,self.carte2]
