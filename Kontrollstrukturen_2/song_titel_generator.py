# Wir bauen ein kleinen generator der uns zufällig lied titel ausgibt :D

# Mit hilfe von Python können wir zufallszahlen generieren
import random

part_1 = ["Rock", "Dance", "Old", "I", "It's", "Loves"]
part_2 = ["With", "Like", "Just", "Wanna", "Still", "me Like"]
part_3 = ["you.", "a Hurricane", "a Singer", "Rock", "Rock and Roll", "a Rock"]

all_parts = [part_1,part_2,part_3]

text = []

for part in all_parts:
    zufall = random.randint(0, len(part) - 1)
    text.append(part[zufall])

print(" ".join(text))
