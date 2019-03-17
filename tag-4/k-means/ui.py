from tkinter import *
import config

DATEN_FARBE = config.FARBEN[0]


class UI:

    def __init__(self, weite, hoehe):
        self.haupt_komponente = Tk()
        self.weite, self.hoehe = (weite, hoehe)
        self.SKALA_PLATZ = 20
        self.TEXT_PLATZ = 10
        self.rahmen = Canvas(self.haupt_komponente, width=self.weite + self.SKALA_PLATZ,
                             height=self.hoehe + self.SKALA_PLATZ)
        self.rahmen.pack()
        self.zeichne_x_achse()
        self.zeichne_y_achse()

    def zeichne_x_achse(self):
        self.rahmen.create_line(0, self.hoehe, self.weite + self.SKALA_PLATZ, self.hoehe, fill=DATEN_FARBE)
        # Grid
        punkte = [int((x / 4) * self.weite) for x in range(4) if x != 0]
        for x in punkte:
            self.rahmen.create_text(x + self.SKALA_PLATZ, 400 + self.TEXT_PLATZ, text=str(x), fill=DATEN_FARBE)

    def zeichne_y_achse(self):
        self.rahmen.create_line(self.SKALA_PLATZ, 0, self.SKALA_PLATZ, self.hoehe + self.SKALA_PLATZ, fill=DATEN_FARBE)
        # Grid
        punkte = [int((x / 4) * self.weite) for x in range(4) if x != 0]
        for y in punkte:
            self.rahmen.create_text(self.TEXT_PLATZ, 400 - y, text=str(y), fill=DATEN_FARBE)

    def zeichne_punkt(self, punkt, farbe=DATEN_FARBE, dicke=2):
        rahmen_x = punkt.x + self.SKALA_PLATZ
        rahmen_y = self.hoehe - punkt.y
        self.rahmen.create_oval(rahmen_x, rahmen_y, rahmen_x, rahmen_y, width=dicke, outline=farbe)

    def start(self):
        self.haupt_komponente.mainloop()
