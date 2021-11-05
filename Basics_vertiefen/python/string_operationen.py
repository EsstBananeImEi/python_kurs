# Was strings sind wissen wir schon,
# aber das man auf strings weitere Funktionen anwenden kann noch nicht, hier sind ein paar

text = "   Willkommen, hier ist ein Text   "

# strip(): entfernt leerzeichen am anfang und ende eines Strings
print("\n#### strip #####")
print(text)
text = text.strip()
print(text)

# lower(): der String wird kleingeschieben
print("\n#### lower #####")
print(text.lower())

# upper(): der String wird großgeschieben
print("\n#### upper #####")
print(text.upper())

# index() / find(): sucht ein bestimmten zeichenfolge in einem String und
# gibt die position aus an dem die zeichenfolge startet
print("\n#### index / find #####")
print(text.index("ist"))
print(text.find("ist"))

# string -> list
# split(): zerteilt einen string entweder nach jedem word oder an einer definierten zeichenfolge
print("\n#### split #####")
print(text.split())
print(text.split(","))

# replace(): ersetzt eine zeichenfolge in einem String durch eine andere
# dies kann durch angabe von positionen auf mehrere treffer oder alle treffer ausgeweitet werden
print("\n#### replace #####")
print(text.replace("Willkommen", "Auf Wiedersehen"))
print(text.replace("i", "?"))
print(text.replace("i", "#", 2))

# list -> str
# join()
# Mit der join methode können wir Strings aus listen ganz einfach verketten
print("\n#### join #####")
liste = text.split()
print(" ".join(liste))
print(" ".join(liste[:-2]))
print(" ".join(liste[-2]))


