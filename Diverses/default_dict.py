"""
    Dictionaries sind eine bequeme Möglichkeit, Daten für den späteren Abruf nach Namen (keys) zu speichern.
    Die Schlüssel müssen eindeutige, unveränderliche Objekte sein und sind typischerweise Strings.
    Die Werte in einem Dictionary können alles Mögliche sein.
    Für viele Anwendungen sind die Werte einfache Typen wie Ganzzahlen und Zeichenketten.

    Interessanter wird es, wenn es sich bei den Werten in einem Dictionary um Sammlungen (Listen, Dicts usw.) handelt.
    In diesem Fall muss der Wert (eine leere Liste oder ein leeres Dict) initialisiert werden,
    wenn ein bestimmter Schlüssel zum ersten Mal verwendet wird.
    Während dies manuell relativ einfach zu bewerkstelligen ist,
    automatisiert und vereinfacht der Typ defaultdict diese Art von Operationen.

    Ein defaultdict funktioniert genau wie ein normales dict,
    aber es wird mit einer Funktion ("default factory") initialisiert,
    die keine Argumente benötigt und den Standardwert für einen nicht vorhandenen Schlüssel liefert.

    Ein defaultdict löst niemals einen KeyError aus. Jeder Key, der nicht existiert,
    erhält den Wert, der von der default factory zurückgegeben wird.
"""

from collections import defaultdict

ice_cream = defaultdict(lambda: "Strawberry")
print(ice_cream)

ice_cream["Sarah"] = "Chunky Monkey"
ice_cream["Joel"] = "Salted Caramel Brownie"

print(ice_cream)
print(ice_cream.get("Sarah"))
print(ice_cream["Klaus"])

"""
    Im nächsten Beispiel sehen wir, dass immer wenn wir ein Dictionary benötigen und jedes element mit einem standart
    Wert begint, sollten wir ein defaultdict verwenden.
"""

city_list = [('TX', 'Austin'), ('TX', 'Houston'), ('NY', 'Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'),
             ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA', 'Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

cities_by_state_norm = {}

for state, city in city_list:
    if state in cities_by_state_norm:
        cities_by_state_norm[state].append(city)
    else:
        cities_by_state_norm[state] = [city]

for state, cities in cities_by_state_norm.items():
    print(state, " ,".join(cities))

cities_by_state = defaultdict(list)

for state, city in city_list:
    cities_by_state[state].append(city)

for state, cities in cities_by_state.items():
    print(state, " ,".join(cities))
