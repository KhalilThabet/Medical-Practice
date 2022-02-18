import sys

sys.path.insert(1, "../")

def Annuler_RDV():
    Cin = input("Entrez le CIN ici:\t")
    Rdv = open("../DATA/rdv.txt")
    Candidat = ""
    for ligne in Rdv:
        L = ligne.split(" ")
        if L[0] == Cin:
            continue
        Candidat += ligne
    Rdv.close()
    File = open("../DATA/rdv.txt", "w")
    File.writelines(Candidat)
    File.close()
