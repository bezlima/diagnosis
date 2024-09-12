from sqlalchemy import Column, String, Integer, ForeignKey
from ..db.db import Base

class APIKey(Base):
    __tablename__ = 'api_keys'

    api_key_id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True, nullable=False)
    owner = Column(String, nullable=False)
    contact = Column(String, nullable=False)