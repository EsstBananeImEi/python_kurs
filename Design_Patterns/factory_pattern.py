from __future__ import annotations
from abc import ABC, abstractmethod

"""
    Als „Factories“ werden Hilfsobjekte bezeichnet, deren Aufgabe es ist,
    die Erzeugung eines Objekts von seiner Verwendung zu trennen.
    Man unterscheidet im Allgemeinen zwischen der „Factory Method“ und der „Factory Class“
    als zwei verschiedenen Möglichkeiten, dieses Prinzip zu implementieren.
"""


class Creator(ABC):
    """
        Die Creator-Klasse deklariert die Factory-Methode, die ein Objekt einer Produktklasse liefern soll.
        Die Unterklassen des Creators stellen normalerweise die Implementierung dieser Methode.

    """

    @abstractmethod
    def factory_method(self):
        """
            Beachten Sie, dass der Creator möglicherweise auch eine Standardimplementierung der
            der Factory-Methode bereitstellt.
        """
        pass

    def some_operation(self) -> str:
        """
            Beachten Sie auch, dass trotz seines Namens die Hauptaufgabe des Creators
            nicht das Erstellen von Produkten ist. Normalerweise enthält er einige Kerngeschäftslogiken,
            die sich auf Product-Objekte bezieht, die von der Factory-Methode zurückgegeben werden.
            Unterklassen können diese Geschäftslogik indirekt ändern, indem sie die
            Factory-Methode überschreiben und einen anderen Produkttyp zurückgeben.
        """

        product = self.factory_method()

        result = f"Creator: Der Code desselben Creators hat gerade mit dem {product.operation()} gearbeitet"

        return result


"""
    Concrete Creators überschreiben die Factory-Methode, um den Typ des resultierenden
    Produkttyps zu ändern.
"""


class ConcreteCreator1(Creator):
    """
        Beachten Sie, dass die Signatur der Methode immer noch den abstrakten Produkttyp verwendet,
        obwohl das konkrete Produkt tatsächlich von der Methode zurückgegeben wird. Diese
        kann der Creator auf diese Weise unabhängig von konkreten Produktklassen bleiben.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
        Die Schnittstelle Product deklariert die Operationen, die alle konkreten Produkte
        implementieren müssen.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
    Konkrete Produkte bieten verschiedene Implementierungen der Schnittstelle Product.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Ergebnis des ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Ergebnis des ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
        Der Client-Code arbeitet mit einer Instanz eines Concrete Creators, wenn auch über
        seine Basisschnittstelle. Solange der Client weiterhin mit dem Creator über
        die Basisschnittstelle arbeitet, können Sie ihm eine beliebige Unterklasse des Creators übergeben.
    """

    print(f"Client: Die Klasse des Erstellers ist mir nicht bekannt, aber es funktioniert trotzdem.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Gestartet mit dem ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Gestartet mit dem ConcreteCreator2.")
    client_code(ConcreteCreator2())