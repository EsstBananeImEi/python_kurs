# Bisher haben wir in variablen nur einen wert gespeichert, nun stelle ich dir Listen vor
# Listen sind eine art Container in denen man Daten bzw. Objekte speichern kann

# umstaendlich
person1 = "Peter"
person2 = "Marie"
person3 = "Gabi"
person4 = "Max"
person5 = "Paul"


liste_mit_personen = ["Max", "Peter", "Marie", "Gabi"]

print(liste_mit_personen)
print(len(liste_mit_personen))
print("#########")

liste_mit_numbers = [1, 4, 5, 3, 8]
print(liste_mit_numbers)
print("#########")

liste_mit_verschiedenen_typen = [1, "Peter", 8.9, object]
print(liste_mit_verschiedenen_typen)
print("#########")

print("Es befinden sich "+ str(len(liste_mit_personen)) + " Personen in der liste")
liste_mit_personen.append("Tina")
liste_mit_personen.append("Karl")
print("Es befinden sich "+ str(len(liste_mit_personen)) + " Personen in der liste")
print(liste_mit_personen)
print("#########")

liste_mit_personen.remove("Peter")
print(liste_mit_personen)
print("#########")

# in der informatik fängt man immer bei 0 an zu Zählen d.h position 0 ist das erste element
print(liste_mit_personen[0])
print(liste_mit_personen[2])
print("#########")

print(liste_mit_personen[0] + " und " + liste_mit_personen[2] + " sind Freunde")
print("#########")

liste_mit_personen[1] = "Beacon"
print(liste_mit_personen)
