""" Guards

Guards sind Boolische Ausdrücke mit denen wir Verschachtelte Klauseln ersetzen können,
um code von den "Bedingungen aus der Hölle" zu befreien. 
Dies wird in einigen Kreisen so bezeichnet da die Einrückungen jeder Ebene einer Verschachtelung einen Pfeil bilden, 
der nach rechts in Richtung Schmerz und Leid zeigt

```Python
def conditional_from_hell() -> None:
    if condition: 
        if condition:
            # not good
            do someting...
            if condition:
                # Dooh
                if condition
                    # painful
                    if condition
                        # Entrance to hell
            while True:
                ...
    else 
        do something
```
"""

"""
Problem

Du hast eine Gruppe von verschachtelten Konditionen und es ist schwer, den normalen Ablauf der Codeausführung zu bestimmen.
"""


def do_some_json_stuff(data) -> str:
    return f"Sensor Data: {data.get('sensor_data')}"


import json
import os


def read_json_data_without_guards(file_path: str) -> str:
    if os.path.isfile(file_path):
        try:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
                if "sensor_data" in data:
                    return do_some_json_stuff(data)
                else:
                    return f"{file_path} enthält keine passenden Daten"
        except Exception as ex:
            return f"{file_path} ist kein JSON"
    else:
        return f"{file_path} ist keine Datei"


"""
Lösung

Alle Sonderprüfungen und Randfälle werden in separaten Klauseln isoliert und stehen vor den Hauptprüfungen. 
Im Idealfall sollte eine "flache" Strucktur entstehen, in der eine Klausel nach der anderen kommt.
"""

import json
import os


def read_json_data_with_guards(file_path: str) -> str:
    data = None
    if not os.path.isfile(file_path):
        return f"{file_path} ist keine Datei"

    if not validate_json(file_path):
        return f"{file_path} ist kein JSON"

    data = json.load(open(file=file_path, encoding="utf-8"))

    if not "sensor_data" in data:
        return f"{file_path} enthält keine passenden Daten"

    return do_some_json_stuff(data)


def validate_json(json_file) -> bool:
    try:
        json.load(open(file=json_file, encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return True


if __name__ == "__main__":
    os.chdir(os.sep.join([os.path.dirname(os.path.abspath(__file__))]))

    print(read_json_data_without_guards("../jupyter/data.json"))
    print(read_json_data_with_guards("../jupyter/data.json"))
