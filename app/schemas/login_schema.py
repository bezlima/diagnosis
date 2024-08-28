from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    email: str = Field(
        ...,
        description="Endereço de e-mail do profissional",
        example="example@diagnosis.com"
    )
    password: str = Field(
        ...,
        description="Senha do profissional",
        example="example123"
    )

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    email: str
    professional_id: int
    role_id: int