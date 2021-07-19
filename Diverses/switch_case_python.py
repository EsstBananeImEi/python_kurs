"""
    Python verfügt nicht über eingebaute Switch-Anweisungen, wie man sie in Programmiersprachen wie PHP und Java findet.
    Stattdessen könnte man als Python-Programmierer versucht sein, if-else-if-Blöcke zu verwenden,
    aber Switch-Cases sind wegen der Sprungtabelle effizienter zu verwenden als die if-else-if-Leiter.

    Der Grund dafür ist, dass er nicht jede Bedingung sequenziell auswertet,
    sondern sich den ausgewerteten Ausdruck oder die Variable ansieht und direkt zu dem entsprechenden Codezweig springt,
    der ausgeführt werden soll.

    Dennoch haben wir 4 Wege ein Switch zu erstellen

"""

""" Beispiel 1 - Switch mit dem if else konstrukt """


def switch():
    option = int(input("enter your option from 1-3 to get the name on month : "))

    if option == 1:
        result = "January"
        print("the month is = ", result)

    elif option == 2:
        result = "febuary"
        print("the month is ", result)

    elif option == 3:
        result = "march"
        print("the month is ", result)

    else:
        print("Incorrect option")


# switch()


""" Beispiel 2 - Dictionary mapping to return value """

b = {

    1: "Jan",

    2: "Feb",

    3: "Mar",

    4: "Apr"

}

print(b.get(5, "nothing"))

""" Beispiel 3 - Dictionary mapping replacement"""


def numbers_to_strings(argument):
    switcher = {

        1: "Jan",

        2: "Feb",

        3: "Mar"

    }

    return switcher.get(argument, "nothing")


print(numbers_to_strings(2))

"""  
    Im obigen Python-Switch-Fallbeispiel schreiben wir zunächst eine Funktion, 
    um eine Zahl in eine Zeichenkette zu konvertieren. 
    Die get()-Methode des Datentyps dictionary gibt den Wert des übergebenen Arguments zurück, 
    wenn es im dictionary vorhanden ist. Andernfalls wird das zweite Argument als Standardwert des übergebenen Arguments zugewiesen
"""

""" Beispiel 4 - Switch mit einer Klasse"""


class PythonSwitchStatement:

    def switch(self, month):
        default = "Incorrect month"
        return getattr(self, '_case_' + str(month), lambda: default)()

    def _case_1(self):
        return "January"

    def _case_2(self):
        return "February"

    def _case_3(self):
        return "March"

    def _case_4(self):
        return "April"

    def _case_5(self):
        return "May"

    def _case_6(self):
        return "June"

    def _case_7(self):
        return "July"


switch_class = PythonSwitchStatement()

print(switch_class.switch(3))
print(switch_class.switch(4))
print(switch_class.switch(10))

"""
    Im obigen Beispiel für den Switch-Fall erstellen Sie zunächst eine Klasse namens PythonSwitchStatement, 
    um eine switch()-Methode zu definieren. Sie definiert auch andere Funktionen für bestimmte andere Fälle.

    Die switch()-Methode nimmt ein Argument 'month' und konvertiert es in eine Zeichenkette, 
    hängt es dann an das Case-Literal an und übergibt es an die getattr()-Methode, 
    die dann die in der Klasse verfügbare passende Funktion zurückgibt.

    Wenn sie keine Übereinstimmung findet, gibt die getattr()-Methode eine Lambda-Funktion als Standard zurück.
"""
