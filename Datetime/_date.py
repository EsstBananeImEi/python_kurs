"""
    Du kannst date-objekts von der date-Klasse. bei der instanzierung des date-objekt werden jahr, monat und tag benötigt
"""

import datetime

datum = datetime.date(2021, 7, 16)
print(type(datum))
print(datum)

"""
    wir können auch direct die date-Klasse importieren und nutzen.
"""

from datetime import date

today = date.today()
print(f"current date = {today}")

"""
    wir können aus einem Timestamp ebenfalls ein date-objekt zu erstellen. Ein Unix timestamp ist eine Nummber
    in sekunden zwischen einem bestimmten datum und dem 1 Januar 1970.
"""

timestamp = date.fromtimestamp(1326244364)
print(f"Date = {timestamp}")

"""
    Aus dem date-objekt können wir auf einfache weise, das jahr, den monat und den tag erhalten.
"""

today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
