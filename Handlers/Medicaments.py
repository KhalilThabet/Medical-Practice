def medicament():
    Nom_medicament = input("saisir le nom du medicament:\t")
    quantite = input("saisir la quantite :\t")
    Duree = input("saisir la duree de traitement:\t")
    ligne = Nom_medicament + " " + quantite + " " + Duree + "\n"
    return ligne
