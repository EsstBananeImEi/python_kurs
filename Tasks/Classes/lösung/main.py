from functools import partial
from components import (
    Address,
    Company,
    ContactInfo,
    PersonStats,
    University,
    StudyInfo,
    Person,
    send_email,
    bmi,
    bmi_category,
)

SMTP_SERVER = "smtp.gmail.com"
PORT = 465
EMAIL_ADDRESS = "yourEmail@Adress.de"
EMAIL_PASSWORD = "yourPassword"


def main() -> None:
    # create company
    company = Company(
        company="Company Inc.",
        occupation="Software Engineer",
        company_email="compy@inc.com",
        company_phone="147-258-3692",
        company_address_line1="123 Company Street",
        company_address_line2="",
        company_city="New York",
        company_state="NY",
        company_country="USA",
        company_postal_code="10001",
        company_fax="147-258-5892",
        company_website="www.company.com",
    )

    # create university
    university = University(
        university="University of New York",
        university_address_line1="123 University Street",
        university_address_line2="",
        university_city="New York",
        university_state="NY",
        university_country="USA",
        university_postal_code="10001",
        university_phone="123456789",
        university_website="www.university.com",
        study_info=StudyInfo(
            degree="Master",
            field_of_study="Computer Science",
            graduation_year=2015,
            gpa=3.5,
        ),
    )

    # create stats
    stats = PersonStats(
        blood_type="A+",
        eye_color="brown",
        hair_color="brown",
        age=30,
        birthdate="01.01.1990",
        gender="Male",
        height=1.80,
        weight=80.0,
    )

    # create contact information
    contact_information = ContactInfo(
        address=Address(
            address_line1="123 Main Street",
            address_line2="",
            city="New York",
            state="NY",
            country="USA",
            postal_code="10001",
        ),
        phone_number="202-555-0131",
        mobile_number="+1 111-547-2589",
        email="test@person.de",
    )

    # create person
    person = Person(
        firstname="John",
        lastname="Doe",
        contact=contact_information,
        university=university,
        person_stats=stats,
        company=company,
    )

    # print personal information
    print(person.person_stats)

    if person.company:
        # print company information
        print(person.company)

        # print occupation information
        print(person.company.get_occupation())

    if person.university:
        # print university information
        print(person.university)

        # print study information
        print(person.university.study_info)

    # change email
    send_message = partial(
        send_email,
        smtp_server=SMTP_SERVER,
        port=PORT,
        from_address=EMAIL_ADDRESS,
        password=EMAIL_PASSWORD,
    )
    person.update_email("test@email.de", send_message)

    # change contact information
    send_message = partial(
        send_email,
        smtp_server=SMTP_SERVER,
        port=PORT,
        from_address=EMAIL_ADDRESS,
        password=EMAIL_PASSWORD,
    )
    person.update_contact_information(
        "555-123-4567", "+1 818-771-3482", "new@email.us", send_message
    )

    if person.person_stats:
        # compute bmi
        bmi_value = bmi(person.person_stats.weight, person.person_stats.height)
        print(f"Your BMI is {bmi_value:.2f}")
        print(f"Your BMI category is {bmi_category(bmi_value)}")


if __name__ == "__main__":
    main()
