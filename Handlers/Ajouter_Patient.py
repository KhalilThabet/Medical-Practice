from Verifications.Cin import Cin_verif
from Verifications.String import String_verif
from Verifications.Age import Age_verif
from Verifications.Sexe import Sexe_verif
from Src.M_P import M_P


def ajouter_Patient():
    try:
        File = open("patient.txt")
        Test_Cin = File.readlines()
        if Test_Cin == []:
            pass
        Dpatient = {}
        ligne = ""
        Dpatient["Cin"] = input("saisir Cin")
        while (Cin_verif(Dpatient["Cin"]) == "False") and (a == 1):
            Dpatient["Cin"] = input("saisir un Cin Correct")
            for T in Test_Cin:
                if T[0] != Dpatient["Cin"]:
                    a = 1
                if T[0] == Dpatient["Cin"]:
                    a = 0
                    break
        File.close()
        Dpatient["Nom"] = input("saisir le Nom du Patient")
        while String_verif(Dpatient["Nom"]) == "False":
            Dpatient["Nom"] = input("saisir un Nom Correct")
        Dpatient["Prenom"] = input("Saisir le Prenom du Patient")
        while String_verif(Dpatient["Prenom"]) == "False":
            Dpatient["Prenom"] = input("saisir un prenom Correct")
        Dpatient["Age"] = input("saisir l'age du Patient")
        while Age_verif(Dpatient["Age"]) == "False":
            Dpatient["Age"] = input("Saisir un Age correct")
        Dpatient["Sexe"] = input("saisir le sexe du Patient")
        while Sexe_verif(Dpatient["Sexe"]) == "False":
            Dpatient["Sexe"] = input(
                "Choisir entre un Sexe masculin ou un Sexe Feminin"
            )
        File = open("patient.txt", "a")
        for valeur in Dpatient.values():
            ligne += str(valeur) + " "
        ligne += "\n"
        File.writelines(ligne)
        File.close()
    except:
        print("fichier inexistant")
    M_P()
