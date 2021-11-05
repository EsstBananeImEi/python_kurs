# Um Strings zu verketten gibt es verschiedene möglichkeiten
from string import Template

a = "Hello"
b = "World"

print("##### %-formatting #####")
string = "%s %s" % (a, b)
print(string)

name = "Max"
nachname = "Mustermann"
string = "Mein Vorname ist %s und mein Nachname ist %s" % (name, nachname)
print(string)

print("\n##### f-strings #####")
string = f"Mein Vorname ist {name} und mein Nachname ist {nachname}"
print(string)

liste = ["Marie", "Musterfrau"]
string = f"Mein Vorname ist {liste[0]} und mein Nachname ist {liste[1]}"
print(string)

print("\n##### Str.format() #####")
welt = "Welt"
program = "python"
print('Hallo {name}!Das ist {program}.'.format(name=welt, program=program))

print("\n##### Template Strings #####")
template_string = Template('Hallo $name! Das ist $program.')
print(template_string.substitute(name=name, program=program))
