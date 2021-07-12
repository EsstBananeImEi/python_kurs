# Es ist auch möglich Funktionen mit standart werden zu erstellen

def say_hello_to(name) -> None:
    print("Hallo %s, Willkommen" % name)


def say_hello_default(name, nachname="Mustermann") -> None:
    print(name + " " + nachname)


# default parameter müssen immer nach den undefinierten parametern stehen


say_hello_default("Hans")
say_hello_default("Hans", "Blech")
