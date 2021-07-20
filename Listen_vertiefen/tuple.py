# Listen und Tupels sind beides Listen, der wesentliche unterschied ist, das Tupels nicht veränderbar (Immutable) sind,
# sie können also nach ihrer erstellung nicht mehr verändert werden

liste = [1, 2, 3, 4]
print(liste)
tupel = (1, 2, 3, 4)
print(tupel)

liste[0] = "Dienstag"
print(liste)

