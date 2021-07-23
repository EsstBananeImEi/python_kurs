"""
    Was ist mit staticmethod? Es ist classmethod ziemlich ähnlich,
    akzeptiert jedoch keine obligatorischen Parameter (wie es eine Klassenmethode oder eine Instanzmethode tut).
"""

import datetime


class Bear(object):

    def schlafen(self, dauer):
        print(f"der Bär schläft jetzt {dauer} minuten")

    def fressen(self):
        print(f"der Bär frisst")

    @classmethod
    def class_method(*args):
        return args

    @staticmethod
    def static_method(*args):
        return args

    @staticmethod
    def is_in_winter_rest(date_as_string):
        day, month, year = map(int, date_as_string.split('/'))
        if month >= 10 or month <= 2:
            return True
        return False


date = datetime.datetime.now().strftime("%d/%m/%Y")
is_in_winter_rest = Bear.is_in_winter_rest(date)
print(is_in_winter_rest)

obj = Bear()

print('Aufruf von static_method:', obj.static_method())
print('Aufruf von class_method:', obj.class_method())

"""
    Der Aufruf der @staticmethod hat als rückgabe wie zu erwarten nichts. 
    Wir übergeben keine Parameter an die Methode und bekommen dementsprechend nichts zurück. 
    Wie wir allerdings sehen, hat der Dekorator @classmethod dafür gesorgt, 
    dass der Parameter *args nun die Eigenschaften der Klasse sind, die an die Methode übergeben werden.
    
    Bei der Static Methode brauchen wir eine Klasse nicht erst zu Instanzieren sondern können ohne die klasse
    zu erstellen mit der Methode arbeiten
"""
