from Calcul import Calcul
from Carte import Carte
from Main import Main 
from Symbole import Symbole
from Couleur import Couleur
from Flop import Flop

carte1=Carte(Symbole.AS,Couleur.PIQUE)
carte2=Carte(Symbole.AS,Couleur.CARREAU)
carte3=Carte(Symbole.SEPT,Couleur.PIQUE)
carte4=Carte(Symbole.AS,Couleur.CARREAU)
carte5=Carte(Symbole.AS,Couleur.PIQUE)

flop = Flop(carte3,carte4,carte5)

main = Main(carte1,carte2)

calcul = Calcul(main,flop,3)

print(calcul.topCarte())

