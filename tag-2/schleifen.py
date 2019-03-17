import random

geheime_zahl = random.randint(0, 99)
geratene_zahl = 0
anzahl_versuche = 0

while geheime_zahl != geratene_zahl and anzahl_versuche < 10:
    anzahl_versuche += 1

    print("Gib eine Zahl ein")
    try:
        geratene_zahl = int(input())
    except ValueError:
        print("Gib bitte eine Zahl ein!")

    if geratene_zahl < geheime_zahl:
        print("Die gesuchte Zahl ist größer!")
    elif geratene_zahl > geheime_zahl:
        print("Die gesuchte Zahl ist kleiner!")
    else:
        print("Richtig!")
        break

if anzahl_versuche >= 10:
    print("Zu viele Versuche!")