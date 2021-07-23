# Nehmen wir an wir wollen in Disco und brauchen ein kleines programm was das alter einer person prüft
# und entscheidet wer rein darf und wer nicht. Sagen wir mal die disco hat eine Party in der nur
# Person zwischen 18 und 30 hineindürfen damit könnte man folgendes machen.

mindestalter = 18
maximales_alter = 30
alter = 25

if alter >= mindestalter and alter <= maximales_alter:
    print("Die Person Darf hinein, da sie zwischen 18 und 30 jahren ist")

alter = 17
if alter < mindestalter or alter >= maximales_alter:
    print("Die Person Darf nicht hinein, weil sie auserhalb der alters grenzen ist")

ist_alt_genug = 30 >= 18
print(ist_alt_genug)

drunken = True
age = 25
if mindestalter <= age <= maximales_alter or drunken == False:
    print("Die Person ist alt genug und nicht betrunken")

drunken = False
age = 12
if drunken == False or age >= mindestalter and age <= maximales_alter:
    print("die person kommt rein")

print("\n##################")
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("\n##################")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("\n##################")
land = "US"
alter = 20
if (land == "US" and alter >= 21) or (land != "US" and alter >= 18):
    print("er darf alkohol trinken")

