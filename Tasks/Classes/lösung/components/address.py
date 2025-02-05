from dataclasses import dataclass


@dataclass
class Address:
    address_line1: str
    address_line2: str
    city: str
    state: str
    country: str
    postal_code: str

    def __str__(self) -> str:
        return f"{self.address_line1}, {self.address_line2}, {self.city}, {self.state}, {self.country}, {self.postal_code}"
