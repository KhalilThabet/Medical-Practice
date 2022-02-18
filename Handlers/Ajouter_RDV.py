import sys

sys.path.insert(1, "../")

from Verifications.Cin import Cin_verif
from .Date_Heure import Date_Heure

def Ajouter_RDV():

    RDV = open("../DATA/rdv.txt", "a")
    Cin = input("Veuillez saisir le Cin Du Patient !\t")
    while Cin_verif(Cin) == "False":
        Cin = input(
            "Veuillez saisir un Cin Correct! ou Appuyez sur Q pour Retourner a la page d'acceuil\t"
        )
        if Cin.upper() == "\Q":
            # M_P()
            break
    c = Date_Heure()
    ligne = Cin + " " + c + "\n"
    RDV.writelines(ligne)
    RDV.close()
