# in python ist es auch möglich eine variable anzahl an parametern zu übergegen

def summiere2(a, b):
    pass


def summiere3(a, b, c):
    pass


def summiere4(a, b, c, d):
    pass


"""
    *ARGS
    - Wenn die Parameterwerte für eine Funktion in Objektform vorliegen (einer Liste oder einem Tupel) 
      können sie eben in dieser Form an die Funktion übergeben werden.
    - Die Anzahl der Übergabeparameter an die Funktion soll variabel bleiben.
"""


def summiere(a, b, c, *args):
    return a, b, c, args


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(summiere(*liste))


def max(*values):
    result = values[0]
    for zahl in values:
        if zahl > result:
            result = zahl
    return result


zahlen = [1, 6, 4, 5, 8, 9, 2, 4]
print(max(*zahlen))

"""
    **KWARGS 
    - Übergabe der Parameter als Dictionary. Über die Keys werden die Werte den Parametern der Funktion zugeordnet.
    - kwargs sind verglichen mit *args eine konservative Variante an die Funktion ein Objekt zu übergeben. 
      Da das Objekt ein Dictionary ist, verhindert man eine Falschzuordnung von Parameter zu Wert 
      wie es durch die Order-Of-Appearence-Regel bei der Verwendung *args passieren kann.
"""


def print_list_of_dicts(**kwargs):
    print(kwargs)
    print(kwargs["vorname"])
    print(kwargs["nachname"])
    print(kwargs["alter"])


print_list_of_dicts(vorname="Stefan", nachname="Draeger", alter="40")


def func(required_arg, *args, **kwargs):
    print(required_arg)

    if args:
        print(args)

    if kwargs:
        print(kwargs)


func("run1")
print()
func("run2", 1, 2, '3')
print()
func("run3", 1, 2, '3', 4, 5, keyword0=[1, 3, 4], keyword1=4, keyword2="foo")
