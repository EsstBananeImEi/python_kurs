# 1.)
import json

has_no_car_list = []
car_dict = {}

oldest_car_date = 2021
oldest_car_owner = ""

with open("../Materialien/data.json", "r") as json_file:
    json_content = json.load(json_file)
    for data in json_content:
        name = f"{data.get('first_name')} {data.get('last_name')}"
        for key, value in data.items():
            if key == "car":
                has_car = value["has_car"]
                if not has_car:
                    if name not in has_no_car_list:
                        has_no_car_list.append(f"{data.get('first_name')} {data.get('last_name')}")
                else:
                    # 2.)
                    date = value["manufacture_year"]
                    if date is None:
                        continue

                    if oldest_car_date > date:
                        oldest_car_date = date
                        oldest_car_owner = name
                    # 2.) ende

                    manufacturer = value["manufacturer"]
                    if manufacturer not in car_dict:
                        car_dict[manufacturer] = 1
                    else:
                        car_dict[manufacturer] += 1

for person in has_no_car_list:
    print(f"{person} besitzt kein Auto")

print("\n############################")
print(f"{oldest_car_owner}'s Auto ist das Älteste und wurde {oldest_car_date} gebaut")
#
print("\n############################")
for key, val in car_dict.items():
    if key in ["BMW", "Jeep", "Dodge"]:
        print(key + ": " + str(car_dict[key]))
