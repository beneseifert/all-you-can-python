# Arithmetische Operatoren
print("1 + 3 =", 1 + 3)
print("5 - 1 =", 5 - 1)
print("10 * 3 =", 10 * 3)
print("2 ** 3 =", 2 ** 3)
print("20 / 5 =", 20 / 5)
print("20 / 6 =", 20 / 6)
print("20 % 6 =", 20 % 6)

# Aufgabe 1
print(3 * 7 - 5 % 3 - 2 ** 5, "= -13")
print(3 * (7 - 5) % (3 - 2) ** 5, "= 0") # Setze Klammern, so dass das Ergebnis 0 ist

# Boole'sche Operatoren
print("True or False =", True or False)
print("True and False =", True and False)
print("not True =", not True)


# Aufgabe 2
def soll_ich_regenschirm_mitnehmen(regen, wolken, wind):
    return (regen or wolken) and not wind # Setze die Operatoren sinnvoll



print("regen = True, wolken = True, wind = True, => False : ", soll_ich_regenschirm_mitnehmen(True, True, True))
print("regen = True, wolken = True, wind = False, => True : ", soll_ich_regenschirm_mitnehmen(True, True, False))
print("regen = True, wolken = False, wind = True, => False : ", soll_ich_regenschirm_mitnehmen(True, False, True))
print("regen = True, wolken = False, wind = False, => True : ", soll_ich_regenschirm_mitnehmen(True, False, False))
print("regen = False, wolken = True, wind = True, => False : ", soll_ich_regenschirm_mitnehmen(False, True, True))
print("regen = False, wolken = True, wind = False, => True : ", soll_ich_regenschirm_mitnehmen(False, True, False))
print("regen = False, wolken = False, wind = True, => False : ", soll_ich_regenschirm_mitnehmen(False, False, True))
print("regen = False, wolken = False, wind = False, => False : ", soll_ich_regenschirm_mitnehmen(False, False, False))