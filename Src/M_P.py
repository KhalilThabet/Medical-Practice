from M_P_L import M_P_L
from ..Handlers.Creer_Fichier_Patient import Creation_fichier_patient
def M_P():  # fonction du prgramme principale
    import os
    import time

    M_P_L()  # appelle a la fonction Look du programme
    dict = {
        "1": "Creation_fichier_patient",
        "2": "ajouter_Patient",
        "3": "Supprimer_patient",
        "4": "Ajouter_RDV",
        "5": "Annuler_RDV",
        "6": "Modify_RDV",
        "7": "Ordonnance",
        "8": "Historique_patient",
        "9": "Consulation_Mois",
        "10": "Consultation_An",
    }  # dictionnaire contenant les fonctions du programme exigees
    print("")
    c = input()
    dict[c]()


M_P()
