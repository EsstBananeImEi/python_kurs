class Bear(object):

    def __init__(self, name, alter, gewicht, groesse):
        """
        Hier haben wir __init__, einen typischen Initialisierer von Python Klasseninstanzen,
        der Argumente als typische instancemethod empfängt,
        mit dem ersten nicht optionalen Argument (self) enthält einen Verweis auf eine neu erstellte Instanz.
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

    @classmethod
    def wiki(cls):
        # der parameter ist ähnlich dem self, der unterschied ist das self auf ein objekt verweist aber
        # cls auf die Klasse verweist
        print('Die Bären (Ursidae) sind eine Säugetierfamilie aus der Ordnung der Raubtiere (Carnivora)')


# eine Klassenmethode lässt sich grundsätzlich auch wie eine Instanzmethode aufrufen
balu = Bear("balu", 22, 600, 400)
balu.wiki()

# Jetzt aber das tolle an klassenmethoden, in unserem beispiel können wir die Wiki methode nicht nur über
# balu aufrufen sondern auch über die Klasse Bear
Bear.wiki()

print(Bear.wiki)
print(Bear.fressen)
print(balu.wiki)
print(balu.fressen)

"""
    Wir sehen an der Ausgabe von Bear.fressen, dass die Methode nicht an die Klasse Bear gebunden ist, 
    sondern an eine Instanz von Bear. Alle anderen Ausgaben von print geben an, 
    dass die Methode an das zugehörige Objekt gebunden ist – also mit dem genannten Objekt innerhalb von print ausgeführt werden kann.
"""


class Bear(object):
    anzahl_bears = 0

    def __init__(self, name, alter, gewicht, groesse):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse

        Bear.anzahl_bears += 1

    @classmethod
    def counter(cls):
        # der Name cls kein festgelegtes Keyword
        # sondern lediglich ein konventioneller Bezeichner
        # und könnte auch anders benannt werden, aber um den code für alle lesbarer zu machen
        return cls.anzahl_bears


balu = Bear("balu", 22, 600, 400)
heidi = Bear("heidi", 21, 300, 200)

print(heidi.anzahl_bears)
print(Bear.anzahl_bears)
