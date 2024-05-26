from pydantic import BaseModel, Field

class BaseClientName(BaseModel):
    family_name: str = Field(..., description="クライアントの姓")
    first_name: str = Field(..., description="クライアントの名前")

class BaseAddress(BaseModel):
    postal_code:int = Field(..., description="郵便番号")
    address:str = Field(..., description="住所")
    phonetic_character:str = Field(..., description="住所のフリガナ")

class BaseSchoolInfo(BaseModel):
    school_name:str = Field(..., description="学校の名前")
    graduation_year:int = Field(..., description="卒業年")
    graduation_month:int = Field(..., description="卒業月")


class BaseEmployementHistory(BaseModel):
    company_name:str = Field(..., description="会社名")
    employement_style:str = Field(..., description="雇用形態")
    job_position:str = Field(..., description="職種・ポジション")
    year_started:int = Field(..., description="入社年")
    month_started:int = Field(..., description="入社月")
    year_ended:int = Field(..., description="退職年")
    month_ended:int = Field(..., description="退職月")
    task_detail:list[str] = Field(..., description="担当業務")

class BaseQualification(BaseModel):
    name:str = Field(..., description="資格の名前")
    month_obtained:int = Field(..., description="資格を取得した月")
    year_obtained:int = Field(..., description="資格を取得した年")

