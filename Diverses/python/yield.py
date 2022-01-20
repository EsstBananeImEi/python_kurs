"""
    Von den meisten Funktionen wird ein Rückgabewert erwartet, 
    in Python kannst du dies mit den Schlüsselwörtern return und yield erreichen.
    
    return haben wir bereits kennnegelernt und wissen das wir mit dem return einen Wert aus einer Methode zurückgeben.
    Nun werden wir uns das yield anschauen und werden schnell den unterschied erkennen.
"""


def addiere(a, b):
    return a + b


print(addiere(2, 5))

"""
    Wenn wir nun aber Code haben nach dem Return hätten würde dieser nicht ausgeführt
"""


def addiere(a, b):
    print("Code vor dem Return ist erreichbar")
    return a + b
    print("Code nach dem Return ist nicht erreichbar")


print(addiere(2, 5))

"""
    Generatoren mit Python yield:
    
        Mit dem Schlüsselwort yield kannst du sogenannte Generatoren erstellen, die mehrere Ergebnisse einzeln zurückgeben.
"""


def potenz_generator(zahl, potenz):
    print("Code vor dem yield ist erreichbar")
    for counter in range(0, potenz + 1):
        yield zahl ** counter
    print("Code nach dem yield ist erreichbar")


for potenz in potenz_generator(2, 10):
    print(potenz)

"""
    Generatoren in Listen umwandeln mit list
        Mit der eingebauten Funktion list kannst du deine Generatoren einfach in Listen konvertieren.
"""

potenzen = list(potenz_generator(2, 10))
print(potenzen)

print(*potenz_generator(2, 10))

"""
    Das zurückgeben von Werten mit dem Schlüsselwort return ist einfach, 
    zudem ist es möglich, mehrere Werte mit dem Schlüsselwort yield nach und nach zurückzugeben, 
    um unter anderem Operationen mit größeren Listen speicherschonender zu implementieren.
"""
