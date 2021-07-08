# Die pop funktion ermöglicht uns das entfernen von elementen aus einer liste

liste_mit_personen = ["Max", "Peter", "Marie", "Gabi"]

a = liste_mit_personen.pop()
print(liste_mit_personen)
print(a)

liste_mit_personen.pop(1)
print(liste_mit_personen)
liste_mit_personen.append(a)
print(liste_mit_personen)
