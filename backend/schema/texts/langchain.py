from pydantic import BaseModel, EmailStr, Field
from .base import (
    BaseAddress, 
    BaseSchoolInfo, 
    BaseEmployementHistory,
    BaseQualification)

class GetClientInfo(BaseModel):
    "Get the job seeker's information from a given text"
    name:str =Field(..., description="求職者の名前")
    phonetic_character:str = Field(..., description="求職者のフリガナ")
    age:int= Field(..., description="求職者の年齢")
    gender:str= Field(..., description="求職者の性別")
    phone_number:int = Field(..., description="求職者の電話番号")
    email:EmailStr = Field(..., description="求職者のメールアドレス")
    full_address: BaseAddress = Field(..., description="求職者の住所")
    full_school_info: list[BaseSchoolInfo]= Field(..., description="求職者の学歴")
    full_employement_history:list[BaseEmployementHistory] = Field(..., description="求職者の職歴")
    full_qualifications:list[BaseQualification] = Field(..., description="求職者の資格")
    Married: bool = Field(..., description="求職者が結婚しているか")
    support_obligation:bool = Field(..., description="求職者に扶養義務があるか")
    family_member:int = Field(..., description="求職者の扶養家族人数")
    self_introduction:list[str] = Field(..., description="求職者の自己PR")
