###############################################  Aufgabe 1 ###########################################################


"""
    Auto- und Fußgängerampeln weisen eine Reihe von Gemeinsamkeiten auf.
    Beim Weiterschhalten durchlaufen beide zyklisch eine bestimmte Folge von Zuständen.

    Autoampel: Rot -> Rotgelb -> Grün -> Gelb
                ^                          |
                |                          |
                ----------------------------

    Fußgängerampel: Rot -> Grün
                     ^       |
                     |       |
                     ---------

    Das Verhalten von Ampeln lässt sich verallgemeinernd mit dem folgenden Klassendiagramm beschreiben:

    ##############################################
    #                  Ampel                     #
    ##############################################
    # liste_zustaende: list of str               #
    # index_aktueller_zustand: int               #
    ##############################################
    # Ampel(liste_ampel_zustaende): list of str) #
    # schalten()                                 #
    # get_zustand(): str                         #
    # set_zustand(zustand: str)                  #
    ##############################################

"""


# Hier eine Implementierung zu dieser allgemeinen Ampel-Klasse.
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


"""
    Aufgabe 1
    
    (a) Simuliere mit dieser Klasse das Verhalten einer Fußgängerampel.
    
    (b) Autoampeln in anderen Ländern (z.B. in Frankreich) verhalten sich manchmal etwas anders als in Deutschland. 
        Benutze die Klasse Ampel zur Simulation einer solchen Ampel.
        
        Ampel Frankreich:  Rot -> Grün -> Gelb
                            ^               |
                            |               |
                            -----------------
    
    Tip: 1. Schaue dir die Ampel-Klasse genau an und versuche nachzuvollziehen wie diese Klasse funktioniert
         2. Vergiss an die Ampel zustände nicht!
         3. du kannst schon einen zustand am anfang setzten
         4. du hast eine liste, nutze die möglichkeit die einträge zu durchlaufen :-)
    
    Falls du zu der Ampel Klasse ein beispiel benötigst, um eine Ampelschaltung zu Simulieren Schaue in die Datei
    "beispiel_aufgabe_klassen.py"
    
"""

# a.)


# b.)


###############################################  Aufgabe 2 ###########################################################

"""
    Aus der allgemeinen Ampel-Klasse kann man durch eine Erweiterung Klassen für Auto- und Fußgängerampeln gewinnen.
    
                     ####################################################################
                     #                  Ampel                                           #
                     ####################################################################
                     # liste_zustaende: list of str                                     #
                     # index_aktueller_zustand: int                                     #
                     ####################################################################
                     # Ampel(liste_ampel_zustaende, anfangs_zustand): list of str, str) #
                     # schalten()                                                       #
                     # get_zustand(): str                                               #
                     # set_zustand(zustand: str)                                        #
                     ####################################################################
                                                      ^
                                                      |
                                -----------------------------------------------
                                |                                             |
                                |                                             |      
            ###########################################   ###########################################
            #                  AmpelAuto              #   #             AmpelFussgaenger            #
            ###########################################   ###########################################
            #                                         #   #                                         #  
            ###########################################   ########################################### 
            # AmpelAuto(anfangs_zustand: str)         #   # AmpelFussgaenger(anfangs_zustand: str)  # 
            # get_lampen(): (bool, bool, bool)        #   # get_lampen(): (bool, bool)              #
            ###########################################   ###########################################
            
    Die Klassen AmpelAuto und AmpelFussgaenger sollen dabei sämtliche Attribute und Methoden der 
    Basisklasse Ampel übernehmen (man sagt auch erben) und zusätzlich die im Klassendiagramm aufgeführten 
    neuen Methoden (die Konstruktormethode und die Methode getLampen) vorsehen.

    Hier eine Implementierung der beiden Klassen Ampel und AmpelAuto. 
    Beachte die vererbung AmpelAuto(Ampel) bei der Deklaration der Klasse AmpelAuto.
        
"""


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


# Test
a = AmpelAuto('Grün')
print(a.get_zustand())
print(a.get_lampen())
print()
for i in range(4):
    a.schalten()
    print(a.get_zustand())
    print(a.get_lampen())
    print()

"""
    Aufgabe 2
    
    (a) Führe das Programm selbst aus. Kannst du das Verhalten erklären?
    
    (b) Entwickle analog eine Klasse AmpelFussgaenger und teste sie.
"""

# a.)


# b.)
