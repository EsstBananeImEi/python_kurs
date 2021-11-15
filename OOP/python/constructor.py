"""
    Um Objekte nach ihrer erzeugung nicht bearbeiten zu müssen, erstellt man diese mit einem Konstruktor .
    Ein Konstruktor ist eine besondere Methode in Python, diese wird immer aufgerufen sobald wir eine
    Klasse instanzieren.
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


# Durch den Konstruktor brauchen wir hinterher die attribute nicht mehr zu verändern
balu = Bear("balu", 10, 450, 250)
print(f"{balu.name} ist {balu.alter} Jahre alt, ist {balu.groesse}cm groß und wiegt {balu.gewicht}kg")

hugo = Bear("hugo", 15, 470, 300)
print(f"{hugo.name} ist {hugo.alter} Jahre alt, ist {hugo.groesse}cm groß und wiegt {hugo.gewicht}kg")


# Der Deconstuctor
# Für eine Klasse kann man eine Methode __del__ definieren. Wenn man eine Instanz einer Klasse mit del löscht,
# wird die Methode __del__ aufgerufen. Allerdings nur, falls es keine weitere Referenz auf diese Instanz gibt
# in c++ zum beispiel benötigt man Destruktoren um den Speicher zu bereinigen, in Python brauchen wir uns um die
# Speicherbereinigung aber nicht kümmern daher ist der Dekonstruktor eher selten vertreten


class Cat:

    def __init__(self):
        print("Cat wurde erstellt")

    def __del__(self):
        print("Cat wurde gelöscht")


cat = Cat()
cat.name = "Mizie"
print(cat.name)
