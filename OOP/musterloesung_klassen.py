###############################################  Aufgabe 1 ###########################################################

class Ampel(object):
    def __init__(self, liste_ampel_zustaende):
        self.liste_zustaende = liste_ampel_zustaende
        self.index_aktueller_zustand = 0

    def schalten(self):
        if self.index_aktueller_zustand < len(self.liste_zustaende) - 1:
            self.index_aktueller_zustand = self.index_aktueller_zustand + 1
        else:
            self.index_aktueller_zustand = 0

    def get_zustand(self):
        return self.liste_zustaende[self.index_aktueller_zustand]

    def set_zustand(self, zustand):
        self.index_aktueller_zustand = self.liste_zustaende.index(zustand)


# a.) Fußgänger Ampel
a = Ampel(['Rot', 'Grün'])
a.set_zustand('Rot')
print(a.get_zustand())
for i in range(len(a.liste_zustaende)):
    a.schalten()
    print(a.get_zustand())

# b.) Französische Ampel
print()
a = Ampel(['Rot', 'Grün', "Gelb"])
a.set_zustand('Rot')
print(a.get_zustand())
for i in range(len(a.liste_zustaende)):
    a.schalten()
    print(a.get_zustand())

###############################################  Aufgabe 2 ###########################################################

"""
       
    a.) Führe das Programm selbst aus. Kannst du das Verhalten erklären?
    was passiert alles:  
        - Das AmpelAuto wird mit dem Startwert "Grün" inizialisiert
           somit beginnt die Ampel bei Grün
        - Es wird eine ausgabe des aktuellen zustands auf der Console gemacht
        - Es wird die aktivität der lampen ausgegeben, also ob sie True oder False bzw an oder aus sind
        - dann wird in einer for schleife 4x durchlaufen und für jeden zyklus wird die ampel geschalten also
           der aktuelle index erhöht, der zustand und die aktivität der lampen ausgegeben
        - in der get_lampen wird gebrüft wie der zustand ist und dementsprechend der zustand der lampen gesetzt
    
    
"""


# b.)
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


a = AmpelFussgaenger('Rot')
print(a.get_zustand())
print(a.get_lampen())
print()
for i in range(2):
    a.schalten()
    print(a.get_zustand())
    print(a.get_lampen())
    print()
