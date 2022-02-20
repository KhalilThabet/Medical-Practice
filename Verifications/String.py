import sys


def String_verif(
    x,
):  # Fonction que verifie que la chaine de caractere n'est pas composee d'entier
    a = 0
    p = 0
    for i in x:
        try:
            int(i)
        except:
            a += 1
        if i == "":
            p += 1
    if (a == len(x)) and (p != len(x)):
        return "True"
    else:
        return "False"


# Tester
# if __name__ == "__main__":
#     for arg in sys.argv[1:]:
#         print(String_verif(arg))
