import os
from Verifications.Cin import Cin_verif
import Date_Heure
from Src.M_P import M_P

def Ajouter_RDV():

    RDV = open("rdv.txt", "a")
    Cin = input("Veuillez saisir le Cin Du Patient !")
    while Cin_verif(Cin) == "False":
        Cin = input(
            'Veuillez saisir un Cin Correct! ou Appuyez sur "Q" pour Retourner a la page d\'acceuil'
        )
        if Cin.upper() == "\Q":
            M_P()
            break
    c = Date_Heure()
    ligne = Cin + " " + c + "\n"
    RDV.writelines(ligne)
    RDV.close()
    M_P()
