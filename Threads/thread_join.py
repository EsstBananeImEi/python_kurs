"""
    Die Join()-Methode
        Führen wir den Code unten einmal aus und reden über das ergebnis
"""
#
# import threading
#
# import time
#
# list1 = []
#
# def fun1(a):
#
#     time.sleep(1)
#
#     list1.append(a)
#
# thread1 = threading.Thread(target = fun1, args = (1, ))
#
# thread1.start()
#
# thread2 = threading.Thread(target = fun1, args = (6, ))
#
# thread2.start()
#
# print("List1 is: ", list1)

"""
    Das Resultat ist eine leere Liste, obwohl wir eine 1 und eine 6 hinzugefügt haben. Das Problem liegt darin das der 
    MainThread pausieren muss solange bis alle anderen Thread fertig sind, um das zu erreichen nutzen wir die join()-Methode
"""

#
# import threading
# import time
#
# list1 = []
#
# def fun1(a):
#     time.sleep(1)
#     list1.append(a)
#
# thread1 = threading.Thread(target = fun1, args = (1, ))
# thread1.start()
#
# thread2 = threading.Thread(target = fun1, args = (6, ))
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("List1 is: ", list1)

"""
    Nun da wir den MainThread Blocken und auf die Laufenden Threads warten, bekommen wir auch die 1 und die 6 in die Liste

    Lasst und noch ein weiteres join() scenario betrachten
"""
#
# import threading
# import time
# import datetime
#
# t1 = datetime.datetime.now()
# list1 = []
#
# def fun1(a):
#     time.sleep(1)
#     list1.append(a)
#
# list_thread = []
#
# for number in range(10):
#     thread1 = threading.Thread(target = fun1, args = (number, ))
#     list_thread.append(thread1)
#
#     thread1.start()
#
# for thread in list_thread:
#     thread.join()
#
# print("List1 is: ", list1)
# t2 = datetime.datetime.now()
# print("Time taken", t2 - t1)

"""
    der Code oben nutzt eine for schleife um 10 threads zu erstellen und jeden Thread einer liste von Threads hinzuzufügen.
    Nach der Erstellung aller Threads wird mittels for schleife auf jeden Thread in der Thread liste gewartet bis dieser
    fertig ist

    das ganze ging mit etwa 1 sekunde auch ziemlich flott, da wir den join erst nach der erstellung aller Thread gemacht haben,
    dies sieht anders aus wenn wir den join direkt nach der erstellung machen würden.
"""

#
# import threading
# import datetime
#
# t1 = datetime.datetime.now()
# list1 = []
#
# def fun1(a):
#     time.sleep(1)
#     list1.append(a)
#
# list_thread = []
#
# for number in range(10):
#     thread1 = threading.Thread(target = fun1, args = (number, ))
#     list_thread.append(thread1)
#
#     thread1.start()
#     thread1.join()
#
# print("List1 is: ", list1)
# t2 = datetime.datetime.now()
# print("Time taken", t2 - t1)

"""
    im obrigen Code kann man gut erkennen das hier kein Paraleles arbeiten stattfindet und wir ca. 10 sekunden benötigen,
    da auf jeden einzelnen Thread gewartet wird. 

    Es kommt also immer drauf an wann wir die jon()-Methode aufrufen.


"""
