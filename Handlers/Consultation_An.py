import sys

sys.path.insert(1, "../")
import numpy as np
import matplotlib.pyplot as plt
import M_P


def Consultation_An():

    File = open("../DATA/Nbr_consultation.txt")
    Liste = []
    Nbr_consultation = []
    for ligne in File:
        L = ligne.split(" ")
        Liste.append(int(L[1]))
    An = []
    j = 0
    while Liste != []:
        for u in Liste:
            u = Liste[0]
            x1 = Liste.count(u)
            for k in range(x1):
                Liste.remove(u)
            An += [u]
            Nbr_consultation.append(int(x1))
            j += 1
            print(An)
    File.close()
    for i in range(j, len(An)):
        Nbr_consultation += [0]
    for i in An:
        a = An.index(i)
        plt.bar(i, Nbr_consultation[a], label=str(i), width=0.3)
    plt.legend()
    plt.show()
    M_P()
