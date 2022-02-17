def Age_verif(x):  # Fonction que verfie que l'age est composee de chiffres
    try:
        int(x)
        return "True"
    except:
        return "False"
