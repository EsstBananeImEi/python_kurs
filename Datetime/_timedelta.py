"""
    Man kann auch die differenz zwischen zwei timedelta objekten berechnen
"""

from datetime import timedelta

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
t3 = t1 - t2

print("t3 =", t3)

"""
    Negatives timedelta objekt
"""

from datetime import timedelta

t1 = timedelta(seconds=33)
t2 = timedelta(seconds=54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))

""" mit der total_seconds()-Methode bekommen wir als ausgabe die differenz in sekunden """

timedelta_objekt = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
print("total seconds =", timedelta_objekt.total_seconds())

""" 
    Wir können auch die Summe zweier Datums- und Zeitangaben mit dem Operator + ermitteln. 
    Außerdem ist es möglich ein Zeitdelta-Objekt mit int und float zahlen zu multiplizieren und zu dividieren. 
"""

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
print(t1)
t1 += timedelta(days=1, hours=4)
print(t1)
