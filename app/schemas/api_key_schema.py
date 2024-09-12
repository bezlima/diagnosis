from pydantic import BaseModel

class ApiKeyBase(BaseModel):
    key : str
    owner : str
    contact : str

class ApiKeyCreate(BaseModel):
    owner : str
    contact : str

class ApiKey(ApiKeyBase):
    apy_key_id: int

    class Config:
        from_attributes = True