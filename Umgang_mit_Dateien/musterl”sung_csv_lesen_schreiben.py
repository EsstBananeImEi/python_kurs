d = {}

with open("../Materialien/bundesländer.csv", "r") as csvfile:
    for line in csvfile.readlines():
        splitted = line.strip().split(";")
        if "Bundesland" in splitted:
            continue

        federal_state = splitted[0]
        amount_of_people = int(splitted[1])
        growth = int(splitted[2][:-1])

        d[federal_state] = {"amount": amount_of_people,
                            "growth": growth}

amount = 0
name_max_citizen = ""
growth = 0
name_max_growth = ""

for key, value in d.items():
    if amount < value.get("amount"):
        amount = value.get("amount")
        name_max_citizen = key

    if growth < value.get("growth"):
        growth = value.get("growth")
        name_max_growth = key

print("%s hat mit %s Menschen die Meisten Einwohner" % (name_max_citizen, amount))
print("%s hat mit %s %% den meisten zuwachs" % (name_max_growth, growth))