from punkt import Punkt, mittelpunkt
import config
import random


class KMeans:

    def __init__(self, anzahl_cluster, punkte):
        self.anzahl_cluster = anzahl_cluster
        self.punkte = punkte
        self.anzahl_iterationen = 1
        mittelpunkte = []
        for i in range(self.anzahl_cluster):
            mittelpunkte.append(self.generiere_zufaelligen_mittelwert())
        self.initialisiere_attribute(mittelpunkte)

    def initialisiere_attribute(self, mittelpunkte):
        self.punkte_zu_mittelpunkt = {}
        self.mittelpunkte = mittelpunkte
        for mittelpunkt in mittelpunkte:
            self.punkte_zu_mittelpunkt[mittelpunkt] = []

    def generiere_zufaelligen_mittelwert(self):
        return Punkt(random.randint(0, config.WEITE), random.randint(0, config.HOEHE))

    def starte(self):
        self.weise_punkte_zu_mittelwert()
        neue_mittelpunkte = self.neue_mittelpunkte()
        if not self.mittelpunkte_sind_gleich(neue_mittelpunkte):
            self.anzahl_iterationen += 1
            self.initialisiere_attribute(neue_mittelpunkte)
            self.starte()

    def weise_punkte_zu_mittelwert(self):
        for punkt in self.punkte:
            abstaende = [(mittelpunkt, punkt.abstand_zu(mittelpunkt)) for mittelpunkt in self.mittelpunkte]
            min_abstand = min(abstaende, key=lambda abstand_paar: abstand_paar[1])
            mittelpunkt, _abstand = min_abstand
            self.punkte_zu_mittelpunkt[mittelpunkt].append(punkt)

    def neue_mittelpunkte(self):
        neue_mittelpunkte = []
        neue_punkte_zu_mittelpunkt = {}
        for alter_mittelpunkt in self.mittelpunkte:
            punkte = self.punkte_fuer_mittelpunkt(alter_mittelpunkt)
            neuer_mittelpunkt = mittelpunkt(punkte)
            neue_mittelpunkte.append(neuer_mittelpunkt)
            neue_punkte_zu_mittelpunkt[neuer_mittelpunkt] = punkte
        self.punkte_zu_mittelpunkt = neue_punkte_zu_mittelpunkt
        return neue_mittelpunkte

    def mittelpunkte_sind_gleich(self, neue_mittelpunkte):
        anzahl_gleiche_mittelpunkte = 0
        for mittelpunkt in self.mittelpunkte:
            if mittelpunkt in neue_mittelpunkte:
                anzahl_gleiche_mittelpunkte += 1
        return anzahl_gleiche_mittelpunkte == len(self.mittelpunkte)

    def punkte_fuer_mittelpunkt(self, mittelpunkt):
        return self.punkte_zu_mittelpunkt[mittelpunkt]
