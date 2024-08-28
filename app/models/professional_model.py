from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db.db import Base

class Professional(Base):
    __tablename__ = "professionals"

    professional_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    professional_document_RG = Column(String)
    professional_document_CPF = Column(String)
    professional_document_type = Column(String)
    professional_document = Column(String, unique=True, index=True)
    address = Column(String)
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    role = relationship("Role") 
    hashed_password = Column(String)
