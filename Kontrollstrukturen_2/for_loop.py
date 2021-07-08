# Es gibt weitere Arten von Schleifen neben while in Python.
# Je nach Anwendung spart die geschickte Wahl der Schleife Programmierarbeit.
# Und um das geht es ja beim Programmieren – eine zeitsparende Lösung mit dem geringstmöglichen Aufwand.


vornamen = ['Axel', 'Elke', 'Martin']
for einzelwert in vornamen:
    print(einzelwert)
print("nach der for-Schleife")


namen_dict = {"key0": "value0",
              "key1": "value1",
              "key2": "value2",
              "key3": "value3",
              }

for item in namen_dict:
    print(item)

for key, value in namen_dict.items():
    print(key, value)

vornamen = ['Axel', 'Elke', 'Martin']
for nr, einzelwert in enumerate(vornamen):
    print(nr, einzelwert)

for e in range(5):
    print(e)