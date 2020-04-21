from Symbole import Symbole
from Couleur import Couleur

class Carte:
    def __init__(self,symbole,couleur):
        self.symbole = symbole
        self.couleur = couleur

    def getSymbole(self):
        return self.symbole

    def getCouleur(self):
        return self.couleur

    def __str__(self):
        return str((self.symbole,self.couleur))