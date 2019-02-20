import io

worte = []

with io.open('./openthesaurus.txt', mode='r', encoding='utf-8') as datei:
    for zeile in datei:
        if not zeile.startswith('#'):
            eintrag = zeile.split(';')[0]
            if len(eintrag.split(' ')) == 1:
                worte.append(eintrag)

print(worte)