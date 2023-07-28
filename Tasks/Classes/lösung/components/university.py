from dataclasses import dataclass


@dataclass
class StudyInfo:
    field_of_study: str
    graduation_year: int
    gpa: float
    degree: str

    def __str__(self) -> str:
        return f"{self.degree}, {self.field_of_study}, {self.graduation_year}, {self.gpa}"        

@dataclass
class University:
    university: str
    university_address_line1: str
    university_address_line2: str
    university_city: str
    university_state: str
    university_country: str
    university_postal_code: str
    university_phone: str
    university_website: str
    study_info: StudyInfo

    def __str__(self) -> str:
        return f"{self.university_address_line1}, {self.university_address_line2}, {self.university_city}, {self.university_state}, {self.university_country}, {self.university_postal_code}"
