from pydantic import BaseModel

class ProfessionalBase(BaseModel):
    email: str
    professional_document: str
    role_id: int
    name : str
    professional_document_RG : str
    professional_document_CPF : str
    professional_document_type : str
    professional_document : str
    address : str

class ProfessionalCreate(ProfessionalBase):
    password: str

class UpdateProfessional(BaseModel):
    new_password: str
    professional_document: str
    role_id: int
    name : str
    professional_document_RG : str
    professional_document_CPF : str
    professional_document_type : str
    professional_document : str
    address : str

class Professional(ProfessionalBase):
    professional_id: int

    class Config:
        orm_mode = True