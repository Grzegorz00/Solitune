# schemas/schemas.py
from pydantic import BaseModel
from enum import Enum
from pydantic.fields import Field


class Education(Enum):
    Masters = "Masters"
    Bachelors = "Bachelors"

class Gender(Enum):
    Female = "Female"
    Male = "Male"

class EverBenched(Enum):
    Yes = "Yes"
    No = "No"

class Employee(BaseModel):
    education: Education
    # "education".title()
    gender: Gender
    ever_benched: EverBenched = Field(alias="everBenched")