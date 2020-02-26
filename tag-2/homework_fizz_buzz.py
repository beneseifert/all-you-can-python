for i in range(1, 101):
    ausgabe = ""
    if i % 3 == 0:
        ausgabe += "FIZZ"
    if i % 5 == 0:
        ausgabe += "BUZZ"
    if ausgabe == "":
        print(i)
    else:
        print(ausgabe)


