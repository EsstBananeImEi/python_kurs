"""
    Der Operator is prüft, ob zwei Variablen die gleiche Referenz
    auf ein Objekt aufweisen. Wie wir in dem Beispielcode sehen,
    ist das Resultat des is-Operators False, wenn lediglich der
    Wert zweier Variablen gleich ist
"""
a = [1, 2, 3]
b = [1, 2, 3]

print("\n##########")
print(a is b)
print(a == b)
print(id(a))
print(id(b))
print("\n##########")
c = a
print(c is a)
print(id(a))
print(id(c))
print("\n##########")

a = 2
b = 2
print(a is b)
