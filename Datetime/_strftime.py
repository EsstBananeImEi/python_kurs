"""
    Zeitangaben werden in verschiedenen bereichen auch verschieden eingesetzt, z.b sind zeitangaben in Internationalen
    Unternehmen wahrscheinlich anders Formatiert als in dem Kleinen Kaffee um die Ecke.

    So wird die Zeit in den USA eher "mm/dd/yyyy" nach dieser art Formatiert, wohingegen die Engländer bevorzugt
    "dd/mm/yyyy" als formatierung bevorzugen. Auch geläufig ist "yyyy/mm/dd"

    Python besitzt strftime()- und strptime()-Method um mit der Formatierung zu arbeiten
"""

from datetime import datetime
from os import system
import time

# Aktuelle datum und Zeit
now = datetime.now()

time_1 = now.strftime("%H:%M:%S")
print("time:", time_1)

string_date_1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", string_date_1)

string_date_2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", string_date_2)

"""
    Die strftime()-Methode benötigt einen Format Code und macht aus einem datetime objekt einen String.
    
    Formatierungs Codes:
        https://docs.python.org/3/library/datetime.html
"""

now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%B")
day = now.strftime("%I%p")
print(year)
print(month)
print(day)
