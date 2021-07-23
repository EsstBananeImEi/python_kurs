"""
    Dies ist ein sehr einfaches Singelton Pattern, aber dieses hier ist nicht Threadsafe.
"""

class SingletonMeta(type):
    """
        Die Singleton-Klasse kann in Python auf unterschiedliche Weise implementiert werden. Einige
        mögliche Methoden sind: Basisklasse, Dekorator, Metaklasse. Wir werden die
        Metaklasse verwenden, weil sie für diesen Zweck am besten geeignet ist.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
            Mögliche Änderungen des Werts des Arguments `__init__` haben keinen Einfluss auf
            die zurückgegebene Instanz.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
            Schließlich sollte jedes Singleton eine Geschäftslogik definieren, die auf seiner Instanz ausgeführt werden kann.
        """

        # ...


if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")