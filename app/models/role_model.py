from sqlalchemy import Boolean, Column, Integer, String
from ..db.db import Base

class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String, index=True)

    create_role = Column(Boolean)
    edit_role = Column(Boolean)
    delete_role = Column(Boolean)
    get_all_roles = Column(Boolean)

    create_professionals = Column(Boolean)
    get_all_professionals = Column(Boolean)
    edit_all_professional = Column(Boolean)
    delete_all_professional = Column(Boolean)

    create_report = Column(Boolean)
    get_all_reports = Column(Boolean)
    edit_all_reports= Column(Boolean)
    delete_all_reports= Column(Boolean)

    create_clients = Column(Boolean)
    get_all_clients = Column(Boolean)
    edit_all_client = Column(Boolean)
    delete_all_client = Column(Boolean)
