"""
    Aufgabe 1
        benutzte im folgenden Code dein wissen über exceptions.

        a.) passe den Code mit einem Exception Handling so an das, dass die Exception abgefangen wird und eine
        nachricht ausgegeben wird

        b.) fange die exceptions lasse jeweils ein None zurückgeben

        * Optional
        c.) Baue eine Prüfung so ein das die Exception nicht mehr erscheint, du aber eine eigene Exception-Klasse
            für diesen AmpelError schreibst. Diese Exception-Klasse soll eine Nachricht generieren (__str__).
            Das Programm soll beim aufrufen der Exception nicht abbrechen sondern weiter laufen und die nachrichten
            anzeigen.


"""


# a.)
def read_file():
    try:
        with open("throw.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("Die datei existiert nicht")


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
        try:
            return self.zahl1 / self.zahl2
        except ZeroDivisionError:
            print("Durch 0 Teilen nicht möglich")

    def do_more(self):
        return_value = None
        my_object = Object()
        try:
            return_value = self.get_name(my_object)
            return return_value
        except AttributeError:
            print("Das Attribute name Existiert nicht")
        finally:
            return return_value

    def get_name(self, object):
        return object.namee


do = DoSomething(5, 0)
name = do.do_more()
print(name)
result = do.do_something_1()
print(result)


# c.)
class AmpelZustandNotFoundError(Exception):
    def __init__(self, anfangs_zustand, klasse):
        self.message = f"Der Ampelzustand {anfangs_zustand} ist für {klasse.__name__} nicht vorhanden"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class Ampel(object):
    DEFAULT_ZUSTAND = 0

    def __init__(self, liste_ampel_zustaende, anfangs_zustand):
        self.liste_zustaende = liste_ampel_zustaende
        self.index_aktueller_zustand = self.set_anfangs_zustand(anfangs_zustand)

    def set_anfangs_zustand(self, anfangs_zustand):
        return_zustand = self.DEFAULT_ZUSTAND
        try:
            if anfangs_zustand not in self.liste_zustaende:
                raise AmpelZustandNotFoundError(anfangs_zustand, self.__class__)
            else:
                return_zustand = self.liste_zustaende.index(anfangs_zustand)
        except AmpelZustandNotFoundError as ex:
            print(ex)
        finally:
            return return_zustand

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
