# Dictionarys können wie listen durchlaufen werden

kennzeichen = {"Köln": "K", "Koblenz": "KO", "München": "M", "Feuchtwangen": "FEU"}

for key in kennzeichen:
    value = kennzeichen[key]
    print(key)
    print(value)

print(kennzeichen.items())

for key, value in kennzeichen.items():
    print("%s : %s" % (key, value))