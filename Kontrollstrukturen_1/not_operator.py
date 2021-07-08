# Mit dem logischen Operator not lässt sich das Resultat in das Gegenteil verkehren:

print(3 not in [1, 2, 3])

a = True

print(a == True)
print(not a == True)

a = 4
b = 5

print(not a == b)

# Achtung Fehlergefahr: Auch wenn die Schreibweise not in x am natürlichen Sprachgebrauch ist,
# ist dieses Kontrukt mit einem Fallstrick versehen.
# Bei der Verwendung von not in Kombination mit den logischen Operatoren and und or wird not
# an die zweite Position gesetzt. In Kombination mit dem Teilmengenoperator steht das not an erster Stelle.
#
# not in
#
# and not
# or not

print(a not in [1, 2, 3])
print(a not in [1, 2, 3] and not 5 in [1, 2, 3, 4, 5])
print(a not in [1, 2, 3, 4] or not 5 in [1, 2, 3, 4])
