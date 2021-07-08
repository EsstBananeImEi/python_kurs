# Über Schleifen können wir Aktion mehrmals ausführen lassen,
# bis eine festgelegte Bedingung erfüllt ist.
# So können wir z.B. in einem Shop 10 Artikel ausgeben lassen.
# Die while-Schleife läuft 10-mal und gibt dann 10 Artikel aus.

import time

# loop = True
# counter = 0
# while loop:
#     print("Das ist durchgang Nr. %s" % counter)
#     counter += 1
#     time.sleep(0.2)

max_loops = 10
counter = 1
while counter <= max_loops:
    print("Das ist durchgang Nr. %s" % counter)
    counter += 1
    time.sleep(0.2)


max_loops = 10
counter = 1
while counter <= max_loops:
    if counter % 2 == 0:
        print("Das ist durchgang Nr. %s" % counter)
    counter += 1
    time.sleep(0.2)
