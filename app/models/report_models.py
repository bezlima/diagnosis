from sqlalchemy import String, Column, Integer, ForeignKey, Text
from ..db.db import Base

class Report(Base):
    __tablename__ = "reports"

    report_id = Column(Integer, primary_key=True)
    professional_id = Column(Integer, ForeignKey('professionals.professional_id'))
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    title = Column(String)
    content = Column(Text)