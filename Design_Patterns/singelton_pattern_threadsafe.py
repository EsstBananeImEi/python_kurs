from threading import Lock, Thread


class SingletonMeta(type):
    """
        Dies ist eine thread-sichere Implementierung von Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
            Mögliche Änderungen des Werts des Arguments `__init__` haben keinen Einfluss auf
            die zurückgegebene Instanz.
        """

        """
            Stellen Sie sich nun vor, dass das Programm gerade erst gestartet wurde. Da es noch keine
            Singleton-Instanz gibt, können mehrere Threads gleichzeitig die
            vorherige Bedingung erfüllen und diesen Punkt fast zur gleichen Zeit erreichen.  Der
            erste von ihnen wird eine Sperre erhalten und weitermachen, während der
            Rest hier warten wird.
        """
        with cls._lock:
            """
                Der erste Thread, der die Sperre erhält, erreicht diese Bedingung,
                geht hinein und erzeugt die Singleton-Instanz. Sobald er den
                Sperrblock verlässt, kann ein Thread, 
                der möglicherweise auf die Freigabe der Sperre gewartet hat diesen Abschnitt betreten. 
                Da aber das Singleton-Feld bereits initialisiert ist, wird der Thread kein neues Objekt erzeugen.
            """
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
        Wir werden diese Eigenschaft verwenden, um zu beweisen, dass unser Singleton wirklich funktioniert.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
            Schließlich sollte jedes Singleton eine Geschäftslogik definieren, die auf seiner Instanz ausgeführt werden kann.
        """


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":

    print("Wenn Sie den gleichen Wert sehen, dann wurde Singleton wiederverwendet (yay!)\n"
          "Wenn Sie unterschiedliche Werte sehen, "
          "dann wurden 2 Singletons erstellt (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()