# Mit dem Teilmengenoperator in wird überprüft, ob ein Objekt Teilmenge eines anderen Objekts ist. Hier prüfen wir, ob sich der Wert 3 in der Liste [1,2,3] befindet:

print(3 in [1, 2, 3])

liste = ["hallo", "welt"]

print("welt" in liste)

if "lo" in liste:
    print("lo ist drin")

text = "Dies ist ein Test Text"

if "ist" in text:
    print("'ist' ist drin")

if "xt" in text:
    print("'xt' ist drin")

a = [1, 2, 3, 4, 5, 6]
if 4 in a:
    print("zahl vorhanden")

a = {"numbers": [],
     "strings": [],
     "booleans": []}

if "strings" in a:
    print("ist im dict")
