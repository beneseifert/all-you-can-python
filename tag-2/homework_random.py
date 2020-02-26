import random

liste = [random.randint(0, 20) for i in range(40)]

liste_kleiner = []
liste_groesser = []

for wert in liste:
    if wert <= 10:
        liste_kleiner.append(wert)
    else:
        liste_groesser.append(wert)

print(liste)
print(liste_kleiner)
print(liste_groesser)


