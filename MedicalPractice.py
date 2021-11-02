def Cin_verif(x):#Fonction qui verifie que le Cin est composee de 8 chiffres
        a=0
        try:
                int(x)
        except:
                a=1
        if len(x)!=8 or a==1 :
                return 'False';
        else:
                return 'True' ;
def Age_verif(x):#Fonction que verfie que l'age est composee de chiffres
        try :
          int(x)
          return 'True';
        except:
          return 'False';
def String_verif(x):#Fonction que verifie que la chaine de caractere n'est pas composee d'entier
       a=0
       p=0 
        for i in x:
         try:
                int(i)
         except:
                 a+=1
                  if i == “ ” :
                             p+=1  
        if (a==len(x) ) and (p!=len(x) ) :
                return 'True';
        else:
          return 'False';
def Date_Heure():#fonction qui permet au user d'entrer la date et l'heure si demander
 import os
 import msvcrt as m
 while 1 :
  i=0
  F=['_','_','/','_','_','/','_','_','_','_']
  while (i<=9):
   if i==2 or i==5:
         i+=1
         continue;
   X="".join(F)
   print(X)
   Date=m.getch()
   for j in Date:
          try:
                   int(j)
                   Date=chr(j)
          except:
                  a=0
   F[i]=Date
   i+=1
   os.system('cls')
  if int(F[3]+F[4]) in [1,3,5,7,8,10,12]:
           if int(F[0]+F[1]) in range(31):
                   break;
  elif int(F[3]+F[4]) in [4,6,9,11]:
           if int(F[0]+F[1]) in range(30):
                   break;
  elif int(F[3]+F[4])==2:
           if int(F[0]+F[1])in range(28):
                   break;
   
 while 1 :
  j=0
  A=['_','_',':','_','_']
  while j <=4 :
     if j==2 :
         j+=1
         continue;
     Y="".join(A)
     print(Y)
     Heure=m.getch()
     for i in Heure :
             try:
                     int(i)
                     Heure=chr(i)
             except:
                     a=0
     A[j]=Heure
     j+=1
     os.system('cls')
  if (int(A[0]+A[1]) in range(23))and(int(A[3]+A[4])in range(59)) :
          break;
 X="".join(F)
 Y="".join(A)
 return X+" "+Y;
  
  #****************************************************************#
def Sexe_verif(x):#Fonction qui verifie le sexe
  if (x.upper() ==("MASCULIN")) or (x.upper() ==("FEMININ")):
          return 'True';
  else :
          return 'False';
        
def Ajouter_RDV():
        import os
        RDV=open("rdv.txt","a")
        Cin=input("Veuillez saisir le Cin Du Patient !")
        while Cin_verif(Cin)=='False':
                Cin=input("Veuillez saisir un Cin Correct! ou Appuyez sur \"Q\" pour Retourner a la page d'acceuil")
                if Cin.upper() =="\Q":
                        Main_Page()
                        break;
        c=Date_Heure()
        ligne=Cin+" "+c+"\n"
        RDV.writelines(ligne)
        RDV.close()
        M_P()

###################################################################
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
####################################################################
def Modify_RDV():
        import os
        Cin=input("Entrez le CIN ici:")
        Rdv=open("rdv.txt")
        Patient=""
        for ligne in Rdv:
            L=ligne.split(" ")
            if L[0]==Cin:
                    ligne=L[0]+" " +Date_Heure()+"\n"
            Patient+=ligne
        Rdv.close()
        Rdv=open("rdv.txt","w")
        Rdv.writelines(Patient)
        Rdv.close()
        M_P()
 ##############################################################       
