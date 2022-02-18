from .Date_Heure import Date_Heure
def Modifier_RDV():
    Cin=input("Entrez le CIN ici:\t")
    Rdv=open("../DATA/rdv.txt")
    Patient=""
    for ligne in Rdv:
        L=ligne.split(" ")
        if L[0]==Cin:
                ligne=L[0]+" " +Date_Heure()+"\n"
        Patient+=ligne
    Rdv.close()
    Rdv=open("../DATA/rdv.txt","w")
    Rdv.writelines(Patient)
    Rdv.close()