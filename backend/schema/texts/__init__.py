from pydantic import BaseModel, EmailStr
from .base import (
    BaseAddress, 
    BaseSchoolInfo,  
    BaseEmployementHistory,
    BaseQualification,
    BaseClientName
    )

class Client_Model_1(BaseModel):
    name:BaseClientName
    phonetic_character:str
    birth_date: str
    age:int
    gender:str
    phone_number:int
    email:EmailStr
    full_address: BaseAddress
    full_school_info: list[BaseSchoolInfo]
    full_employement_history:list[BaseEmployementHistory]
    full_qualifications:list[BaseQualification]
    Married: bool
    support_obligation:bool
    family_member:int
    self_introduction:list[str]



__all__ = [
    "Client_Model_1",
    ]