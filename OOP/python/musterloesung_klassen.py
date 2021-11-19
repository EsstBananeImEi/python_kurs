###############################################  Aufgabe 1 ###########################################################

from abc import ABC, abstractmethod


class Person:
    def __init__(self) -> None:
        self.name = None
        self.alter = None
        self.geschlecht = None

    def set_name(self, name: str) -> None:
        self.name = name

    def set_alter(self, alter: int) -> None:
        self.alter = alter

    def set_geschlecht(self, geschlecht: str) -> None:
        self.geschlecht = geschlecht

    def birthday(self) -> None:
        self.alter += 1

    def talk(self) -> None:
        print(f"Mein Name ist {self.name} ich bin {self.alter} Jahre alt.")


alice = Person()
alice.set_name("Alice")
alice.set_alter(22)
alice.talk()
alice.birthday()
alice.talk()

###############################################  Aufgabe 2 ###########################################################


class Mensch:
    def __init__(self) -> None:
        self.name = None
        self.alter = None
        self.geschlecht = None
        self.augenfarbe = None

    def set_name(self, name: str) -> None:
        self.name = name

    def set_alter(self, alter: int) -> None:
        self.alter = alter

    def set_geschlecht(self, geschlecht: str) -> None:
        self.geschlecht = geschlecht

    def set_augenfarbe(self, augenfarbe: str) -> None:
        self.augenfarbe = augenfarbe

    def birthday(self) -> None:
        self.alter += 1

    def talk(self) -> None:
        if self.augenfarbe is not None:
            print(
                f"Mein Name ist {self.name} ich bin {self.alter} Jahre alt und meine Augenfarbe ist {self.augenfarbe}")
        else:
            print(f"Mein Name ist {self.name} ich bin {self.alter} Jahre alt.")


class Person(Mensch):
    pass


petra = Person()
petra.set_name("Petra")
petra.set_alter(44)
petra.talk()
petra.set_augenfarbe("blau")
petra.talk()

###############################################  Aufgabe 3 ###########################################################


class Computer(ABC):

    def __init__(self, architecture: str, os_system: str) -> None:
        self.architecture = architecture
        self.os_system = os_system

    @abstractmethod
    def start_process(self) -> None:
        pass


class Laptop(Computer):
    def start_process(self) -> None:
        print(
            f"Starte Laptop Prozess für {self.os_system} {self.architecture}")


class Desktop(Computer):
    def start_process(self) -> None:
        print(
            f"Starte Desktop Prozess für {self.os_system} {self.architecture}")


class Programmer:
    programmers = []

    def __init__(self, name: str, team: str) -> None:
        self.name = name
        self.team = team

    def __del__(self) -> None:
        self.programmers.remove(self.name)

    @classmethod
    def get_aktive_programmers(cls) -> str:
        if len(cls.programmers) == 0:
            return "Kein Aktiver Programmierer"
        return f"Aktive Programmierer: {', '.join(cls.programmers)}"

    def beginn_work(self, computer: Computer) -> None:
        print(f"{self.name} beginnt seine Arbeit")
        if not self.name in self.programmers:
            self.programmers.append(self.name)
        computer.start_process()


# Inizialisieren der Arbeitsgeräte
laptop = Laptop("32 bit", "Linux")
desktop = Desktop("64 bit", "Windows")

# Inizialisieren der Programmierer
heike = Programmer("Heike", "Python")
peter = Programmer("Peter", "C#")
martin = Programmer("Martin", "Java")

heike.beginn_work(laptop)
peter.beginn_work(desktop)
martin.beginn_work(desktop)

Programmer.get_aktive_programmers()

peter = None
Programmer.get_aktive_programmers()
