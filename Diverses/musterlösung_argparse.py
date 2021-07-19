###############################################  Aufgabe 1 ###########################################################

"""
    Aufgabe 1
        Die Methoden-Namen und alle Informationen zu den Argumenten dienen als beispiel du kannst auch gerne eigene
        Namen verwenden, solange das ergebnis das richtig ist :-)

        - Schreibe eine task()-Methode in der ein ArgumentParser erstellt wird.
        - füge dem ArgumentParser drei Argumente hinzu
            |----------------------------------------------------------------|
            | Argument Name  | type   | default   | help                     |
            |----------------|--------|-----------|--------------------------|
            | value1         | int    | 0         | gib die erste zahl an    |
            | value2         | int    | 0         | gib die zweite zahl an   |
            | operation      | str    | add       | gib die Operation an     |
            |----------------|--------|-----------|--------------------------|
        - erstelle eine Methode in der die Operation geprüft wird und an hand der Operation eine berechnung durchgeführt wird

        Gültige operationen sind z.b. add, sub, mul, div

        starte das skript so das nur die task-Methode gestartet wird (if __name__ == "__main__":)
"""

import argparse
import sys


def task():
    parser = argparse.ArgumentParser()
    parser.add_argument('--value1', type=int, default=0, help='gib die erste zahl an')
    parser.add_argument('--value2', type=int, default=0, help='gib die zweite zahl an ')
    parser.add_argument('--operation', type=str, default="add", help='gib die Operation an')
    arguments = parser.parse_args()
    sys.stdout.write(str(calc(arguments)))


def calc(arguments):
    if arguments.operation == "add":
        return arguments.value1 + arguments.value2
    if arguments.operation == "sub":
        return arguments.value1 - arguments.value2
    if arguments.operation == "mul":
        return arguments.value1 * arguments.value2
    if arguments.operation == "div":
        return arguments.value1 / arguments.value2


if __name__ == '__main__':
    task()
