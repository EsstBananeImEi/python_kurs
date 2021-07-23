# List Comprehentions auf Deutsch auch Listen-Abstraktion genannt, wird verwendet
# um Listen effektiv und mit wenig Code zu erstellen. Grundlage bilden hierbei immer andere
# iterierbare Objekte, wie Listen oder Dictionaries.

# Eine List Comprehention ist immer eine Liste, die einen Ausdruck,
# eine Schleife und ggf. noch weitere Schleifen oder Bedingungen enthält.

numbers = [1, 2, 3, 4, 5]

number_multiplied_by_2 = [zahl * 2 for zahl in numbers]
print(number_multiplied_by_2)

# Ohne List Comprehention
number_multiplied_by_2 = []
for x in numbers:
    number_multiplied_by_2.append(x * 2)
print(number_multiplied_by_2)

####################################################
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadiere = [x * x for x in liste]
print(quadiere)

# Ohne List Comprehention
quadiere = []
for x in liste:
    quadiere.append(x * x)
print(quadiere)

####################################################

# List Comprehention mit einer Bedingung
comprehention_with_expresion = [zahl * 2 for zahl in numbers if zahl % 2 == 0]
print(comprehention_with_expresion)


# List Comprehention mit mehreren for Schleifen
liste1 = [1, 2, 3]
liste2 = [3, 1, 4]

combined = [(zahl1, zahl2) for zahl1 in liste1 for zahl2 in liste2 if zahl1 != zahl2]
print(combined)

combined2 = []
for zahl1 in liste1:
    for zahl2 in liste2:
        if zahl1 != zahl2:
            combined2.append((zahl1,zahl2))
print(combined2)
