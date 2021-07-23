"""
    Wenn man in der Software entwicklung von vererbung spricht, meint man genau das was es bedeutet,
    denn wenn wir einer klasse die mutterklasse zur verfügung stellen werden deren funktionen vererbt.

    Dies ist bei der OOP ein wichtiger bestandteil
"""


class Animal:

    def __init__(self, name, gattung):
        self.name = name
        self.gattung = gattung
        self.art = self.__class__.__name__

    def introduce(self):
        print(f"Ich heiße {self.name}, ich gehöre zur gattung der {self.gattung} und bin ein {self.art} !!")

    def schlafen(self, dauer):
        raise NotImplemented

    def fressen(self):
        print(f"{self.name} frisst")


class Bear(Animal):

    def __init__(self, name, gattung, alter, gewicht, groesse):
        super(Bear, self).__init__(name, gattung)
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse


class Grizzly(Bear):

    def __init__(self, name, gattung, alter, gewicht, groesse):
        super(Grizzly, self).__init__(name, gattung, alter, gewicht, groesse)


class BrownBear(Bear):

    def __init__(self, name, gattung, alter, gewicht, groesse):
        super(BrownBear, self).__init__(name, gattung, alter, gewicht, groesse)


class Fish(Animal):

    def __init__(self, name, gattung, alter, gewicht, groesse):
        super(Fish, self).__init__(name, gattung)
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse


class Goldfisch(Fish):
    def __init__(self, name, gattung, alter, gewicht, groesse):
        super(Goldfisch, self).__init__(name, gattung, alter, gewicht, groesse)


bruno = Grizzly("Bruno", "Säugetiere", 20, 500, 300)
franzi = BrownBear("franzi", "Säugetiere", 19, 400, 250)
goldi = Goldfisch("Goldi", "Wirbeltiere", 2, 0.1, 10)

bruno.fressen()
franzi.fressen()
goldi.fressen()

bruno.introduce()
franzi.introduce()
goldi.introduce()
