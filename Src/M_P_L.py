def M_P_L():
    i = 0
    while i < 80:
        print("*", end="")
        i += 1
    print(" ")
    print(
        """                Programme de Gestion des Patients dans un cabinet Médical                """
    )
    i = 0
    while i < 120:  # repetion de l'etape d'affichage precedente
        print("*", end="")
        i += 1
    Dict_info = {
        0: "**q- Quitter",
        1: "*0 Créer fichier patient.txt",
        2: "*1- Ajouter un patient",
        3: "*2- Supprimer un patient",
        4: "*3- Ajouter un rendez-vous",
        5: "*4- Annuler un rendez-vous",
        6: "*5- Modifier un rendez-vous",
        7: "*6- Créer une ordonnance",
        8: "*7- Historique patient",
        9: "*8- Tracer la courbe de nombre des consulatations pour chaque mois",
        10: "*9- Tracer la courbe de nombre de consultations pour chaque annee",
    }  # dictionnaire contenant les noms des fonctions Exigees
    for o in range(1,11):
        x = Dict_info[o]
        print(" ")
        print(x,end="")
    x = Dict_info[0]
    print(" ")
    print(x,end="")
    print(" ")
    i = 0
    while i < 120:
        print("*", end="")
        i += 1
