"""
    Listen können mit den Funktionen sort und sorted recht einfach neu sortiert werden,
    um zum Beispiel eine Liste in umgekehrter Reihenfolge zu sortieren,
    kannst du einfach die Methode sort der Liste mit dem Parameter reverse aufrufen
"""

liste = [7, 3, 78, 3, 1, 2, 8, 9]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)

""" 
    Sort hat auch einen Parameter key, mit dem du eine Funktion erstellen kannst, 
    die das Feld der Liste bestimmt, nach dem sortiert werden soll. 
    Dies macht natürlich nur Sinn mit komplexeren Datentypen, 
    weswegen wir eine Liste aus Tupeln erstellen. 
"""
liste = [(1, "Zeppelin"), (42, "Hund"), (3, "Ampel")]


def get_name(element):
    return element[1]


def get_number(element):
    return element[0]  # in dem fall Montag, Dienstag oder Mittwoch


liste.sort(key=get_name)
print(liste)
liste.sort(key=get_number)
print(liste)

"""
    Das gleiche Ergebnis könnte man allerdings auch mit der Funktion sorted erreichen, 
    da diese ebenfalls über den Parameter key verfügt:
"""
liste = [(1, "Zeppelin"), (42, "Hund"), (3, "Ampel")]
liste2 = sorted(liste, key=get_name)
print(liste2)

"""
    Du kannst, wenn du möchtest, mit der Funktion zip zwei Listen zusammenführen, 
    sodass du über beide zeitgleich in einer einzigen for-Schleife iterieren kannst.
"""
liste_0 = [1, 2, 3]
liste_1 = [4, 5, 6]
liste = zip(liste_0, liste_1)
print(liste)
for element_0, element_1 in liste:
    print(element_0, element_1)
