"""
    Ein Thread ist ein separater Ausführungsfluss. Dies bedeutet, dass in Ihrem Programm zwei Dinge gleichzeitig passieren.
    Bei den meisten Python 3-Implementierungen werden die verschiedenen Threads jedoch nicht gleichzeitig ausgeführt.

    Es ist verlockend, sich das Threading so vorzustellen,
    dass zwei (oder mehr) verschiedene Prozessoren in Ihrem Programm ausgeführt werden,
    von denen jeder gleichzeitig eine unabhängige Aufgabe ausführt. Das ist fast richtig.
    Die Threads werden möglicherweise auf verschiedenen Prozessoren ausgeführt,
    sie werden jedoch jeweils nur einzeln ausgeführt.
"""
# import threading
#
# class mythread(threading.Thread):
#
#     def __init__(self, i):
#         threading.Thread.__init__(self)
#         self.h = i
#
#     def run(self):
#         print("Value send" + str(self.h))
#
# for e in range(10):
#     thread1 = mythread(e)
#
#     thread1.start()

"""
    jetzt wollen wir eine funktion in einem Neuen Thread starten
"""

# import threading
#
# def fun1(a, b):
#     c = a + b
#     print(c)
#
# thread1 = threading.Thread(target = fun1, args = (12, 10))
#
# thread1.start()

"""
    Schauen wir uns ein paar wichtige Methoden für das Threading an

    Als erstes Schauen wir uns folgende an
        threading.activeCount() = Rückgabe ist ein Integer der für die anzahl Activen Threads steht
        threading.enumerate() = Rückgabe ist eine Liste mit den Aktiven Threads
"""
#
# import threading
#
# def fun1(a, b):
#     time.sleep(1)
#     c = a + b
#
#     print(c)
#
# thread1 = threading.Thread(target = fun1, args = (12, 10))
#
# thread1.start()
#
# thread2 = threading.Thread(target = fun1, args = (10, 17))
#
# thread2.start()
#
# print("Anzahl der Laufenden Threads", threading.activeCount())
#
# print("Liste der Threads: ", threading.enumerate())

"""
    Hier sieht man jetzt sehr gut das wir 2 neue Threads starten, wir aber 3 Aktive Threads haben. Dies liegt daran
    da das Hauptprogramm auch einen Thread benötigt und unter dem MainThread läuft
"""
