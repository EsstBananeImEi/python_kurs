"""
    Damit Quellcode übersichtlicher und Strukturierter wird verwendet man klassen.
    Mit klassen ist es uns möglich Objekt Orientiert zu Programmieren
"""


class Bear(object):
    name = "balu"
    alter = 20
    gewicht = 450
    groesse = 250


### Ohne Konstructor haben beide die gleichen werte
balu = Bear()
print(balu.name)
print(balu.alter)

hugo = Bear()
print(hugo.name)
hugo.name = "hugo"
print(hugo.name)

balu.lieblings_fressen = "Fisch"
print(balu.lieblings_fressen)

hugo.lieblings_fressen = "Honig"
print(hugo.lieblings_fressen)
