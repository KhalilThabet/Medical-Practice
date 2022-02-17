from Src.M_P import M_P
def Annuler_RDV():
        Cin=input("Entrez le CIN ici:")
        Rdv=open("rdv.txt")
        Candidat=""
        for ligne in Rdv :
                L=ligne.split(" ")
                if L[0]==Cin:
                        continue;
                Candidat+=ligne
        Rdv.close()
        File=open("rdv.txt","w")
        File.writelines(Candidat)
        File.close()
        M_P()