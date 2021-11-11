# JSON Format ist eines der wichtigsten formate, dieses format findet auch anwendung in der entwicklung mit REST

# eine JSON Datei ist kurzgesagt nichts anderes als ein Dictionary das aus key value paaren besteht,
# dieses wird in einer .json gespeichert


# in json sind keine kommentar blöcke erlaubt hier muss man sich mit einem passenden key:value paar aushelfen

import json

# Lesen von Json files

with open("../Materialien/test_json_read.json", "r") as json_file:
    people_dict = json.load(json_file)
    print(people_dict)

    for index, people in enumerate(people_dict.get("people")):
        name = people.get("firstName")
        if name.lower() == "james":
            replace_person = {'firstName': 'Maria', 'lastName': 'Hansen', 'gender': 'female', 'age': 22,
                              'number': '4568956564'}

            people_dict.get("people")[index] = replace_person

    print(people_dict)

# write json file
with open("../Materialien/test_json_write.json", "w") as json_file:
    json.dump(people_dict, json_file)

dictionary = {"lakes":
    [
        {
            "name": "Froglake",
            "kords": [45.21940446638516, -121.69440878540168],
            "comment": "Der Frosch See, Quak"
        },
        {
            "name": "Lost Lake",
            "kords": [45.49040839503808, -121.8224018732182]
        },
        {
            "name": "Frost Lake",
            "kords": [44.989087175716264, -93.04019921375355]
        }
    ]
}

with open("../Materialien/test_json_write.json", "w") as json_file:
    json.dump(dictionary, json_file)
