"""
    Die Python Queue:

    Die Queue ist eine lineare Datenstruktur. In ihr werden die Daten nach dem FIFO-Prinzip (First In First Out) verwaltet
    Wie das Prinzip schon ausdrückt wird das erste Element das rein geht auch wieder als erstes heraus genommen.

    Stellen wir uns als Beispiel eine Schlange von Personen an einer Kasse vor. Die erste Person in der Schlange
    wird auch als erstes bezahlen, danach verlässt die Person die Schlange wieder. Dann kommt die zweite Person zum
    bezahlen und verlässt dann die schlange wieder, dies passiert solange bis die Schlange leer ist.
    Und genau so funktioniert eine Queue.

    Bevor wir eine Queue implementieren, müssen wir die grundlegenden Bedingungen und Operationen verstehen.

    1. Enqueue: Die enqueue-Funktion fügt ein Element am Ende der Queue ein
    2. Dequeue: Die Funktion löscht ein Element aus der Queue. Das gelöschte Element ist dabei immer das erste in der Queue
    3. Overflow: Die Overflow-Bedingung zeigt an, ob die Queue Elemente hält. Sie wird in der enqueue-Funktion verwendet.
    4. Underflow: Die Underflow-Bedingung zeigt an, ob die Queue leer ist. Sie wird in der dequeue-Funktion verwendet.
    5. Front: Die Front-Funktion gibt das erste Element in der Queue zurück.
    6. Rear: Die Rear-Funktion gibt das letzte Element in der Queue zurück.


    Es gibt in Python 3 Wege eine Queue zu erstellen, diese werden wir jetzt besprechen.
"""

"""####################      Python queue.Queue Modul      ###################### 
    
    Das queue-Modul ist ein in Python integriertes Modul, das speziell für das erstellen einer Queue in gedacht ist.
    Es bietet und mehrere Methoden, die auf verschiedenste weise nützlich sind.
    
    Diese Herangehensweise ist die gradlinigste Möglichkeit die Queue in Python zu implementieren und auch die am
    häufigsten benutzte.
     
"""

""" Starten wir erneut mit dem Erstellen einer leeren Queue mit dem queue-Modul. """
from queue import Queue

queue = Queue(maxsize=7)

""" 
    Ein Vorteil beim Verwenden dieser Methode ist die Begrenzung der maximalen Größe der Queue. 
    Dabei übergeben wir der Funktion die maximale Größe, in unserem Fall sieben.

    Um Elemente der Queue hinzuzufügen, nutzen wir die put()-Methode
    Die put()-Methode arbeitet gleich zu den vorherigen Ansätzen mit der append()-Methode.
"""


def enqueue(item):
    queue.put(item)


enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
enqueue(6)
enqueue(7)

print(f"Queue ist leer: {queue.empty()}")
print(f"Queue ist voll: {queue.full()}")
print(f"Elemente in Queue: {queue.qsize()}")

"""
    Um die Dequeue-Operation umzusetzen, nutzen wir die get()-Methode des Moduls.
    Die get()-Methode entfernt das erste Element und gibt es zurück.
"""


def dequeue():
    print("dequeue")
    return queue.get()


dequeue()
dequeue()

print(f"Elemente in Queue: {queue.qsize()}")

print("###### Letzter Test der Queue #######")
dequeue()
first_element = dequeue()
print("expected value: 4 -> current value " + str(first_element))
