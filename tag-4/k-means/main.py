from ui import UI
from punkt import Punkt
import config
import data
from kmeans import KMeans

if __name__ == "__main__":
    ui = UI(config.WEITE, config.HOEHE)
    data = data.data
    punkte = []
    for x, y in data:
        punkt = Punkt(x, y)
        ui.zeichne_punkt(punkt)
        punkte.append(punkt)
    k_means = KMeans(config.ANZAHL_CLUSTER, punkte)
    k_means.starte()
    for i, mittelpunkt in enumerate(k_means.mittelpunkte):
        farbe = config.FARBEN[i]
        ui.zeichne_punkt(mittelpunkt, farbe, 5)
        punkte = k_means.punkte_fuer_mittelpunkt(mittelpunkt)
        for punkt in punkte:
            ui.zeichne_punkt(punkt, farbe)
    print("Anzahl Iterationen:", k_means.anzahl_iterationen)
    print("Mittelpunkte:", k_means.mittelpunkte)
    ui.start()
