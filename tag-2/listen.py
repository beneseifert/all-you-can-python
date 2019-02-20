# Du hast einen Obstkorb geschenkt bekommen
obst_korb = ['Orange', 'Zitrone', 'Banane', 'Kirsche', 'Apfel', 'Weintraube', 'Feige', 'Birne', 'Ananas', 'Pflaume', 'Erdbeere', 'Orange', 'Zitrone', 'Banane', 'Kirsche', 'Apfel', 'Feige']

# Um dir einen Überblick zu verschaffen, sortierst du erst einmal alles Obst alphabetisch
alphabetisch_rueckwaerts = obst_korb
print(alphabetisch_rueckwaerts)

# Danach entfernst du alle doppelt vorhandenen Früchte
obst_sorten = obst_korb
print(obst_sorten)

# In deinen Obstsalat, soll nur dein Lieblingsobst
lieblings_obst = set(['Apfel', 'Brombeere', 'Kirsche', 'Mango', 'Ananas', 'Pflaume'])
obst_salat = obst_sorten
print(obst_salat)

# Leider war nicht all dein Lieblingsobst vorhanden, welches musst du noch kaufen?
noch_kaufen = lieblings_obst
print(noch_kaufen)
