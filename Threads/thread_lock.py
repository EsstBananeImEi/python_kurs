"""
    Ein Lock kann zwei zustände annehmen, verschlossen und offen. Wenn ein Thread versucht einen Lock zu setzten der bereits
    von einem anderen Thread gesetzt wurde, wird die Ausführung des zweiten Threads angehalten, bis die Sperre freigegeben wird

    lock.acquire ():
        Aktiviert eine Sperre, blockiert andere Threads bis True (default)

    lock.locked():
        gibt True zurück sollte eine Sperre aktive sein, anderenfalss False

    lock.release():
        offnet die Sperre
"""

# import threading
# lock = threading.Lock()
#
# list1 = []
#
# def fun1(a):
#     lock.acquire()
#     list1.append(a)
#     lock.release()
#
# for each in range(10):
#     thread1 = threading.Thread(target = fun1, args = (each, ))
#     thread1.start()
#
# print("List1 is: ", list1)

"""
    Das lock = threading.Lock() statement wird verwendet um ein lock objekt zu erstellen.
    Das Hauptproblem mit dem Lock ist das es sich nicht errinert welcher Thread die Sperre gesetzt hat.
    
    Problem 1
"""

# import threading
# import time
# lock = threading.Lock()
# import datetime
#
# t1 = datetime.datetime.now()
#
# def second(n):
#     lock.acquire()
#     print(n)
#
# def third():
#     time.sleep(5)
#     lock.release()
#     print("Thread3")
#
# th1 = threading.Thread(target = second, args = ("Thread1", ))
# th1.start()
#
# th2 = threading.Thread(target = second, args = ("Thread2", ))
# th2.start()
#
# th3 = threading.Thread(target = third)
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# t2 = datetime.datetime.now()
#
# print("Total time", t2 - t1)

"""
    Im Obrigen Code sehen wir das thread1 mit lock.acquire eine sperre setzt und thread3 diese sperre aufhebt, thread2 hat
    versucht eine Sperre zu setzten dies klappte aber nicht, da bereits eine sperre gesetzt war. deshalb konnte thread3
    vor thread2 gestartet werden
    
    Problem 2
"""

import threading

lock = threading.Lock()


def first(n):
    lock.acquire()
    a = 12 + n
    lock.release()
    print(a)


def second(n):
    lock.acquire()
    b = 12 + n
    lock.release()
    print(b)


def all():
    lock.acquire()
    first(2)
    second(3)
    lock.release()


th1 = threading.Thread(target=all)

th1.start()

"""
    Wenn der Code oben ausgeführt wird, endet dies in einem sogenannten Deadlock, dies bedeutet das alle Threads eine Sperre
    setzten wollen dies aber nicht funktioniert, da bereits eine Sperre gesetzt ist, also wird hier endlos eine schleife
    gedreht und versucht einen Thread zu Sperren, das Hauptprogramm wird in diesem Fall nie mals mehr erreicht
"""