def Creation_fichier_patient():
 import os
 i=0
 while i<10:
  try:
    File=open(‘patient.txt ‘ )
    Test_Cin= File.readlines()
    If Test_Cin[]  
    Dpatient={}
    ligne=""
    Dpatient["Cin"]=input("saisir Cin")
    while (Cin_verif(Dpatient["Cin"])=='False') and (a=1):
          Dpatient["Cin"]=input("saisir un Cin Correct")
         For T  in Test_Cin : 
          If T[0]!=Cin :
               a=1
          if T[0]==Cin :
              a=0
              break ;
    File.close()
   Dpatient["Nom"]=input("saisir le Nom du Patient")
   while String_verif(Dpatient["Nom"])=='False':
          Dpatient["Nom"]=input("saisir un Nom Correct")
   Dpatient["Prenom"]=input("Saisir le Prenom du Patient")
   while String_verif(Dpatient["Prenom"])=='False':
           Dpatient["Prenom"]=input("saisir un prenom Correct")
   Dpatient["Age"]=input("saisir l'age du Patient")
   while Age_verif(Dpatient["Age"])=='False':
           Dpatient["Age"]=input("Saisir un Age correct")
   Dpatient["Sexe"]=input("saisir le sexe du Patient")
   while Sexe_verif(Dpatient["Sexe"])=='False':
          Dpatient["Sexe"]=input("Choisir entre un Sexe masculin ou un Sexe Feminin")
   File=open("patient.txt","a")
   for valeur in Dpatient.values():
          ligne+=str(valeur)+" "
   ligne+="_"
   ligne+="\n"
   File.writelines(ligne)          
   File.close()
   C=input("Voulez-Vous Continuez A Rentrer Des Patients?")
   if C.upper()=="NON":
          break;
   i+=1

 Except :
   Dpatient["Cin"]=input("saisir Cin")
   while Cin_verif(Dpatient["Cin"])=='False':
           Dpatient["Cin"]=input("saisir un Cin Correct")
   Dpatient["Nom"]=input("saisir le Nom du Patient")
   while String_verif(Dpatient["Nom"])=='False':
          Dpatient["Nom"]=input("saisir un Nom Correct")
   Dpatient["Prenom"]=input("Saisir le Prenom du Patient")
   while String_verif(Dpatient["Prenom"])=='False':
           Dpatient["Prenom"]=input("saisir un prenom Correct")
   Dpatient["Age"]=input("saisir l'age du Patient")
   while Age_verif(Dpatient["Age"])=='False':
           Dpatient["Age"]=input("Saisir un Age correct")
   Dpatient["Sexe"]=input("saisir le sexe du Patient")
   while Sexe_verif(Dpatient["Sexe"])=='False':
          Dpatient["Sexe"]=input("Choisir entre un Sexe masculin ou un Sexe Feminin")
   File=open("patient.txt","a")
   for valeur in Dpatient.values():
          ligne+=str(valeur)+" "
   ligne+="_"
   ligne+="\n"
   File.writelines(ligne)          
   File.close()
   C=input("Voulez-Vous Continuez A Rentrer Des Patients?")
   if C.upper()=="NON":
          break;
   i+=1
  M_P()
###############################################################
def ajouter_Patient(): 
  try :
    File=open(‘patient.txt ‘ )
    Test_Cin= File.readlines()
    If Test_Cin[]  
    Dpatient={}
    ligne=""
    Dpatient["Cin"]=input("saisir Cin")
    while (Cin_verif(Dpatient["Cin"])=='False') and (a=1):
          Dpatient["Cin"]=input("saisir un Cin Correct")
         For T  in Test_Cin : 
          If T[0]!=Cin :
               a=1
          if T[0]==Cin :
              a=0
              break ;
    File.close()
    Dpatient["Nom"]=input("saisir le Nom du Patient")
    while String_verif(Dpatient["Nom"])=='False':
          Dpatient["Nom"]=input("saisir un Nom Correct")
    Dpatient["Prenom"]=input("Saisir le Prenom du Patient")
    while String_verif(Dpatient["Prenom"])=='False':
          Dpatient["Prenom"]=input("saisir un prenom Correct")
    Dpatient["Age"]=input("saisir l'age du Patient")
    while Age_verif(Dpatient["Age"])=='False':
          Dpatient["Age"]=input("Saisir un Age correct")
    Dpatient["Sexe"]=input("saisir le sexe du Patient")
    while Sexe_verif(Dpatient["Sexe"])=='False':
           Dpatient["Sexe"]=input("Choisir entre un Sexe masculin ou un Sexe Feminin")
    File=open("patient.txt","a")
    for valeur in Dpatient.values():
          ligne+=str(valeur)+" "
    ligne+="\n"
    File.writelines(ligne) 
    File.close()
Except :
  Print(‘fichier inexistant ‘)
    M_P()
###############################################################
def Supprimer_patient():
        cin=input("Saisir le cin du patient a supprimer :")
        file=open("patient.txt")
        Patient_a_conserver=[]
        ligne=file.readlines()
        for i in ligne:
             L=i.split(" ")
             if L[0]!=cin :
              Patient_a_conserver+=i;
        file.close()
        file=open("patient.txt","w")
        file.writelines(Patient_a_conserver)
        file.close()
        M_P()
###############################################################
def medicament():
        Nom_medicament=input("saisir le nom du medicament:")
        quantite=input("saisir la quantite :")
        Duree=input("saisir la duree de traitement:")
        ligne=Nom_medicament+" "+quantite+" "+Duree+"\n"
        return ligne;
