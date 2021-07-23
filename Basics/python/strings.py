"""
    - ein String (engl.: Kette, Folge) ist eine Zeichenkette so genannt, weil sie eine "Kette" von "Zeichen" enthält.
"""

print("Hallo Welt")
print(type("Hallo Welt"))

name = "Paul"
print("Mein Name ist " + name)
print("####")

# print("Ich bin " + 4 + "Jahre alt")  # Fehler da 4 kein string ist
print("Ich bin " + "4" + " Jahre alt")

alter = 6
# print("Ich bin " + alter + " Jahre alt") # Fehler da alter kein string ist sondern als integer festgelegt wurde
print("Ich bin " + str(alter) + " Jahre alt")
print("####")









