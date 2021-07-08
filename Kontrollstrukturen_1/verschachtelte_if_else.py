# if / else anweisungen können auch tief verschachtelt sein, hier möchte ich euch zeigen wie dies aussieht


art_des_treffens = "Date"
personen = 2
blumen_gewuenscht = False
kerzen_gewuenscht = True
blumen_auf_tisch = False
kerze_auf_tisch = True

if personen > 2:
    print("Großen Tisch anbieten!")
else:
    print("Tisch für 2 anbieten!")
    if art_des_treffens == "Date":
        print("Frage nach Kerzen und Blumen")

        if blumen_gewuenscht:

            if blumen_auf_tisch:
                print("Blumen schon auf dem tisch")
            else:
                print("Stelle Blumen auf tisch")

        else:
            if blumen_auf_tisch:
                print("Blumen vom Tisch nehmen")
            else:
                print("Alles Ok, es sind keine Blumen auf dem Tisch")

        if kerzen_gewuenscht:

            if kerze_auf_tisch:
                print("kerze schon auf dem tisch")
            else:
                print("Stelle Kerze auf tisch")

        else:
            if kerze_auf_tisch:
                print("Kerzen vom Tisch nehmen")
            else:
                print("Alles Ok, es sind keine kerzen auf dem Tisch")

    else:
        print("Frage der Art des Treffens")
        print(".....")
