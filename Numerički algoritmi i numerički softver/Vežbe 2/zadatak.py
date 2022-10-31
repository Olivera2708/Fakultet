import numpy as np

def gausovaEliminacija(matrica, rezultat):
    x, y = matrica.shape #x je broj redova, y je broj kolona
    for i in range(x):
        mnozi = matrica[i][x-i-1]
        for j in range(i+1, x): #prolazak kroz sve redove
            deli = matrica[j][x-i-1]
            if deli != 0:
                for k in range(y):
                    matrica[j][k] = matrica[j][k]*mnozi/deli
                rezultat[j] = rezultat[j]*mnozi/deli
            #oduzmi
            for r in range(y):
                matrica[j][r] -= matrica[i][r]
            rezultat[j] -= rezultat[i]

    kon = np.zeros((x, 1))
    for i in reversed(range(x)):
        kon[x-1-i][0] = rezultat[i]
        for j in range(x-1-i):
            kon[x-1-i][0] -= matrica[i][j]*kon[j][0]

        if (matrica[i][x-1-i] != 0):
            kon[x-1-i][0] /= matrica[i][x-1-i];

    print(np.round(kon, 1))


matrica = np.array([[3.0, 4.0, 1.0],
                    [1.0, 0.0, 1.0],
                    [2.0, 3.0, 2.0]])

rezultat = np.array([[3.0],
                    [3.0],
                    [1.5]])

gausovaEliminacija(matrica, rezultat)

#svi ostali zadaci su na istu foru, samo koriscenje gausa, i citanje inputa