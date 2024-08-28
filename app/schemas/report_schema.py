from pydantic import BaseModel

class RoleBase(BaseModel):
    professional_id: int
    client_id: int
    title: str
    content: str

class Role(RoleBase):
    report_id: int

    class Config:
        from_attributes = True