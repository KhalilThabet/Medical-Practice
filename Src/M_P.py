import sys
sys.path.insert(1, "../")
from Src.M_P_L import M_P_L
from Handlers.Ajouter_Patient import ajouter_Patient
from Handlers.Ajouter_RDV import Ajouter_RDV
from Handlers.Annuler_RDV import Annuler_RDV
from Handlers.Consultation_An import Consultation_An
from Handlers.Consultation_Mois import Consulation_Mois
from Handlers.Historique_Patient import Historique_patient
from Handlers.Ordonnanceur import Ordonnance
from Handlers.Supprimer_Patient import Supprimer_patient
from Handlers.Modifier_RDV import Modifier_RDV
from Handlers.CreateFile import Creation_fichier_patient

def M_P():  # fonction du prgramme principale

    M_P_L()  # appelle a la fonction Look du programme
    dict = {
        "0": Creation_fichier_patient,
        "1": ajouter_Patient,
        "2": Supprimer_patient,
        "3": Ajouter_RDV,
        "4": Annuler_RDV,
        "5": Modifier_RDV,
        "6": Ordonnance,
        "7": Historique_patient,
        "8": Consulation_Mois,
        "9": Consultation_An,
    }  # dictionnaire contenant les fonctions du programme exigees
    print("")
    return dict

System= input("saisir votre systeme d'exploitation (UNIX || WINDOWS)").upper()
if System=="UNIX":
    import getch as m
else:
    import msvcrt as m
while 1:
    temp=M_P()
    if System=="WINDOWS":
        c=m.getch().decode("utf-8")
    else:
        c=m.getch()
    if (c=='q'): break
    temp[c](System)