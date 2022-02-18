import sys

sys.path.insert(1, "../")
from Src.M_P_L import M_P_L
from Handlers.Ajouter_Patient import ajouter_Patient
from Handlers.Ajouter_RDV import Ajouter_RDV
from Handlers.Annuler_RDV import Annuler_RDV

# from Handlers.Consultation_An import Consultation_An
# from Handlers.Consultation_Mois import Consulation_Mois
# from Handlers.Historique_Patient import Historique_patient
from Handlers.Ordonnanceur import Ordonnance
from Handlers.Supprimer_Patient import Supprimer_patient
from Handlers.Modifier_RDV import Modifier_RDV
from Handlers.CreateFile import Creation_fichier_patient


def M_P():  # fonction du prgramme principale

    M_P_L()  # appelle a la fonction Look du programme
    dict = {
        "1": Creation_fichier_patient,
        "2": ajouter_Patient,
        "3": Supprimer_patient,
        "4": Ajouter_RDV,
        "5": Annuler_RDV,
        "6": Modifier_RDV,
        "7": Ordonnance,
        "8": "Historique_patient",
        "9": "Consulation_Mois",
        "10": "Consultation_An",
    }  # dictionnaire contenant les fonctions du programme exigees
    print("")
    c = input()
    dict[c]()


M_P()
