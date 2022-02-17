from Src.M_P import M_P

def Historique_patient():
    Nom = input("saisir le Nom du patient")
    X = "Historique" + Nom + ".txt"
    Fichier = open(X)
    for ligne in Fichier:
        print(ligne)
    M_P()
