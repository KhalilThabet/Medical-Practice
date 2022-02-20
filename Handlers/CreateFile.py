import sys

sys.path.insert(1, "../")
from Verifications.Cin import Cin_verif
from Verifications.String import String_verif
from Verifications.Age import Age_verif
from Verifications.Sexe import Sexe_verif

def Creation_fichier_patient(System):
    i = 0
    while i < 10:
        Dpatient = {}
        ligne = ""
        try:
            File = open("../DATA/patient.txt")
            Test_Cin = File.readlines()
            
            Dpatient["Cin"] = input("saisir Cin\t")
            while (Cin_verif(Dpatient["Cin"]) == "False") and (a == 1):
                Dpatient["Cin"] = input("saisir un Cin Correct\t")
                for T in Test_Cin:
                    if T[0] != Dpatient["Cin"]:
                        a = 1
                    if T[0] == Dpatient["Cin"]:
                        a = 0
                    break
            File.close()
            Dpatient["Nom"] = input("saisir le Nom du Patient\t")
            while String_verif(Dpatient["Nom"]) == "False":
                Dpatient["Nom"] = input("saisir un Nom Correct\t")
            Dpatient["Prenom"] = input("Saisir le Prenom du Patient\t")
            while String_verif(Dpatient["Prenom"]) == "False":
                Dpatient["Prenom"] = input("saisir un prenom Correct\t")
            Dpatient["Age"] = input("saisir l'age du Patient\t")
            while Age_verif(Dpatient["Age"]) == "False":
                Dpatient["Age"] = input("Saisir un Age correct\t")
            Dpatient["Sexe"] = input("saisir le sexe du Patient\t")
            while Sexe_verif(Dpatient["Sexe"]) == "False":
                Dpatient["Sexe"] = input(
                    "Choisir entre un Sexe masculin ou un Sexe Feminin\t"
                )
            File = open("../DATA/patient.txt", "a")
            for valeur in Dpatient.values():
                ligne += str(valeur) + " "
            ligne += "_"
            ligne += "\n"
            File.writelines(ligne)
            File.close()
            C = input("Voulez-Vous Continuez A Rentrer Des Patients?\t")
            if C.upper() == "NON":
                break
            i += 1

        except:
            Dpatient["Cin"] = input("saisir Cin\t")
            while Cin_verif(Dpatient["Cin"]) == "False":
                Dpatient["Cin"] = input("saisir un Cin Correct\t")
            Dpatient["Nom"] = input("saisir le Nom du Patient\t")
            while String_verif(Dpatient["Nom"]) == "False":
                Dpatient["Nom"] = input("saisir un Nom Correct\t")
            Dpatient["Prenom"] = input("Saisir le Prenom du Patient\t")
            while String_verif(Dpatient["Prenom"]) == "False":
                Dpatient["Prenom"] = input("saisir un prenom Correct\t")
            Dpatient["Age"] = input("saisir l'age du Patient\t")
            while Age_verif(Dpatient["Age"]) == "False":
                Dpatient["Age"] = input("Saisir un Age correct\t")
            Dpatient["Sexe"] = input("saisir le sexe du Patient\t")
            while Sexe_verif(Dpatient["Sexe"]) == "False":
                Dpatient["Sexe"] = input(
                    "Choisir entre un Sexe masculin ou un Sexe Feminin\t"
                )
            File = open("../DATA/patient.txt", "a")
            for valeur in Dpatient.values():
                ligne += str(valeur) + " "
            ligne += "_"
            ligne += "\n"
            File.writelines(ligne)
            File.close()
            C = input("Voulez-Vous Continuez A Rentrer Des Patients?\t")
            if C.upper() == "NON":
                break
            i += 1


# if __name__ == "__main__":
#     Creation_fichier_patient()
