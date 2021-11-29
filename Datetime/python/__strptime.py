"""
    Mit dem strptime() erstellen wir aus einen Datums string ein datetime object.
    Die strptime()-Methode ist also das gegenteil von der strftime()-Methode

    Das Format des Datetime objects ist Year.Month.Day Hour:Minute:Second:Millisec
"""
from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

"""
    Die strptime()-Methode benötigt zwei Argumente.
        1. Einen String der Datum und/oder Zeit representiert
        2. Einen Formatcode der den aufbau von dem string representiert
        
    Formatierungs Codes:
        https://docs.python.org/3/library/datetime.html
"""

date_string = "01.06.2021 12:14/55"
date_object = datetime.strptime(date_string, "%d.%m.%Y %H:%M/%S")
print(date_object)
