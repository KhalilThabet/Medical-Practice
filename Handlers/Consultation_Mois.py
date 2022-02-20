import sys

sys.path.insert(1, "../")
import matplotlib.pyplot as plt


def Consulation_Mois(System):
    File = open("../DATA/Nbr_consultation.txt")
    Liste = []
    Nbr_consultation = []
    for ligne in File:
        L = ligne.split(" ")
        Liste.append(int(L[0]))
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    j = 0
    while Liste != []:
        for u in Liste:
            u = Liste[0]
            x1 = Liste.count(u)
            for k in range(x1):
                Liste.remove(u)
            a = x[j]
            y1 = x.index(u)
            x[j] = x[y1]
            x[y1] = a
            Nbr_consultation.append(int(x1))
            j += 1
    File.close()
    for i in range(j, len(x)):
        Nbr_consultation += [0]
    for i in x:
        a = x.index(i)
        plt.bar(i, Nbr_consultation[a], label="n" + ":" + str(i), width=0.5)
    plt.legend()
    plt.show()
