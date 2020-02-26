zahlen = list(range(2, 101))
primzahlen = []
# [5,7,9,...] [5,7,11,13,...]
while len(zahlen) > 0:
    primzahl = zahlen[0]
    del zahlen[0]
    primzahlen.append(primzahl)
    neue_zahlen = []
    for i in zahlen:
        if i % primzahl != 0:
            neue_zahlen.append(i)
    zahlen = neue_zahlen

print(primzahlen)