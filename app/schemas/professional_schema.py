from pydantic import BaseModel

class ProfessionalBase(BaseModel):
    email: str
    professional_document: str
    role_id: int

class ProfessionalCreate(ProfessionalBase):
    password: str

class UpdateProfessional(BaseModel):
    new_password: str

class Professional(ProfessionalBase):
    professional_id: int

    class Config:
        orm_mode = True