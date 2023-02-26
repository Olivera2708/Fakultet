import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import leastsquares

# instalirati "pip install pandas xlrd"


def g(file):
    games = pd.read_excel(file)

    return np.sum(games.iloc[:, 0] - games.iloc[:, 1])

games = pd.read_excel('games.xls')

MR = games.iloc[:, 0]

home = games.iloc[:, 4]
draw = games.iloc[:, 5]
away = games.iloc[:, 6]

order = 7
pH = leastsquares.least_squares_regression(MR, home, order)
pD = leastsquares.least_squares_regression(MR, draw, order)
pA = leastsquares.least_squares_regression(MR, away, order)
print(np.round((pH, pD, pA), 4))

pHome = np.polyval(pH, MR)
pDraw = np.polyval(pD, MR)
pAway = np.polyval(pA, MR)

# r2 = SSR/SST
r2Home = np.sum((pHome - np.mean(home)) ** 2) / np.sum((home - np.mean(home)) ** 2)
r2Draw = np.sum((pDraw - np.mean(draw)) ** 2) / np.sum((draw - np.mean(draw)) ** 2)
r2Away = np.sum((pAway - np.mean(away)) ** 2) / np.sum((away - np.mean(away)) ** 2)

print(r2Home, r2Away, r2Draw)

gHome1 = g('home.xls')
gAway1 = g('away.xls')
MR1 = gHome1 - gAway1

pHome1 = np.polyval(pH, MR1)
pDraw1 = np.polyval(pD, MR1)
pAway1 = np.polyval(pA, MR1)
QHome1 = round(100/pHome1)/100
QDraw1 = round(100/pDraw1)/100
QAway1 = round(100/pAway1)/100

print(QHome1, QDraw1, QAway1)





x = np.linspace(min(MR), max(MR), 100)

plt.subplot(1, 3, 1)
plt.scatter(MR, home, c='black')
plt.plot(x, np.polyval(pH, x), 'red')
plt.scatter(MR1, pHome1, c='red')
plt.xlabel('MR')
plt.ylabel('pHome')
plt.subplot(1, 3, 2)
plt.scatter(MR, draw, c='black')
plt.plot(x, np.polyval(pD, x), 'red')
plt.scatter(MR1, pDraw1, c='red')
plt.xlabel('MR')
plt.ylabel('pDraw')
plt.subplot(1, 3, 3)
plt.scatter(MR, away, c='black')
plt.plot(x, np.polyval(pA, x), 'red')
plt.scatter(MR1, pAway1, c='red')
plt.xlabel('MR')
plt.ylabel('pAway')

plt.show()

