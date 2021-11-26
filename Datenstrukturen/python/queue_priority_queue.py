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
    
    Eine Queue mit Prioritäten ist eine höhere Variante der normalen Queue. 
    Sie bildet also eine Art Erweiterung der normalen Funktion der Queue. 
    Die Elemente werden dabei beim Entfernen auf Basis ihrer Priorität bearbeitet.
     
    
    Jedes Element, das in eine Queue mit Prioritäten hinzugefügt wird, erhält eine Nummer. 
    Das Element mit der niedrigsten Nummer, also bildlich mit der niedrigsten Priorität, 
    wird in der Queue als erstes gelöscht. Grundsätzlich wird dabei also das bekannte FIFO-Prinzip übergangen
"""

""" Eine Queue mit Priorität kann mittels der PriorityQueue-Klasse aus dem queue-Modul realisiert werden."""
from queue import PriorityQueue

queue = PriorityQueue(maxsize=7)

""" 
    Um Elemente hinzuzufügen, nutzen wir wie zuvor die put()-Funktion.
    Allerdings müssen wir bei der PriorityQueue-Klasse einen Unterschied zur Queue-Klasse beachten. 
    Die Elemente müssen mit einer Prioritätsnummer übergeben werden.

    Die put()-Funktion akzeptiert zwei Parameter. Zum einen die Priorität und zum zweiten das hinzuzufügende Element.
"""


def enqueue(priority, item):
    queue.put(priority, item)


enqueue(5, "a")
enqueue(7, "b")
enqueue(6, "c")
enqueue(3, "d")
enqueue(4, "e")
enqueue(1, "f")
enqueue(2, "g")
print(f"Queue ist leer: {queue.empty()}")
print(f"Queue ist voll: {queue.full()}")
print(f"Elemente in Queue: {queue.qsize()}")

"""
    Für die Dequeue-Operation umzusetzen wir wie bei der queue.Queue die get()-Methode des Moduls.
    Die get()-Methode entfernt das erste Element und gibt es zurück.
    
    Betrachten wir die Dequeue-Operation. Das erste Element in der Queue ist das „a“ mit der Priorität 5. 
    In einer normalen Queue sollte das „a“ als erstes entfernt werden, 
    da nach dem FIFO-Prinzip das erste Element als erstes gelöscht werden muss. 
    Dies gilt so allerdings nicht zwingend für die Queue mit individueller Priorität. 
    Im Folgenden Beispiel können wir das schnell erkennen.
"""


def dequeue():
    print("dequeue")
    return queue.get()


print(dequeue())
print(dequeue())

""" 
    Die get()-Funktion gibt die Priorität des gelöschten Elements zurück. 
    Als erstes gibt die get()-Methode die Priorität 1 zurück, dies bedeutet das "f" gelöscht wurde, 
    da "f" die Priorität 1 hatte. 
    Im zweiten Aufruf wird 2 ausgegeben, das bedeutet das nun das "g" gelöscht wurde, da es die Priorität 2 hatte.

    So funktioniert die Queue mit Priorität :-).
"""

print(f"Elemente in Queue: {queue.qsize()}")

print("###### Letzter Test der Queue #######")
print(dequeue())
first_element = dequeue()

print("expected Priority: 4 -> current Priority " + str(first_element))
