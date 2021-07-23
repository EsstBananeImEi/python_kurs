###############################################  Aufgabe 1 ###########################################################

"""
    Aufgabe 1

        a.) Schreibe einen eigenen Dekorator, der uns unsere Funktion 2x ausführt
        b.)
            1. Schreibe eine funktion die 2 zahlen entgegen nimmt und die ausgabe 'Das Ergebnis von a + b' erzeugt
                a und b sind hier logischerweise die werte :)
            2. Schreibe einen Dekorator der uns das ergebnis von a + b zurückgibt
        c.) Nutze erweitere den Dekorator das er die rundrechenarten beherscht
"""


# a.)


def hello():
    print("Hallo World")


hello()

# b.)


# c.)


###############################################  Aufgabe 2 ###########################################################

"""
    Schreibe eine Funktion in der die Datei "meal.txt" ausgelesen werden soll, die aber nicht existiert, dies wird zu einer
    Exception führen, schreibe dafür einen Dekorator, der prüft ob die Datei vorhanden ist. Sollte die Datei
    nicht vorhanden sein, soll keine Exception geworfen werden, sondern es soll eine nachricht über das fehlen der datei
    angezeigt werden.
    
    Es gibt zwar funktionen für genau diesen fall, aber in manchen usecases braucht man etwas eigenes, hier bieten sich
    dekoratoren sehr gut an.
    
    Wenn du eine existierende Datei benötigst kannst du die Datei ../Materialien/meal.txt benutzen

    tip: Um zu prüfen ob eine Datei existiert kannst du z.b folgendes machen:
        1. import os
        2. mit os.path.isfile() könntest du prüfen es sich um eine Datei handelt, die funktion impliziert exists
           aber nur für dateien, nicht für Ornder
        3. mit os.path.exists() könntest du prüfen ob die/der Datei/Ornder existiert
"""
