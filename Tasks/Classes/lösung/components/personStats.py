from dataclasses import dataclass
from functools import lru_cache


@lru_cache
def bmi(weight: float, height: float) -> float:
    return weight / (height**2)


def bmi_category(bmi_value: float) -> str:
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

@dataclass
class PersonStats:
    blood_type: str
    eye_color: str
    hair_color: str
    age: int
    gender: str
    height: float
    weight: float
    birthdate: str

    def __str__(self) -> str:
        return f"{self.weight}, {self.height}, {self.hair_color}, {self.eye_color}, {self.blood_type}, {self.birthdate}, {self.gender}"

