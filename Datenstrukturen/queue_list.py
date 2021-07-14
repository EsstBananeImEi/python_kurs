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

"""####################      Die Python Liste      ###################### 
    
    Die Liste in Python haben wir bereits kennengelernt. Die Queue mithilfe einer Liste zu Implementieren, ist einer 
    der einfachsten wege.
"""

queue = []

""" 
    um ein Element hinzuzufügen nutzen wir die append()-Methode, 
    dabei nutzen wir eine Methode der wir ein element übergeben
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
    um Elemente nur wieder zu entfernen können wir die pop()-Methode nutzen.
    in der deqeue müssen wir der pop()-Methode eine 0 übergeben um das erste element aus der Liste bzw. der
    Queue zu löschen
"""


def dequeue():
    if len(queue) > 0:
        queue.pop(0)


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
