from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db.db import Base

class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    address = Column(String)
    name = Column(String)
    age = Column(Integer)
    client_document_RG = Column(String, unique=True)
    client_document_CPF = Column(String, unique=True)
    professional_id = Column(Integer, ForeignKey('professionals.professional_id'))