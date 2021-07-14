"""
    Aufgabe 1
        benutzte im folgenden Code dein wissen über exceptions.

        a.) passe den Code mit einem Exception Handling so an das, dass die Exception abgefangen wird und eine
        nachricht ausgegeben wird

        b.) fange die exceptions lasse jeweils ein None zurückgeben

        * Optional
        c.) Baue eine Prüfung so ein das die Exception nicht mehr erscheint, du aber eine eigene Exception-Klasse
            für diesen AmpelError schreibst. Diese Exception-Klasse soll eine Nachricht generieren (__str__).
            Mache dir gedanken wie du es erreichen kannst das, dass Programm trozdem funktionsfähig bleibt, obwohl du
            eine Exception wirfst und die nachrichten anzeigst.

            Denn es wäre extrem schlecht wenn die Ampel troz des fehlers nicht mehr funktioniert :-)

            - Für die Aufgabe "c" nehmen wir folgenden umstand an:
                - Es existiert "Immer" wirklich "IMMER" eine liste mit zuständen, auf die wir zugreifen können!


        tip zu c.)
        1. Baue die ampel ein wenig um, damit du prüfen kannst ob der anfangs_zustand in der liste ist
        2. Baue deine eigene Exception klasse, in der du eine nachricht erstellt (__str__ überschreiben)
        3. lasse die Exception in deiner Prüfung an der richtigen stelle auslösen
        4. fange die Exception ab
        5. gib die nachricht aus
        6. sorge dafür das die Ampel an einer anderen stelle anfängt und trozdem läuft wenn der fehler ensteht
"""


# a.)
def read_file():
    with open("throw.txt", "r") as file:
        file.read()


read_file()


# b.)
class Object:
    name = "Peter"
    age = 21
    plz = 53776


class DoSomething():

    def __init__(self, zahl1, zahl2):
        self.zahl1 = zahl1
        self.zahl2 = zahl2

    def do_something_1(self):
        return self.zahl1 / self.zahl2

    def do_more(self):
        return_value = None
        my_object = Object()
        return_value = self.get_name(my_object)
        return return_value

    def get_name(self, object):
        return object.namee


do = DoSomething(5, 0)
name = do.do_more()
print(name)
result = do.do_something_1()
print(result)


# c.)


class Ampel(object):

    def __init__(self, liste_ampel_zustaende, anfangs_zustand):
        self.liste_zustaende = liste_ampel_zustaende
        self.index_aktueller_zustand = self.liste_zustaende.index(anfangs_zustand)

    def schalten(self):
        if self.index_aktueller_zustand < len(self.liste_zustaende) - 1:
            self.index_aktueller_zustand = self.index_aktueller_zustand + 1
        else:
            self.index_aktueller_zustand = 0

    def get_zustand(self):
        return self.liste_zustaende[self.index_aktueller_zustand]

    def set_zustand(self, zustand):
        self.index_aktueller_zustand = self.liste_zustaende.index(zustand)


class AmpelAuto(Ampel):
    def __init__(self, anfangs_zustand):
        super().__init__(['Rot', 'Rotgelb', 'Grün', 'Gelb'], anfangs_zustand)

    def get_lampen(self):
        lampen = None
        zustand = self.liste_zustaende[self.index_aktueller_zustand]
        if zustand == 'Rot':
            lampen = (True, False, False)
        elif zustand == 'Rotgelb':
            lampen = (True, True, False)
        elif zustand == 'Grün':
            lampen = (False, False, True)
        elif zustand == 'Gelb':
            lampen = (False, True, False)
        return lampen


class AmpelFussgaenger(Ampel):
    def __init__(self, anfangs_zustand):
        super().__init__(['Rot', 'Grün'], anfangs_zustand)

    def get_lampen(self):
        lampen = None
        zustand = self.liste_zustaende[self.index_aktueller_zustand]
        if zustand == 'Rot':
            lampen = (True, False)
        elif zustand == 'Grün':
            lampen = (False, True)
        return lampen


# Test
print("\n#########################")
a = AmpelAuto('Grünss')
print(a.get_zustand())
print(a.get_lampen())
for i in range(4):
    a.schalten()
    print(a.get_zustand())
    print(a.get_lampen())

print("\n#########################")
b = AmpelFussgaenger('GelbGrün')
print(b.get_zustand())
print(b.get_lampen())
for i in range(4):
    b.schalten()
    print(b.get_zustand())
    print(b.get_lampen())
