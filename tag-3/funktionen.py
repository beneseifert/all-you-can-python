import io
import random


worte_die_ich_mag = []
worte_die_ich_nicht_mag = []


def lade_worte():
    worte = []
    with io.open('../tag-2/openthesaurus.txt', mode='r', encoding='utf-8') as datei:
        for zeile in datei:
            if not zeile.startswith('#'):
                eintrag = zeile.split(';')[0]
                if len(eintrag.split(' ')) == 1:
                    worte.append(eintrag)
    return worte


def filtere_worte(worte):
    for wort in worte:
        if len(set(wort.lower()).intersection(set([chr(112), chr(121), chr(116), chr(104), chr(111), chr(110)]))) > 0:
            worte_die_ich_mag.append(wort)
        else:
            worte_die_ich_nicht_mag.append(wort)


def starte_spiel():
    sag_was_ich_mag()
    while(True):
        rate_wort = zufalls_wort()
        print("Mag ich", rate_wort, "?")
        eingabe = input().lower()
        if eingabe == "":
            break
        if (eingabe == "ja" and rate_wort in worte_die_ich_mag) \
                or (eingabe == "nein" and rate_wort in worte_die_ich_nicht_mag):
            print("Genau!")
        else:
            sag_was_ich_mag()


def sag_was_ich_mag():
    print("Ich mag", zufalls_wort_das_ich_mag(), ", aber ich mag nicht", zufalls_wort_das_ich_nicht_mag())


def zufalls_wort():
    if random.random() < 0.5:
        return zufalls_wort_das_ich_mag()
    else:
        return zufalls_wort_das_ich_nicht_mag()


def zufalls_wort_das_ich_mag():
    anzahl_worte_die_ich_mag = len(worte_die_ich_mag)
    zufall_index_mag = random.randint(0, anzahl_worte_die_ich_mag - 2)
    return worte_die_ich_mag[zufall_index_mag]


def zufalls_wort_das_ich_nicht_mag():
    anzahl_worte_die_ich_nicht_mag = len(worte_die_ich_nicht_mag)
    zufall_index_mag_nicht = random.randint(0, anzahl_worte_die_ich_nicht_mag - 2)
    return worte_die_ich_nicht_mag[zufall_index_mag_nicht]


def init():
    worte = lade_worte()
    filtere_worte(worte)
    starte_spiel()


if __name__ == '__main__':
    init()