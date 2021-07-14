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

"""####################     collections.deque Modul      ###################### 
    
    Die zweite Möglichkeit ist mehr oder weniger sehr ähnlich zur ersten Methode. 
    Allerdings wird statt der Python List die deque Klasse aus dem Python Collection-Modul verwendet. 
    Der größte Unterschied ist dabei die Zeitkomplexität. 
    
    Die Zeitkomplexität der deque-Klasse in der O-Notation ist O(1). Die Komplexität der List wiederrum ist O(n). 
    das bedeutet, dass die deque-Klasse Operation innerhalb der Datenstruktur deutlich schneller ausführt als die List. 
    Dies ist besonders bei großen Datenstrukturen wichtig.
"""

""" Starten wir zunächst mit dem Erstellen der Queue: """

from collections import deque

queue = deque()

""" 
    Als erstes müssen wir die deque-Klasse aus dem Collection-Modul importieren. 
    Dann können wir diese nutzen, um unsere Queue zu initialisieren. 
   
    Als nächstes implementieren wir die Enqueue-Operation, indem wir die append()-Funktion der Klasse nutzen.
"""


def enqueue(item):
    queue.append(item)


enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
enqueue(6)
enqueue(7)

print(queue)

""" 
    um nun das erste Element entfernen zu können benutzen wir die popleft()-Methode.
"""


def dequeue():
    if len(queue) > 0:
        queue.popleft()


dequeue()
dequeue()

print(queue)

"""
    Nun können wir noch die front()- und rear()-Methode implementieren um das erste und letzte Element ausgeben zu können
"""


def front():
    if len(queue) > 0:
        return queue[0]


def rear():
    last_element = len(queue) - 1
    if last_element >= 0:
        return queue[last_element]


print(front())
print(rear())

"""
    Nun haben wir zwei Methoden, eine front()-Methode für die Front-Operation und eine rear()-Methode für die Rear-Operation
    
    - In der front()-Methode wird das erste Element der Queue zurückgegeben.
    - In der rear()-Methode wiederum wird mit hilfe der len()-Methode der index des letzten elements ermittelt und ausgegeben
    
    Testen wir das ganze noch einmal und verwenden nochmals die dequeue()-Methode, dann muss das die front()-Methode 4
    zurückgeben und die rear()-Methode immer noch die 7 
"""
print("###### Letzter Test der Queue #######")
dequeue()
print("expected value: 4 -> current value " + str(front()))
print("expected value: 7 -> current value " + str(rear()))
