import csv


def get_vehicle_id_list() -> list:
    vehicle_id_list = []
    with open("kennzeichen.csv", "r", encoding="UTF8") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=";").reader

        next(csvreader)
        for kennzeichen, name in csvreader:
            vehicle_id_list.append(kennzeichen)
    return vehicle_id_list
