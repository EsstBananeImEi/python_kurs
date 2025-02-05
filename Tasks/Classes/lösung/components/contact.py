from dataclasses import dataclass
from components.address import Address


@dataclass
class ContactInfo:
    address: Address
    phone_number: str
    mobile_number: str
    email: str

    def __str__(self) -> str:
        return (
            f"{self.address}, {self.phone_number}, {self.mobile_number}, {self.email}"
        )
