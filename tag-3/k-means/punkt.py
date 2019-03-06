import math


def mittelpunkt(punkte):
    if len(punkte) == 0:
        return Punkt(None, None)
    x = [punkt.x for punkt in punkte]
    y = [punkt.y for punkt in punkte]
    return Punkt(sum(x) / len(x), sum(y) / len(y))


class Punkt:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "".join(["(", str(int(self.x)), ",", str(int(self.y)), ")"])

    def __hash__(self):
        return hash(str(self))

    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Punkt(self.x - other.x, self.y - other.y)

    def abstand_zu(self, anderer_punkt):
        differenz = self - anderer_punkt
        return math.sqrt(differenz.x ** 2 + differenz.y ** 2)


def aufgabe_1():
    punkt = Punkt(2, 3)
    print(punkt)
    punkt = Punkt(4)
    print(punkt)
    punkt = Punkt()
    print(punkt)
    punkt = Punkt(y=2)
    print(punkt)


def aufgabe_2():
    punkt_1 = Punkt(4, 5)
    punkt_2 = Punkt(4, 5)
    print(punkt_1 == punkt_2)


def aufgabe_3():
    punkt_1 = Punkt(2, 4)
    punkt_2 = Punkt(6, 1)
    print(punkt_1.abstand_zu(punkt_2))


if __name__ == "__main__":
    aufgabe_1()
    aufgabe_2()
    aufgabe_3()

