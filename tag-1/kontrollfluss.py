geheime_zahl = 23
geratene_zahl = 0


print("Gib eine Zahl ein")
try:
    geratene_zahl = int(input())
except ValueError:
    print("Gib bitte eine Zahl ein!")


if geratene_zahl == geheime_zahl:
    print("Richtig!")
else:
    print("Falsch!")

# Aufgabe:
# 1. Erweitere den Code so, dass auch ausgegeben wird, ob man zu hoch, oder zu niedrig geraten hat
# 2. Gib dazu noch an, ob man mehr als 10 daneben liegt