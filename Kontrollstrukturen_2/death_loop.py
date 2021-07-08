# Bei einer While Schleife gilt es zu beachten das aus dieser art von schleife eine Death loop werden kann.
# Denn man muss darauf achten das die Bedingung irgend wann einmal False wird sonst läuft die Schleife unentlich
# lang weiter, bis das Programm abstürzt


a = 0

while a >= 0:
    a += 1
    print(a)

print("ende")