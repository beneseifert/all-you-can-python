from collections import Counter

obst = ['Orange', 'Zitrone', 'Banane', 'Kirsche', 'Apfel', 'Feige', 'Birne', 'Ananas', 'Pflaume', 'Erdbeere', 'Orange', 'Zitrone', 'Banane', 'Kirsche', 'Apfel', 'Feige',
        'Orange', 'Zitrone', 'Banane', 'Kirsche', 'Apfel', 'Weintraube', 'Feige', 'Birne', 'Ananas', 'Pflaume', 'Erdbeere', 'Orange', 'Zitrone', 'Banane', 'Kirsche', 'Apfel', 'Feige',
        'Orange', 'Zitrone', 'Banane', 'Apfel', 'Weintraube', 'Feige', 'Birne', 'Ananas', 'Pflaume', 'Apfel', 'Erdbeere', 'Orange', 'Zitrone', 'Banane', 'Kirsche', 'Apfel', 'Feige']

vorkommen = {}

for frucht in obst:
    try:
        vorkommen[frucht] += 1
    except KeyError:
        vorkommen[frucht] = 1

print(vorkommen)
print(Counter(obst))