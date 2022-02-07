from abc import ABC, abstractmethod
import csv


def get_vehicle_id_list() -> list:
    vehicle_id_list = []
    with open("kennzeichen.csv", "r", encoding="UTF8") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=";").reader

        next(csvreader)
        for kennzeichen, name in csvreader:
            vehicle_id_list.append(kennzeichen)
    return vehicle_id_list


class VehicleInfo:

    def __init__(self, brand: str, electric: bool, catalogue_price: int) -> None:
        self.brand = brand
        self.is_electric = electric
        self.catalogue_price = catalogue_price

    def generate_tax(self) -> float:
        tax_percentage = 0.05
        if self.is_electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.generate_tax()}")
