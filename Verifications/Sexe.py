import sys


def Sexe_verif(x):  # Fonction qui verifie le sexe
    if (x.upper() == ("MASCULIN")) or (x.upper() == ("FEMININ")):
        return "True"
    else:
        return "False"


# Tester
# if __name__ == "__main__":
#     for arg in sys.argv[1:]:
#         print(Sexe_verif(arg))