###############################################################
def Ordonnance():
 import os
 import msvcrt as m
 Cin=input("veuillez entrer le CIN :")
 try:
  File=open("rdv.txt")
  Patient=" "
  Tp=" "
  for ligne in File :
     L=ligne.split(" ")
     if L[0]==Cin:
      try:     
        File_Patient=open("patient.txt")
        for ligne_patient in File_Patient:
             T=ligne_patient.split(" ")
             if T[0]==Cin:    
                Nom_nouveau_fichier=T[1]+" "+T[2]+".txt"
                sub_file=open(Nom_nouveau_fichier,"w")
                ligne=L[0]+" "+T[1]+" "+T[2]+" "+L[1]+" "+L[2]+"\n"
                sub_file.writelines(ligne)
                while 1:
                  Tp=medicament()
                  sub_file.write(Tp)
                  print("Voulez-vous inscrire un autre medicament? ",end="")
                  print("*1- oui",end=" ")
                  print("*2- non")
                  c=m.getch()
                  for i in c:
                    try:
                         int(i)
                         c=chr(i)
                    except:
                         a=0
                  if c=='2':
                          break;
                sub_file.close()
                sub_file=open(Nom_nouveau_fichier)
                New_fichier="Historique"+T[1]+".txt"
                print('a')
                Fichier_historique=open(New_fichier,"a")
                A="\n"+"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"+"\n"
                print('b')
                ligne2=sub_file.readlines()
                print(ligne2)
                Fichier_historique.writelines(ligne2)
                Fichier_historique.writelines(A)
                Fichier_historique.close()
                sub_file.close()
                Fichier0=open("Nbr_consultation.txt","a")
                Fichier1=open(Nom_nouveau_fichier)
                L1=Fichier1.readline()
                T=L1.split(" ")
                X=T[3][3]+T[3][4]
                Y=T[3][6]+T[3][7]+T[3][8]+T[3][9]
                Z=X+" "+Y+'\n'
                Fichier0.writelines(Z)
                Fichier1.close()
                Fichier0.close()
                sub_file.close()
        File_Patient.close()
      except:
              print("fichier patient.txt introuvable")
  File.close()        
 except:
        print("fichier rdv.txt introuvable")
 M_P()       
##############################################################
def Historique_patient():
        Nom=input("saisir le Nom du patient")
        X="Historique"+Nom+".txt"
        Fichier=open(X)
        for ligne in Fichier:
                print(ligne)
        M_P()
def Consulation_Mois():
       import numpy as np
       import matplotlib.pyplot as plt
       File=open("Nbr_consultation.txt")
       Liste=[]
       Nbr_consultation=[]
       for ligne in File:
               L=ligne.split(" ")
               Liste.append(int(L[0]))
       x =[1,2,3,4,5,6,7,8,9,10,11,12]
       j=0
       while Liste!=[]:
        for u in Liste :
         u=Liste[0]
         x1=Liste.count(u)
         for k in range(x1):
           Liste.remove(u)
         a=x[j]
         y1=x.index(u)
         x[j]=x[y1]
         x[y1]=a
         Nbr_consultation.append(int(x1))
         j+=1
       File.close() 
       for i in range(j,len(x)):
          Nbr_consultation+=[0]
       for i in x:
              a=x.index(i)
              plt.bar(i,Nbr_consultation[a],label="n"+":"+str(i),width = 0.5)
       plt.legend() 
       plt.show()
       M_P()
def Consultation_An():
       import numpy as np
       import matplotlib.pyplot as plt
       File=open("Nbr_consultation.txt")
       Liste=[]
       Nbr_consultation=[]
       for ligne in File:
               L=ligne.split(" ")
               Liste.append(int(L[1]))
       An=[]
       j=0
       while Liste!=[]:
        for u in Liste :
         u=Liste[0]
         x1=Liste.count(u)
         for k in range(x1):
           Liste.remove(u)
         An+=[u]
         Nbr_consultation.append(int(x1))
         j+=1
         print(An)
       File.close() 
       for i in range(j,len(An)):
          Nbr_consultation+=[0]
       for i in An:
              a=An.index(i)
              plt.bar(i,Nbr_consultation[a],label=str(i),width = 0.3)
       plt.legend() 
       plt.show()
       M_P()
############################################################################
def M_P_L():
 i=0
 while i<80:
         print('*',end='')
         i+=1
 print(" ")
 print("""                Programme de Gestion des Patients dans un cabinet Médical                """)
 i=0
 while i<120:# repetion de l'etape d'affichage precedente
         print('*',end='')
         i+=1
 Dict_info={0:'**0- Quitter',1:'*1 Créer fichier patient.txt',
            2:'*2- Ajouter un patient',3:'*3- Supprimer un patient',
            4:'*4- Ajouter un rendez-vous',5:'*5- Annuler un rendez-vous',
            6:'*6- Modifier un rendez-vous',7:'*7- Créer une ordonnance',
            8:'*8- Historique patient',9:'*9- Tracer la courbe de nombre des consulatations pour chaque mois',
            10:'*10- Tracer la courbe de nombre de consultations pour chaque annee'}#dictionnaire contenant les noms des fonctions Exigees
 for o in range(1,10):
  x=Dict_info[o]
  print(' ')
  L=[]
  for i in x :
         L+=i
  for i in range(len(L)):
    print(L[i],end='')
 x=Dict_info[0]
 print(' ')
 L=[]
 for i in x :
        L+=i
 for i in range(len(L)):
    print(L[i],end='')
 print(" ")
 i=0
 while i<120:
         print('*',end='')
         i+=1
#######################################################      
def M_P(): #fonction du prgramme principale
 import os
 import time
 M_P_L()#appelle a la fonction Look du programme
 dict={'1':"Creation_fichier_patient",
      '2':"ajouter_Patient",
      '3':"Supprimer_patient",
      '4':"Ajouter_RDV",
      '5':"Annuler_RDV",
     '6':"Modify_RDV",
       '7':"Ordonnance",
       '8':"Historique_patient",
       '9':"Consulation_Mois",
       '10':"Consultation_An"}#dictionnaire contenant les fonctions du programme exigees
 print("")
 c=input()
 dict[c]()
M_P()