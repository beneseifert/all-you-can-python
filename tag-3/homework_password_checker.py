def mindestens_n_zeichen(word, n):
    return len(word) >= n


def ist_zahl(character):
    try:
        int(character)
        return True
    except ValueError:
        return False


def enthaelt_zahl(wort):
    for buchstabe in wort:
        if ist_zahl(buchstabe):
            return True
    return False


def enthaelt_grossbuchstabe(wort):
    return not wort.islower()


def ist_gueltiges_passwort(wort):
    return mindestens_n_zeichen(wort, 10) \
           and enthaelt_zahl(wort) \
           and enthaelt_grossbuchstabe(wort)


print("Gib Passwort ein:")
wort = input()
print("Passwort ist gültig:", ist_gueltiges_passwort(wort))
