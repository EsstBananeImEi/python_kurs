"""
    Datentypen können geändert werden, dies nennt man auch casten, mit dem casten sagt man bsp. mache aus der Zahl 1 einen String
"""

# String -> Zahl
a = "3"
b = "7"
print(int(a) + int(b))
# Zahlt -> String
alter = 18
print("Ich bin " + str(alter) + " Jahre alt")

# String -> Float (Gleitkommazahl)
preis = "49.99"
mwst = "0.16"
print(float(preis) * float(mwst))

# Float -> Int
preis = 49.99
mwst = 0.16
print(int(preis) * int(mwst))
print(int(preis))
print(int(mwst))
