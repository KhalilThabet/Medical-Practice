from Src.M_P import M_P
def Supprimer_patient():
    cin = input("Saisir le cin du patient a supprimer :")
    file = open("patient.txt")
    Patient_a_conserver = []
    ligne = file.readlines()
    for i in ligne:
        L = i.split(" ")
        if L[0] != cin:
            Patient_a_conserver += i
    file.close()
    file = open("patient.txt", "w")
    file.writelines(Patient_a_conserver)
    file.close()
    M_P()
