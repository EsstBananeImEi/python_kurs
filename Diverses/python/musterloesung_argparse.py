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
            | operator       | str    | add       | gib die Operation an     |
            |----------------|--------|-----------|--------------------------|
        - erstelle eine Methode in der die Operation geprüft wird und an hand der Operation eine berechnung durchgeführt wird

        Gültige operationen sind z.b. add, sub, mul, div

        starte das skript so das nur die task-Methode gestartet wird (if __name__ == "__main__":)
"""

import argparse
from functools import reduce
import sys


def task():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--value1', type=float, default=0,
    #                     help='gib die erste zahl an')
    # parser.add_argument('--value2', type=float, default=0,
    #                     help='gib die zweite zahl an ')
    parser.add_argument(
        "-v",
        "--values",
        nargs="+",
        default=0,
        help="gib alle zahlen an ohne komma getrennt e.g. 1 2 3 4 5",
    )
    parser.add_argument(
        "-o", "--operator", type=str, default="+", help='gib den operator an e.g. "*"'
    )
    arguments = parser.parse_args()
    print(calc(arguments))


def calc(arguments):
    if arguments.operator == "+":
        return reduce(lambda a, b: a + b, map(float, arguments.values))
    if arguments.operator == "-":
        return reduce(lambda a, b: a - b, map(float, arguments.values))
    if arguments.operator == "*":
        return reduce(lambda a, b: a * b, map(float, arguments.values))
    if arguments.operator == "/":
        return reduce(lambda a, b: a / b, map(float, arguments.values))


if __name__ == "__main__":
    task()
