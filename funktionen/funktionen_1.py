# durch Funktionen ist es uns möglich unseren Code zu struckturieren und/oder unseren Code wiederverwendbar zu
# machen, dies vermeidet unschöne Code Duplizierung und hilft gegen spagetti code

# Wir haben sogar schon Funktionen genutzt
# z.b haben wir diese in Python Integrierten Funktionen bereits genutzt

print()
int()
str()
"".strip()
len([])


# und einige mehr :)
# nun wollen wir uns aber eigene Funktionen schreiben
# Um eine Funktion du definierten schreiben wir am anfang ein "def" dann den methoden namen


def say_hello() -> None:
    print("Hallo und Willkommen")


say_hello()
say_hello()


# Einer Methode Können auch parameter übergeben werden
def say_hello_to(name) -> None:
    print("Hallo %s, Willkommen" % name)


say_hello_to("Paul")
say_hello_to(name="Frank")


# Es ist auch möglich mehrere Parameter zu übergeben
def multipliziere(a, b) -> None:
    if a is not None \
            and b is not None:
        print(a * b)


multipliziere(5, 5)


# Methoden können auch ergebnisse zurückgeben
def get_highest_value(zahl1, zahl2):
    if zahl1 > zahl2:
        return zahl1
    else:
        return zahl2


rtv = get_highest_value(4, 6)
print(rtv)

rtv = get_highest_value(zahl2=4, zahl1=6)
print(rtv)
