from dataclasses import dataclass
from email.message import EmailMessage
from smtplib import SMTP_SSL

SMTP_SERVER = "smtp.gmail.com"
PORT = 465
EMAIL_ADDRESS = "yourEmail@Adress.de"
EMAIL_PASSWORD = "yourPassword"


@dataclass
class Person:
    firstname: str
    lastname: str
    middlename: str
    birthdate: str
    age: int
    address_line1: str
    address_line2: str
    city: str
    state: str
    country: str
    postal_code: str
    phone_number: str
    mobile_number: str
    email: str
    gender: str
    height: float
    weight: float
    blood_type: str
    occupation: str
    company: str
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
    university: str
    degree: str
    field_of_study: str
    graduation_year: int
    gpa: float
    university_address_line1: str
    university_address_line2: str
    university_city: str
    university_state: str
    university_country: str
    university_postal_code: str
    university_phone: str
    university_website: str
    blood_type: str
    eye_color: str
    hair_color: str

    def get_full_name(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"

    def get_full_address(self):
        return f"{self.address_line1}, {self.address_line2}, {self.city}, {self.state}, {self.country}, {self.postal_code}"

    def get_full_company_address(self):
        return f"{self.company_address_line1}, {self.company_address_line2}, {self.company_city}, {self.company_state}, {self.company_country}, {self.company_postal_code}"

    def get_full_university_address(self):
        return f"{self.university_address_line1}, {self.university_address_line2}, {self.university_city}, {self.university_state}, {self.university_country}, {self.university_postal_code}"

    def get_full_company_info(self):
        return f"{self.company}, {self.company_email}, {self.company_phone}, {self.company_fax}, {self.company_website}"

    def get_full_university_info(self):
        return f"{self.university}, {self.degree}, {self.field_of_study}, {self.graduation_year}, {self.gpa}, {self.university_phone}, {self.university_website}"

    def get_full_personal_info(self):
        return f"{self.weight},{self.height},{self.hair_color},{self.eye_color},{self.blood_type},{self.birthdate},{self.gender}"

    def get_full_contact_info(self):
        return f"{self.phone_number}, {self.mobile_number}, {self.email},{self.company_email}"

    def get_full_education_info(self):
        return f"{self.university},{self.degree},{self.field_of_study},{self.graduation_year},{self.gpa},{self.university_phone},{self.university_website}"

    def get_bmi(self):
        return self.weight / (self.height * self.height)

    def get_bmi_category(self):
        bmi = self.get_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    def update_email(self, email: str) -> None:
        self.email = email

        message = EmailMessage()
        message.set_content(
            f"Hi {self.firstname},\n\nWe're writing to let you know that your email address has been updated to {self.email}.\n"
            "If you did not request this change, please contact us immediately.\n\nThanks,\n\nThe Team"
        )
        message["Subject"] = "Your email address has been updated"
        message["To"] = self.email

        with SMTP_SSL(SMTP_SERVER, PORT) as server:  # type: ignore
            # server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            # server.send_message(message)
            pass
        print(f"Email sent to {self.email}")

    def update_contact_information(
        self, phone_number: str, mobile_number: str, email: str
    ) -> None:
        self.phone_number = phone_number
        self.email = email
        self.mobile_number = mobile_number

        message = EmailMessage()
        message.set_content(
            f"Hi {self.firstname},\n\nWe're writing to let you know that your contact information has been updated to phone: {self.phone_number} mobile: {self.mobile_number} and email: {self.email}.\n"
            "If you did not request this change, please contact us immediately.\n\nThanks,\n\nThe Team"
        )
        message["Subject"] = "Your contact information has been updated"
        message["To"] = self.email

        with SMTP_SSL(SMTP_SERVER, PORT) as server:  # type: ignore
            # server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            # server.send_message(message)
            pass
        print(f"Email sent to {self.email}")


def main() -> None:
    person = Person(
        firstname="John",
        lastname="Doe",
        middlename="",
        birthdate="01.01.1990",
        age=30,
        address_line1="123 Main Street",
        address_line2="",
        city="New York",
        state="NY",
        country="USA",
        postal_code="10001",
        phone_number="202-555-0131",
        mobile_number="+1 818-771-3482",
        email="test@person.de",
        university="University of New York",
        degree="Master",
        field_of_study="Computer Science",
        graduation_year=2015,
        gpa=3.5,
        university_address_line1="123 University Street",
        university_address_line2="",
        university_city="New York",
        university_state="NY",
        university_country="USA",
        university_postal_code="10001",
        university_phone="123456789",
        university_website="www.university.com",
        company="Company Inc.",
        occupation="Software Engineer",
        company_email="company@inc.de",
        company_phone="123456789",
        company_address_line1="123 Company Street",
        company_address_line2="",
        company_city="New York",
        company_state="NY",
        company_country="USA",
        company_postal_code="10001",
        company_fax="123456789",
        company_website="www.company.com",
        gender="male",
        height=1.80,
        weight=80.0,
        blood_type="A+",
        eye_color="brown",
        hair_color="brown",
    )

    # print personal information
    print(f"Personal Info: {person.get_full_personal_info()}")

    # print contact information
    print(f"Contact Info: {person.get_full_contact_info()}")

    # print company information
    print(f"Company Info: {person.get_full_company_info()}")

    # print university information
    print(f"University Info: {person.get_full_university_info()}")

    # print university education
    print(f"Education Info: {person.get_full_education_info()}")

    # change email
    person.update_email("new@Test.us")

    # change contact information
    person.update_contact_information("555-135-1234", "+1 222-511-2345", "new@email.us")

    # compute bmi
    bmi = person.get_bmi()
    print(f"Your BMI is {bmi}")
    print(f"Your BMI category is {person.get_bmi_category()}")


if __name__ == "__main__":
    main()
