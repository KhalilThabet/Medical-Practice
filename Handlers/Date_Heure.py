def Date_Heure():  # fonction qui permet au user d'entrer la date et l'heure si demander
    import os
    import msvcrt as m

    while 1:
        i = 0
        F = ["_", "_", "/", "_", "_", "/", "_", "_", "_", "_"]
        while i <= 9:
            if i == 2 or i == 5:
                i += 1
                continue
            X = "".join(F)
            print(X)
            Date = m.getch()
            for j in Date:
                try:
                    int(j)
                    Date = chr(j)
                except:
                    a = 0
            F[i] = Date
            i += 1
            os.system("cls")
        if int(F[3] + F[4]) in [1, 3, 5, 7, 8, 10, 12]:
            if int(F[0] + F[1]) in range(31):
                break
        elif int(F[3] + F[4]) in [4, 6, 9, 11]:
            if int(F[0] + F[1]) in range(30):
                break
        elif int(F[3] + F[4]) == 2:
            if int(F[0] + F[1]) in range(28):
                break

    while 1:
        j = 0
        A = ["_", "_", ":", "_", "_"]
        while j <= 4:
            if j == 2:
                j += 1
                continue
            Y = "".join(A)
            print(Y)
            Heure = m.getch()
            for i in Heure:
                try:
                    int(i)
                    Heure = chr(i)
                except:
                    a = 0
            A[j] = Heure
            j += 1
            os.system("cls")
        if (int(A[0] + A[1]) in range(23)) and (int(A[3] + A[4]) in range(59)):
            break
    X = "".join(F)
    Y = "".join(A)
    return X + " " + Y
