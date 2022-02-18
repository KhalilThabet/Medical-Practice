import sys

sys.path.insert(1, "../")
import M_P

def Historique_patient():
    Nom = input("saisir le Nom du patient \t")
    X = "Historique" + Nom + ".txt"
    Fichier = open(X)
    for ligne in Fichier:
        print(ligne)
    M_P()
