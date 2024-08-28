from pydantic import BaseModel, Field

class ProfessionalBase(BaseModel):
    email: str = Field(
        ...,
        description="Endereço de e-mail do profissional",
        example="joao.silva@example.com"
    )
    professional_document: str = Field(
        ...,
        description="Número do documento do profissional",
        example="123456789"
    )
    role_id: int = Field(
        ...,
        description="ID do cargo do profissional",
        example=1
    )
    name: str = Field(
        ...,
        description="Nome completo do profissional",
        example="João da Silva"
    )
    professional_document_RG: str = Field(
        ...,
        description="Registro Geral (RG) do profissional",
        example="123456789"
    )
    professional_document_CPF: str = Field(
        ...,
        description="Cadastro de Pessoa Física (CPF) do profissional",
        example="123.456.789-00"
    )
    professional_document_type: str = Field(
        ...,
        description="Tipo de documento do profissional",
        example="RG"
    )
    address: str = Field(
        ...,
        description="Endereço do profissional",
        example="Rua A, 123"
    )

class ProfessionalCreate(ProfessionalBase):
    password: str = Field(
        ...,
        description="Senha do profissional",
        example="password123"
    )

class UpdateProfessional(BaseModel):
    new_password: str = Field(
        ...,
        description="Nova senha para o profissional",
        example="newpassword123"
    )
    professional_document: str = Field(
        ...,
        description="Número do documento do profissional",
        example="123456789"
    )
    role_id: int = Field(
        ...,
        description="ID do cargo do profissional",
        example=1
    )
    name: str = Field(
        ...,
        description="Nome completo do profissional",
        example="João da Silva"
    )
    professional_document_RG: str = Field(
        ...,
        description="Registro Geral (RG) do profissional",
        example="123456789"
    )
    professional_document_CPF: str = Field(
        ...,
        description="Cadastro de Pessoa Física (CPF) do profissional",
        example="123.456.789-00"
    )
    professional_document_type: str = Field(
        ...,
        description="Tipo de documento do profissional",
        example="RG"
    )
    address: str = Field(
        ...,
        description="Endereço do profissional",
        example="Rua A, 123"
    )

class ProfessionalResponse(BaseModel):
    professional_id: int
    name: str
    email: str
    professional_document_RG: str
    professional_document_CPF: str
    professional_document_type: str
    professional_document: str
    address: str
    role_id: int

class Professional(ProfessionalBase):
    professional_id: int = Field(
        ...,
        description="ID único do profissional",
        example=1
    )

    class Config:
        from_attributes = True
