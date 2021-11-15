"""
    Definition
        Ein Dekorator ist ein aufrufbares Python Objekt, das ein Argument annimmt - die zu dekorierende Funktion.
        In Python wird zwischen Signatur bewahrenden und Signatur verändernden Dekoratoren unterschieden.
        Die klasssischen Beispiele für Signatur veränderten Dekoratoren sind die built-in staticmethod und classmethod.
        Durch sie wird die Bindung der Methode an die Klasseninstanz aufgehoben.

    Vorteile
        Dekoratoren erlauben es, deklarativ zu programmieren, indem der Funktion ein Dekorator vorangestellt wird.
        Dadurch wird die Kernfunktionalität um einen neuen Aspekt erweitert.
        Insbesondere das Kapseln von Aspekten (Logging, Tracing) in Dekoratoren ermöglicht es,
        die reine Funktionalität von der erweiterten Funktionalität zu trennen und diese wiederverwendbar zu halten.
        Aspekte der Programmfunktionalität wie Logging müssen nicht mehr mit der Kerfunktionalität verwoben werden.
"""


def outer(func):
    print("Ich bin eine aeußere Funktion")
    func()


def inner():
    print("Ich bin eine innere Funktion")


outer_func = outer
inner_func = inner
outer_func(inner_func)
print("\n########################")


def outer():
    def inner():
        print("Ich bin eine innere Funktion")

    return inner


outer_func = outer()
outer_func()
outer()()

print("\n########################")


def my_decorator(func):
    def inner():
        print("Ich bin eine innere Funktion")
        func()

    return inner


def outer():
    print("Ich bin eine aeußere Funktion")


outer()

my_deco = my_decorator(outer)
my_deco()

print("\n######### Funktionen mit Rückgabewert ###############")

"""
    Funktionen mit Rückgabewert:
        Aktuell ist in unserer „dekorierten“ Funktion outer() nur ein Aufruf der print()-Funktion implementiert. 
        Es kann allerdings vorkommen, dass wir auch in dieser Funktion einen Rückgabewert definieren wollen. 
        Deshalb schauen wir uns jetzt an, wie wir den Decorator bei einer solchen Funktion entsprechend nutzen können.
"""


def my_decorator(func):
    def inner():
        print("Ich bin eine innere Funktion")
        """
            Statt die Funktion func() einfach aufzurufen, 
            speichern wir den Rückgabewert der Funktion jetzt in der „rueckgabe“-Variable. 
            Diese können wir dann der print()-Funktion übergeben.
        """
        outer_return = func()
        print(outer_return)

    return inner


@my_decorator
def outer():
    return "Ich bin eine aeußere Funktion"


outer()

print("\n######### Funktionen mit Argumenten ###############")

"""
    Funktionen mit Argumenten
        Es ist auch möglich, dass Funktionen, die „dekoriert“ werden sollen, Argumente erfordern. 
        Wie wir bereits wissen wird die Funktion selbst als Argument in den Decorator eingegeben. 
        Schauen wir uns also an wie wir mit Argumenten umgehen können. 
"""


def my_decorator(func):
    def inner(str):
        print("Ich bin eine innere Funktion")
        func(str)

    return inner


@my_decorator
def outer(my_message):
    print(my_message)


outer("Ich bin eine aeußere Funktion")

print("\n######### Decorator mit Bedingungen ###############")


def my_decorator1(fun):
    def inner():
        print("Ich bin die innere Funktion von my_decorator1")
        fun()

    return inner


def my_decorator2(fun):
    def inner():
        print("Ich bin die innere Funktion von my_decorator2")
        fun()

    return inner


# bedingung = int(input("Geben Sie 1 für 'decorator1' oder 2 für 'decorator2' ein\n"))
# if bedingung == 1:
#     @my_decorator1
#     def outer():
#         print("Ich bin die aeußere Funktion")
# elif bedingung == 2:
#     @my_decorator2
#     def outer():
#         print("Ich bin die aeußere Funktion ")

# outer()

print("\n######### Mehrere Decoratoren ###############")


def my_decorator1(func):
    def inner():
        print("Ich bin die innere Funktion von my_decorator1")
        func()

    return inner


def my_decorator2(func):
    def inner():
        print("Ich bin die innere Funktion von my_decorator2")
        func()

    return inner


def my_decorator3(func):
    def inner():
        print("Ich bin die innere Funktion von my_decorator3")
        func()

    return inner


@my_decorator1
@my_decorator2
@my_decorator3
def outer():
    print("Ich bin die aeußere Funktion")


outer()

print("\n######### Mehrfache ausführung ###############")


def do_twice(func):
    def func_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return func_do_twice


@do_twice
def say_hello():
    print("Hello World")


@do_twice
def say_goodbye(name):
    print(f"Goodbye {name}")


say_hello()
say_goodbye("Dave")

print("\n######### Beispiel aus der Praxis ###############")


class User():
    def __init__(self, name, bool):
        self.name = name
        self.logged_in = bool


def login_required(func):
    """Make sure user is logged in before proceeding"""

    def wrapper_login_required(*args, **kwargs):
        if user.logged_in is False:
            return "Leite user zum Login um"
        return func(*args, **kwargs)

    return wrapper_login_required


@login_required
def show_secret(user):
    print(f"Ich bin {user.name}'s secret")


user = User("Peter", True)
print(show_secret(user))
