class Component():
    """
        Die Basisschnittstelle "Component" definiert Operationen, die durch "Dekoratoren" geändert werden können.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
        Konkrete Komponenten bieten Standardimplementierungen der Operationen.
        Es kann mehrere Varianten dieser Klassen geben.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
        Die Basisklasse Decorator folgt der gleichen Schnittstelle wie die anderen Komponenten.
        Der primäre Zweck dieser Klasse ist die Definition der Wrapping-Schnittstelle für
        alle konkreten Dekoratoren. Die Standardimplementierung des Wrapping-Codes
        könnte ein Feld zum Speichern einer wrapper Komponente und die Mittel zum
        initialisieren sein.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
            Der Decorator delegiert die gesamte Arbeit an die wrapper Komponente.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Konkrete Dekoratoren rufen das gewrappte Objekt auf und verändern dessen Ergebnis in irgendeiner Weise.
    """

    def operation(self) -> str:
        """
            Dekorateure können die übergeordnete Implementierung der Operation aufrufen, anstatt
            das gewrappte Objekt direkt aufzurufen. Dieser Ansatz vereinfacht die Erweiterung
            von Dekoratorklassen.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """
        Decorators können ihr Verhalten entweder vor oder nach dem Aufruf eines
        gewrappten Objekts ausführen.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    """
    Der Client-Code arbeitet mit allen Objekten, die das Component-Interface verwenden.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":
    """ Auf diese Weise kann der Client-Code sowohl einfache Komponenten unterstützen... """
    simple = ConcreteComponent()
    print("Client: Ich habe eine einfache Komponente:")
    client_code(simple)
    print("\n")

    """
        ...als auch dekorierte.
        
        Beachten Sie, dass Dekoratoren nicht nur einfache Komponenten umhüllen können, 
        sondern auch andere Dekoratoren.
    """
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Jetzt habe ich eine dekorierte Komponente:")
    client_code(decorator2)