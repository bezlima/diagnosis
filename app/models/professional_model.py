from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db.db import Base

class Professional(Base):
    __tablename__ = "professionals"

    professionals_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    professional_document = Column(String, unique=True, index=True)
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    role = relationship("Roles") 
    hashed_password = Column(String)
