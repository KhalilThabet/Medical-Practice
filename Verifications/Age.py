import sys


def Age_verif(x):  # Fonction que verfie que l'age est composee de chiffres
    try:
        int(x)
        return "True"
    except:
        return "False"


# Tester
# if __name__ == '__main__':
#     for arg in sys.argv[1:]:
#         print(Age_verif(arg))
