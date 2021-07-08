# Sowohl die for- wie auch die while-Schleife gibt es die
# Möglichkeit diese frühzeitig abzubrechen, auch wenn das Schleifenende
# eigentlich noch nicht erreicht wurde. Dies läuft über den Python-Befehl break

for durchgang in range(10):
    if durchgang == 7:
        print("Schleifenabbruch wird erzwungen")
        break
    print(durchgang)

print("Nach der Schleife")

# Nicht ganz so radikal wie break funktioniert die Anweisung continue in Python.
# Es wird nur der Schleifendurchgang abgebrochen, aber wieder den nächsten
# Schleifendurchgang mit neuem Wert durchlaufen.

for durchgang in range(10):
    if durchgang % 2 == 1:
        continue
    print(durchgang)

print("Nach der Schleife")