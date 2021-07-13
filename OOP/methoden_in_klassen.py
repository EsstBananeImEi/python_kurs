"""
    Wir können in Klassen Methoden definieren und Methoden überschreiben
"""


class Bear(object):

    def __init__(self, name, alter, gewicht, groesse):
        """
        Der Parameter „self“ verweist innerhalb einer Klasse auf das Objekt / Instanz.
        Er ermöglicht es auf die Eigenschaften des Objekts zuzugreifen
        """

        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse

    def __str__(self):
        return f"{self.name} ist {self.alter} Jahre alt, ist {self.groesse}cm groß und wiegt {self.gewicht}kg"

    def __eq__(self, other):
        if other.alter == self.alter:
            return True
        else:
            return False

    def schlafen(self, dauer):
        print(f"{self.name} schläft jetzt {dauer} minuten")

    def fressen(self):
        print(f"{self.name} frisst")


balu = Bear("balu", 12, 450, 260)
bruno = Bear("bruno", 12, 400, 230)

balu.schlafen(10)
bruno.schlafen(5)

print(balu)
print(bruno)

if not bruno == balu:
    print("nicht gleich")
else:
    print("sie sind gleich alt")
