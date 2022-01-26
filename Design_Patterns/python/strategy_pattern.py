"""
    Das Strategy-Muster ist in Python-Code sehr verbreitet.
    Es wird oft in verschiedenen Frameworks verwendet, um Benutzern eine Möglichkeit zu bieten,
    das Verhalten einer Klasse zu ändern, ohne sie zu erweitern

    Strategy-Muster können durch eine Methode erkannt werden,
    die verschachtete Objekte die eigentliche Arbeit erledigen lässt,
    sowie durch den Setter, der es erlaubt, dieses Objekt durch ein anderes zu ersetzen.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    """
        Der Context definiert die Schnittstelle, die für Kunden von Interesse ist.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
            Normalerweise akzeptiert der Context eine Strategie über den Konstruktor, aber
            bietet auch einen Setter, um es zur Laufzeit zu ändern.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
            Der Context enthält einen Verweis auf eines der Strategieobjekte. Der
            Context kennt die konkrete Klasse einer Strategie nicht.
            Es sollte mit allen Strategien über die Strategie-Schnittstelle funktionieren.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
            Normalerweise ermöglicht der Kontext das Ersetzen eines Strategy-Objekts zur Laufzeit.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
            Der Context delegiert einige Arbeiten an das Strategy-Objekt,
            anstatt mehrere Versionen des Algorithmus allein zu implementieren.
        """

        # ...

        print("Context: Sortieren von Daten anhand der Strategie (nicht sicher, wie es geht)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


class Strategy(ABC):
    """
        Die Strategie-Schnittstelle deklariert Operationen,
        die für alle unterstützten Versionen eines Algorithmus gelten.
        Der Context verwendet diese Schnittstelle, um den durch Concrete Strategies definierten Algorithmus aufzurufen.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
    Konkrete Strategien implementieren den Algorithmus unter Befolgung der grundlegenden Strategie-Schnittstelle. 
    Die Schnittstelle macht sie im Kontext austauschbar.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    """
        Der Client wählt eine konkrete Strategie aus und übergibt sie an den Kontext. 
        Der Client sollte sich der Unterschiede zwischen den Strategien bewusst sein, 
        um die richtige Wahl treffen zu können.
    """

    context = Context(ConcreteStrategyA())
    print("Client: Strategie ist auf normale Sortierung eingestellt.")
    context.do_some_business_logic()
    print()

    print("Client: Die Strategie ist auf umgekehrte Sortierung eingestellt.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()