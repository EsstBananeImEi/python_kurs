"""
    Python besitzt ein Module mit dem wir mit Datums und Zeit Werten arbeiten können.
    Erstellen wir erstmal ein paar einfache programme, um mit dem Datum und der Zeit zu arbeiten, bevor wir
    tiefer in Datetime eintauchen.
"""

import datetime

datetime_object = datetime.datetime.now()
# print(datetime_object)

"""
    Wir haben das datetime module importiert.
    Eine der Klassen die im datetime Module definiert sind ist die datetime Klasse. aus der datetime Klasse nutzen wir
    hier das now() um ein datetime object mit dem heutigen tag und der jetzigen Uhrzeit zu erstellen.
"""

"""
    Das datetime module besitzt eine klasse namens dateclass die informationen vom date und time objekt enthält
"""

from datetime import datetime

# datetime(year, month, day)
datetime_object = datetime(2018, 11, 28)
print(datetime_object)

# datetime(year, month, day, hour, minute, second, microsecond)
datetime_object = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(datetime_object)

import datetime

datetime_object = datetime.date.today()
# print(datetime_object)

"""
    Diesmal nutzen wir die today()-Methode aus der date-Klasse um ein date-Objekt mit dem Lokalen Datum zu erzeugen.
    
    Die am meisten genutzten Klassen des datetime Modules sind:
        - date
        - time
        - datetime
        - timedelta
"""

from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

"""
    Ein Timedelta objekt representiert die differenz zwischen datums oder zeit angaben
"""

from datetime import datetime, date

t1 = date(year=2018, month=7, day=12)
t2 = date(year=2017, month=12, day=23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3))
print("type of t6 =", type(t6))
