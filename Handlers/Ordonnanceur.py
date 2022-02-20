import sys

sys.path.insert(1, "../")
from Handlers.Medicaments import medicament

def Ordonnance(System):
    if System=="UNIX":
        import getch as m
    else:
        import msvcrt as m
    Cin = input("veuillez entrer le CIN :\t")
    try:
        File = open("../DATA/rdv.txt")
        Patient = " "
        Tp = " "
        for ligne in File:
            L = ligne.split(" ")
            if L[0] == Cin:
                try:
                    File_Patient = open("../DATA/patient.txt")
                    for ligne_patient in File_Patient:
                        T = ligne_patient.split(" ")
                        if T[0] == Cin:
                            Nom_nouveau_fichier = "Historique_" + T[0] + ".txt"
                            sub_file = open("../DATA/{}".format(Nom_nouveau_fichier), "w")
                            ligne = (
                                L[0]
                                + " "
                                + T[1]
                                + " "
                                + T[2]
                                + " "
                                + L[1]
                                + " "
                                + L[2]
                                + "\n"
                            )
                            sub_file.writelines(ligne)
                            while 1:
                                Tp = medicament(System)
                                sub_file.write(Tp)
                                print(
                                    "Voulez-vous inscrire un autre medicament? ", end=" "
                                )
                                print("*1- oui", end=" ")
                                print("*2- non")
                                if System=="WINDOWS":
                                    c = m.getch().decode("utf-8")
                                else:
                                    c= m.getch()
                                for i in c:
                                    try:
                                        int(i)
                                        c = chr(i)
                                    except:
                                        a = 0
                                if c == "2":
                                    break
                            sub_file.close()
                            sub_file = open("../DATA/{}".format(Nom_nouveau_fichier))
                            New_fichier = "Historique_" + T[0] + ".txt"
                            Fichier_historique = open("../DATA/{}".format(New_fichier), "a")
                            A = (
                                "\n"
                                + "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                                + "\n"
                            )
                            ligne2 = sub_file.readlines()
                            Fichier_historique.writelines(ligne2)
                            Fichier_historique.writelines(A)
                            Fichier_historique.close()
                            sub_file.close()
                            try :
                                Fichier0 = open("../DATA/Nbr_consultation.txt", "a")
                                Fichier1 = open("../DATA/{}".format(Nom_nouveau_fichier))
                                L1 = Fichier1.readline()
                                T = L1.split(" ")
                                X = T[3][3] + T[3][4]
                                Y = T[3][6] + T[3][7] + T[3][8] + T[3][9]
                                Z = X + " " + Y + "\n"
                                Fichier0.writelines(Z)
                                Fichier1.close()
                                Fichier0.close()
                                sub_file.close()
                            except : 
                                print("Fichier Nbr_consultation.txt not found")
                    File_Patient.close()
                except:
                    print("fichier patient.txt introuvable\n")
        File.close()
    except:
        print("fichier rdv.txt introuvable\n")