"""
    Du kannst time-objekts von der time-Klasse. bei der instanzierung des time-objekt werden.
"""

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

"""
    auf die Attribute stunde, minute, sekunde und microsekunde kann sehr einfach zugegriffen werden. 
"""

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsekunde =", a.microsecond)

"""
    wir haben dem time objekt nur h:m:s übergeben weshalb die microsekunde auf den standart werd 0 gesetzt wurde
"""
