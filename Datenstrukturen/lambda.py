"""
    Eine Lambda Funktion wird in Python auch anonyme Funktion gennant wurd wir im gegensatz zu normalen methoden ohne
    das Stichword "def" definiert, sondern mit dem Wort "Lambda"

    Betrachten wir die Syntax der Lambda-Funktion:

    lambda Parameter: Anweisung

    Betrachten wir nun folgenden Code
"""


def koche_kaffee():
    print("Der Kaffee ist Fertig, Bitte Schön!")


koche_kaffee()

"""
    koche_kaffee() ist eine ganz normale Methode, die einen Ausdruck ausgibt. 
    Nun schreiben wir den Code neu und zwar in form einer Lambda-Funktion
"""

lambda_kaffee = lambda: print("Der Lambda Kaffee ist Fertig, Bitte Schön!")
lambda_kaffee()

"""
    Im obigen Code erfüllt die Funktion genau die gleichen Bedingungen wie in der Definition mit einer normalen 
    Python Funktion über das Stichwort „def“. Auf der linken Seite des Doppelpunktes haben wir den „lambda“-Ausdruck, 
    auf der Rechten steht die eigentliche Anweisung.
    
    Wie wir mit Parametern umgehen schauen wir uns jetzt an.
"""


def verdopple(zahl):
    print(f"Das Doppelte von {zahl} ist {zahl * 2}")


verdopple(5)

lambda_verdopple = lambda parameter: print(f"Das Doppelte von {parameter} ist {parameter * 2}")
lambda_verdopple(4)

"""
    Wie wir sehen wird der Parameter zwischen dem Stichwort „lambda“ und dem Doppelpunkt eingefügt.py
    
    Eine Lambdafunktion kann auch mehrere Parameter akzeptieren. 
    Erstellen wir dafür eine Funktion, die die Werte von drei zahlen addiert und ausgibt.
    
    
    In diesem Fall akzeptiert die Lambdafunktion drei Parameter. Dabei werden die Parameter mittels eines Kommas getrennt.
"""
summe = lambda zahl1, zahl2, zahl3: print(f"Summe: {zahl1 + zahl2 + zahl3}")
summe(2, 4, 6)

"""
    Wie wir sehen, helfen uns Lambda-Funktionen dabei die größe unseres Quellcodes zu reduzieren,
    wenn die Funktion lediglich eine Anweisung enthält.
    
    Die Reduzierung des Quellcodes ist in unserem beispiel nicht sonderlich relevant, aber in größeren Projekten
    macht es einen enormen unterschied.
    
    in der Lambdafunktion wird grundsätzlich die Anweisung ohne das Wort „return“ zurückgegeben.
"""

return_value = lambda: "rückgabe wert"
print(return_value())

"""
    map() und filter() sind Methoden die in Python integriert sind, die dazu genutzt werden um über Sammlungen zu 
    iterieren. Diese Funktionen können ebenfalls in Kombination mit der Lambda-Funktion genutzt werden.
"""


def increase(zahl):
    return zahl + 1


liste_1 = [1, 2, 3, 4, 5]
liste_2 = list(map(increase, liste_1))
print(liste_2)

"""
    Wie wir sehen oben sehen, iterieren wir mittels der map()-Methode über die "liste_1". Dabei wird jedes Element
    über die increase()-Methode um eins erhöht. die liste_2 bildet dann eine neue liste mit den erhöhten Werten. 
    
    Da die increase()-Methode nur eine Zeile mit einer Anweisung umfasst, 
    können wir eine Lambdafunktion daraus erstellen um keine separate Methoden zu benötigen.
"""

liste_1 = [1, 2, 3, 4, 5]
liste_2 = list(map(lambda zahl: zahl + 1, liste_1))
print(liste_2)

"""
    Der Code Funktionier genau so wie unser Code mit der increase()-Methode, nur das wir mit der Lambda funktion
    2 zeilen Code eingespart haben.
    
    Betrachten wir die map()-Funktion einmal genauer:
    Die increase()-Methode wurde durch eine Lambdafunktion ersetzt, die einen Parameter empfängt. Dieses wird dann um eins erhöht.
    
    
    Neben dem Reduzieren von Quellcode sinkt auch unser Aufwand.
    Betrachten wir nun kurz die filer()-Methode
"""
liste_1 = [1, 2, 3, 4, 5]
liste_2 = list(filter(lambda zahl: zahl > 2, liste_1))
print(liste_2)

""" Die filter()-Methode wird nur Elemente hinzufügen die größer zwei sind """

"""
    Wann sollten man nun Lambda-Funktionen verwenden?
    
        Kurz gesagt, wenn...
        
            1. die Funktion nur eine Anweisung enthalten soll
            2. die Anweisung nicht zu Komplex ist
            3. es sich um eine Temporäre und wiederkehrende Aufgabe handelt
            4. die map()- oder filter()-Methode verwendet wird.
"""
