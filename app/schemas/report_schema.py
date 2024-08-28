from pydantic import BaseModel

class ReportBase(BaseModel):
    professional_id: int
    client_id: int
    title: str
    content: str

class Report(ReportBase):
    report_id: int

    class Config:
        from_attributes = True