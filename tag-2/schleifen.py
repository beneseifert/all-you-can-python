import random

geheime_zahl = random.randint(0, 99)
geratene_zahl = 0

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

# Aufgabe:
# Erweitere den Code von Tag 1 so, dass das Spiel nicht ständig neu geladen werden muss
# Benutze das Keyword break um das Spiel zu beenden, falls:
# - die Zahl gefunden wurde
# - oder der Benutzer über 10-mal falsch geraten hat