""" Schauen wir uns nun die is_alive()-Methode an. """

# import threading
#
# import time
#
# def fun1(a):
#     time.sleep(3)# complex calculation takes 3 seconds
#
# thread1 = threading.Thread(target = fun1, args = (1, ))
# thread1.start()
# thread1.join()
#
# print(thread1.is_alive())

""" 
    Wie wir sehen ist kein Thread aktive, dies liegt wieder am join, da wir erst zum print kommen wenn der thread zu ist.
    Machen wir aber eine Kleine änderung am Code und war...
        ändern wir thread1.join() zu thread1.join(2)
    damit sagen wir dem Programm das der MainThread nur 2 sekunden geblocket werden soll.
"""

# import threading
#
# import time
#
# def fun1(a):
#     time.sleep(3)# complex calculation takes 3 seconds
#
# thread1 = threading.Thread(target = fun1, args = (1, ))
# thread1.start()
# thread1.join(2)
#
# print(thread1.is_alive())

"""
    Nun erhalten wir ein True, weil der MainThread nur 2 sekunden lang geblockt wird, der thread1 aber 3 sekunden für 
    seine Arbeit benötigt

    Schauen wir uns zum Schluss noch folgendes an, da es mit dem is_alive() gut zusammen passt und das is_alive() nochmal
    besser zur geltung bringt.

    threading.Timer()

        diese Methode wird verwendet um eine zeit zu setzen, das bedeutet das nach einem festgelegten intervall (in sek)
        eine bestimmte funktion mit args und kwargs ausgeführt wird.
"""

import threading
import time

c = []


def fun1(a, b):
    global c
    c.append(a + b)


thread1 = threading.Timer(5, fun1, args=(12, 10))

thread1.start()
while thread1.is_alive():
    print("warte noch")
    time.sleep(1)
print(c)

"""
    wir sehen hier das der thread erstellt wird, aber erst nach 5 sekunden die Funktion aufruft. somit können wir über die 
    is_alive()-Methode abfragen ob der Thread fertig ist oder nicht.
"""
