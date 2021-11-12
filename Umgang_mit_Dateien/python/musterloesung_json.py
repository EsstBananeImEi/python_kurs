# 1.)
import json

person_without_car = None
oldest_car_owner = None
oldest_car_date = None
car_dict = {}


with open("../../Materialien/data.json", "r") as json_file:
    json_data = json.load(json_file)
    # 1
    person_without_car = [
        f"{person.get('first_name')} {person.get('last_name')}" for person in json_data.get('personen_wihout_car')]
    # 2
    for person in json_data.get('personen_with_car'):
        if oldest_car_date is None:
            oldest_car_date = person['car'].get('manufacture_year')
            oldest_car_owner = f"{person.get('first_name')} {person.get('last_name')}"
        if oldest_car_date > person['car'].get('manufacture_year'):
            oldest_car_date = person['car'].get('manufacture_year')
            oldest_car_owner = f"{person.get('first_name')} {person.get('last_name')}"
    # 3
        manufacturer = person['car'].get("manufacturer")
        if manufacturer not in car_dict:
            car_dict[manufacturer] = 1
        else:
            car_dict[manufacturer] += 1


for person in person_without_car:
    print(f"{person} besitzt kein Auto")

print("\n############################")
print(f"{oldest_car_owner}'s Auto ist das Älteste und wurde {oldest_car_date} gebaut")

print("\n############################")
for car_name, number_of_cars in car_dict.items():
    if car_name in ["BMW", "Jeep", "Dodge"]:
        print(f"{car_name}: {number_of_cars}")
