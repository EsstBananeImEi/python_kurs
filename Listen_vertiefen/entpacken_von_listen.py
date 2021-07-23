
liste = ["Peter", 22]
print(liste)
name, age = liste
print(name)
print(age)

# bei einer Liste kann dies zu einem Problem führen, wenn z.b die liste mehr daten enthält als ausgepackt werden
# liste.append("musterstraße")
# name, age = liste

tupel = ("Lisa", 23)
name, age = tupel
# da ein tupel nicht erweitert werden kann entstehen hier nach der erstellung weniger fehler

def person(int):
    return liste[int]

liste = [("Max", 21),
         ("Petra", 19),
         ("Lisa", 23)]

name, age = person(1)

print(name)
print(age)