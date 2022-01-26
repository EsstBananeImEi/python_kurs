from __future__ import annotations


class Facade:
    """
        Die Klasse Facade bietet eine einfache Schnittstelle zur komplexen Logik eines oder
        mehrerer Subsysteme. Die Facade delegiert die Client-Anfragen an die
        entsprechenden Objekte innerhalb des Subsystems. Die Facade ist auch verantwortlich für
        die Verwaltung ihres Lebenszyklus. All dies schirmt den Client von der unerwünschten
        Komplexität des Subsystems ab.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
            Je nach Anforderungen Ihrer Anwendung können Sie der Facade vorhandene
            Subsystemobjekte zur Verfügung stellen oder die Facade zwingen, diese selbst zu erstellen.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
            Die Methoden der Facade sind bequeme Abkürzungen zu der anspruchsvollen
            Funktionalität der Subsysteme. Allerdings erhalten die Clients nur einen Bruchteil
            der Fähigkeiten eines Subsystems.
        """

        results = []
        results.append("Facade initialisiert Subsysteme:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade beauftragt Subsysteme mit der Ausführung der Aktion:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
        Das Subsystem kann Anfragen entweder von der Fassade oder direkt vom Client annehmen.
        In jedem Fall ist die Fassade für das Subsystem ein weiterer Client, und sie ist
        nicht ein Teil des Subsystems.
    """

    def operation1(self) -> str:
        return "Subsystem1: Fertig!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Los!"


class Subsystem2:
    """
        Einige Fassaden können mit mehreren Subsystemen gleichzeitig arbeiten.
    """

    def operation1(self) -> str:
        return "Subsystem2: Fertig werden!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Feuer!"


def client_code(facade: Facade) -> None:
    """
        Der Client-Code arbeitet mit komplexen Subsystemen über eine einfache Schnittstelle
        die von der Facade bereitgestellt wird. Wenn eine Facade den Lebenszyklus des
        Subsystems verwaltet, weiß der Client möglicherweise nicht einmal von der Existenz des
        Subsystems. Mit diesem Ansatz können Sie die Komplexität unter Kontrolle halten.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    """
        Der Client-Code hat möglicherweise einige der Objekte des Subsystems bereits erstellt.
        In diesem Fall kann es sinnvoll sein, die Facade mit diesen Objekten zu initialisieren, 
        anstatt die Facade neue Instanzen erstellen zu lassen.
    """
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)