import sys

sys.path.insert(1, "../")

def Historique_patient(System):
    Cin = input("saisir le Cin du patient \t")
    print('\n')
    X = "../DATA/Historique_" + Cin + ".txt"
    Fichier = open(X)
    for ligne in Fichier:
        print(ligne)
