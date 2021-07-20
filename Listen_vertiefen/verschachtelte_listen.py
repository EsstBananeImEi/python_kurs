# Listen können in jeglicher form miteinander verschachtelt werden

liste = [["Bulgarien", "Deutschland", "Finnland"],
         ["Albanien", "Serbien", "Ukraine"]]

print(liste[0][1])


countries = {"EU-Countries": ["Bulgarien", "Deutschland", "Finnland"],
             "Non-EU-Countries": ["Albanien", "Serbien", "Ukraine"]}

print(countries.get("EU-Countries"))
print(countries.get("Non-EU-Countries"))