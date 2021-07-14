"""
    Sammlungen werden in Python zum Speichern von Daten verwendet. 
    Es gibt verschiedene Sammlungen in Python, von denen jede ihre eigenen Merkmale hat. 
    Bei einigen können wir Elemente verändern, bei anderen wiederum nicht.
    Sozusagen hat jede Sammlung ihre eigenen Methoden.
    
    Das Set ist eine dieser Sammlungen.
    
    Ein Set ist eine ungeordnete Sammlung von Elementen eines beliebigen Datentyps, 
    es können zum Beispiel Strings und Integer gleichzeitig in einem Set enhalten sein.
    
    Sets können keine doppelten Werte enthalten, dies ist wohl der größte unterschied zu allen anderen Sammlungen.
    Sets können nicht indiziert werden, das bedeutet das keine index()-Operationen auf ihm ausgeführt werden können,
    es ist deshalb nicht möglich, die vorhandenen Werte in einem Set zu ändern, lediglich das löschen oder hinzufügen
    ist möglich.
"""

""" 
    Es gibt zwei Wege ein Set zu erstellen.
    Entwerder können wir direkt die geschwungen Klammern verwenden, oder den Konstruktor.
"""
set_1 = {1, 2, 3, 4, 5}
print(set_1)
set_1 = set({1, 2, 3, 4, 5})
print(set_1)

""" Auf gleichem weg können wir Elemente verschiedenster Typen in das einfügen 
    das Set kann aber keine anderen Sammlungen enthalten, es kann also nicht verschachtelt werden.
"""

set_1 = {1, 2, 'Hallo', 3, "Welt", 4, 5}
print(set_1)

"""
    Wie bereits erwähnt können wir ein Set nicht adressieren, also auf Elemente mittels Index zugreifen.
    Aber wir können mit hilfe einer for schleife über das Set iterieren und die elemente ausgeben.
"""

for element in set_1:
    print(element)

"""
    Wie am Anfang erwähnt handelt es sich bei einem Set um eine unsortierte Sammlung, betrachten wir das nächste Set
    mal genauer und beobachten dann die ausgabe in der Console
"""

set_2 = {1, 2, 3, 4, 5, "Hallo", "Welt"}
print(set_2)

"""
    Es gibt zwei integrierte Methoden um Elemente zu einem Set hinzuzufügen.
    Die erste ist die add()-Methode und fügt genau ein Element hinzu
"""

set_1 = {1, 2, 3, 4}
set_1.add(10)
print(set_1)

"""
    Wir können aber auch die update()-Methode verwenden. 
    Damit können wir auf einen Schlag mehrere Elemente gleichzeitig einfügen
"""

set_1 = {1, 2, 3, 4}
set_1.update({10, 2, 20, 30})
print(set_1)

"""
    Wie wir sehen können, wurden 10, 20 und 30 normal hinzugefügt. 
    Die 2 hingegen wurde nicht hinzugefügt, da diese bereits im Set enthalten war.
    
    Um Elemente aus einem Set zu entfernen, stehen uns die Methoden pop(), remove() und discard() zur verfügung.
"""

""" Die pop()-Methode löscht ein einzelnes Element, da das Set nicht sortiert ist, können wir nicht sicher sein welches """
set_1 = {1, 2, "Hallo", 4}
print(set_1)
set_1.pop()
print(set_1)

""" Mit der remove()-Methode können wir ein spezifisches Element entfernen. Wir entfenen den Wert den wir übergeben """
set_1 = {1, 2, "Hallo", 4}
print(set_1)
set_1.remove(2)
print(set_1)
# set_1.remove(2) # KeyError

""" Die discard()-Methode macht das gleiche wie die remove()-Methode, einziger unterschied, sie gibt keinen Fehler aus """
set_1 = {1, 2, "Hallo", 4}
print(set_1)
set_1.discard(2)
print(set_1)
set_1.discard(2)

"""
    Arbeiten mit mehreren Sets: Zusammenfügen und Schnittmengen bilden
    
    Wir können ein Set auch aus zwei verschiedenen Sets zusammenfügen. Dabei werden doppelte Werte nur ein einziges mal
    übernommen.
    
    Für das Zusammenfügen stehen uns zwei varianten zur verfügung:
    1. |-Operator
    2. union()-Methode
"""

set_1 = {1, 2, 3, 'a', 'b'}
set_2 = {'a', 'b', 4, 5, 6}
set_3 = set_1 | set_2
print(set_3)

"""
    Wir haben mit dem |-Operator das set_1 und set_2 zusammengefügt, wie zu erwarten wurden die doppelten Werte 'a' 
    und 'b' nur ein mal übernommen
"""
set_1 = {1, 2, 3, 'a', 'b'}
set_2 = {'a', 'b', 4, 5, 'c'}
set_3 = set_1.union(set_2)
print(set_3)

"""
    Wenn wir die Sets zusammenfügen wollen, wird jeder Wert maximal einmal in das neue Set eingefügt. 
    Wir können allerdings auch ein neues Set erschaffen, in dem nur die mehrfach vorkommenden Werte eingefügt werden.

    Dafür nutzen wir entweder den &-Operator oder die intersection()-Methode.
"""
set_1 = {1, 2, 3, 'a', 'b'}
set_2 = {'a', 'b', 4, 5, 6}
set_3 = set_1 & set_2
print(set_3)

"""
    Wir haben mit dem &-Operator dafür gesorgt das ein neues Set erstellt wird, das nur die gemeinsamkeiten aus
    dem set_1 und set_2 besitzt, also die Werte 'a' und 'b'
    
    Bei der intersection()-Methode, wird wie bereits bei der union()-Methode auch, 
    die intersection()-Methode auf dem set_1 aufgerufen und set_2 als Argument übergeben.
"""
set_1 = {1, 2, 3, 'a', 'b'}
set_2 = {'a', 'b', 4, 5, 6}
set_3 = set_1.intersection(set_2)
print(set_3)

"""
    Wir können auch versuchen, ein neues Set zu erstellen, 
    in dem nur die Werte eingefügt werden, welche nicht in allen Sets gleichzeitig enthalten sind. 
    Dafür können wir erneut die beiden Sets betrachten.
    
    Schauen wir uns set_1 an, sehen wir das 1 ,2 und 3 im Vergleich zu set_2 einzigartig sind. 
    A und b allerdings tauchen in beiden auf und fallen deshalb weg.
    
    Für die gewünschte Operation können wir entweder den "-"-Operator oder die difference()-Methode verwenden.
"""
set_1 = {1, 2, 3, 'a', 'b'}
set_2 = {'a', 'b', 4, 5, 6}
set_3 = set_1 - set_2
print(set_3)
set_3 = set_2 - set_1
print(set_3)

"""
    Es gibt eine spezielle Möglichkeit, um das Set in Python zu manipulieren. 
    Wir können damit verhindern, dass das Set nach dem Erstellen verändert werden kann.
"""

frozen_set = frozenset({1, 2, 3, 4, 5})
print(frozen_set)

"""
    Trotz des statischen Zustands können wir die Werte weiterhin auslesen.
    Wie bereits erwähnt können wir keinerlei Methoden anwenden um dieses Set zu verändern
"""
