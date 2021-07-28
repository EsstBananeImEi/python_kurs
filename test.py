def do_something():
    try:
        raise ValueError
    except ValueError:
        return False


do_something()
print("wohoo")

# TODO 1: Bei den Datenstrukturen das Stack erstellen
# TODO 2: Threads Weitermachen
