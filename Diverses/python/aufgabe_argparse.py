###############################################  Aufgabe 1 ###########################################################

"""
    Aufgabe 1 
        Erstelle mit hilfe von argparse einen kleinen Taschenrechner, dieser 
        soll über argparse zwei werte und einen operator erhalten.

        Tip:
        - Schreibe eine task()-Methode in der ein ArgumentParser erstellt wird.
        - füge dem ArgumentParser drei Argumente hinzu
            |----------------------------------------------------------------|
            | Argument Name  | type   | default   | help                     |
            |----------------|--------|-----------|--------------------------|
            | value1         | float  | 0         | gib die erste zahl an    |
            | value2         | float  | 0         | gib die zweite zahl an   |
            | operator       | str    | +         | gib die Operation an     |
            |----------------|--------|-----------|--------------------------|
        - erstelle eine Methode in der die Operation geprüft wird und an hand der Operation eine berechnung durchgeführt wird

        Gültige operationen sind z.b. +, -, *, /

        - vergiss im Skripts nicht die (if __name__ == "__main__":)

    Aufgbe 2 **Optional**:
        1. Erstelle eine Klasse Calculator (calculator.py) mit allen funktionen die
           für den Calculator benötigt werden (addiere, subtrahiere....)
        2. Erstelle eine Factory (factory.py) in der es eine statische-methode gibt,
           der als ein parameter der operator übergeben wird und den calculator mit der jeweiligen funktion zurück gibt
        3. Erstelle eine start datei (main.py) mit der die argumente aus der Console entgegengenommen werden.
        4. Teste dein Skipt ob es Funktioniert

    Optional: Passe deinen Code so an das n zahlen übergeben werden können.
         Tip: 
            1. Wenn du nicht weiter weißt nutze Google
            2. Du könntest z.b reduce und map in deinem Code nutzen
            3. Denke nicht zu kompliziert :)
            4. Falls du nicht weiterkommst ist das nicht Schlimm, dann Schaue dir die Lösung an.
"""
