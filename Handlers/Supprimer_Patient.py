import sys

sys.path.insert(1, "../")

def Supprimer_patient():
    cin = input("Saisir le cin du patient a supprimer :\t")
    file = open("../DATA/patient.txt")
    Patient_a_conserver = []
    ligne = file.readlines()
    for i in ligne:
        L = i.split(" ")
        if L[0] != cin:
            Patient_a_conserver += i
    file.close()
    file = open("../DATA/patient.txt", "w")
    file.writelines(Patient_a_conserver)
    file.close()
