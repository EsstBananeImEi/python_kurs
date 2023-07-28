from typing import Optional, Protocol
from dataclasses import dataclass
from components.contact import ContactInfo
from components.personStats import PersonStats
from components.university import University
from components.company import Company


class EmailSender(Protocol):
    def __call__(self, to_address: str, subject: str, content: str) -> None:
        ...


@dataclass
class Person:
    firstname: str
    lastname: str
    person_stats: Optional[PersonStats] = None
    contact: Optional[ContactInfo] = None
    middlename: Optional[str] = None
    university: Optional[University] = None
    company: Optional[Company] = None

    def get_full_name(self):
        return f"{self.firstname} {self.middlename if self.middlename else ''} {self.lastname}"

    def update_email(self, email: str, send_message: EmailSender) -> None:
        if self.contact is None:
            return
        self.contact.email = email

        send_message(
            to_address=self.contact.email,
            subject="Your email address has been updated",
            content=f"Hi {self.firstname},\n\nWe're writing to let you know that your email address has been updated to {self.contact.email}.\n"
            "If you did not request this change, please contact us immediately.\n\nThanks,\n\nThe Team",
        )

    def update_contact_information(
        self,
        phone_number: str,
        mobile_number: str,
        email: str,
        send_message: EmailSender,
    ) -> None:
        if self.contact is None:
            return
        self.contact.phone_number = phone_number
        self.contact.email = email
        self.contact.mobile_number = mobile_number

        send_message(
            to_address=self.contact.email,
            subject="Your contact information has been updated",
            content=f"Hi {self.firstname},\n\nWe're writing to let you know that your contact information has been updated to phone: {self.contact.phone_number} mobile: {self.contact.mobile_number} and email: {self.contact.email}.\n"
            "If you did not request this change, please contact us immediately.\n\nThanks,\n\nThe Team",
        )
