
# Slicing [1:] startet bei 1 bis zum ende
# Slicing [:3] startet bei 0 bis 3 aber die 3 wird ausgeschlossen
# Slicing [1:-1] startet bei 1 bis zum vorletzten

a = ["Linda", "Peter", "Henry", "Margot", "Sahra"]

print(a[1:-1])


# List Slicing funktioniert auch auf Strings, dies könnte zum beispiel nützlich sein um
# Teile von eingaben seperat zu betrachten

a = "Hallo Welt"
print(a[-4:])