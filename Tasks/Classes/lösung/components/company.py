from dataclasses import dataclass


@dataclass
class Company:
    company: str
    occupation: str
    company_email: str
    company_phone: str
    company_address_line1: str
    company_address_line2: str
    company_city: str
    company_state: str
    company_country: str
    company_postal_code: str
    company_fax: str
    company_website: str

    def __str__(self) -> str:
        return f"{self.company_address_line1}, {self.company_address_line2}, {self.company_city}, {self.company_state}, {self.company_country}, {self.company_postal_code}"

    def get_occupation(self):
        return f"{self.occupation}"

    def get_company_email(self):
        return f"{self.company_email}"

    def get_company_phone(self):
        return f"{self.company_phone}"
