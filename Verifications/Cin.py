import sys


def Cin_verif(x):  # Fonction qui verifie que le Cin est composee de 8 chiffres
    a = 0
    try:
        int(x)
    except:
        a = 1
    if len(x) != 8 or a == 1:
        return "False"
    else:
        return "True"


# Tester
# if __name__ == '__main__':
#     for arg in sys.argv[1:]:
#         print(Cin_verif(arg))
