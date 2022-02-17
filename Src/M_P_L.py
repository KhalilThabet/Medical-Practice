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
        0: "**0- Quitter",
        1: "*1 Créer fichier patient.txt",
        2: "*2- Ajouter un patient",
        3: "*3- Supprimer un patient",
        4: "*4- Ajouter un rendez-vous",
        5: "*5- Annuler un rendez-vous",
        6: "*6- Modifier un rendez-vous",
        7: "*7- Créer une ordonnance",
        8: "*8- Historique patient",
        9: "*9- Tracer la courbe de nombre des consulatations pour chaque mois",
        10: "*10- Tracer la courbe de nombre de consultations pour chaque annee",
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
