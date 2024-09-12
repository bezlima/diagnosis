from sqlalchemy import Boolean, Column, Integer, String
from ..db.db import Base

class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String, index=True)

    create_role = Column(Boolean)
    get_your_role = Column(Boolean)
    get_all_roles = Column(Boolean)
    edit_role = Column(Boolean)
    delete_role = Column(Boolean)

    create_professional = Column(Boolean)
    get_all_professionals = Column(Boolean)
    edit_professional = Column(Boolean)
    delete_professional = Column(Boolean)

    create_report = Column(Boolean)
    get_your_report = Column(Boolean)
    get_all_reports = Column(Boolean)
    edit_report= Column(Boolean)
    delete_report= Column(Boolean)

    create_client = Column(Boolean)
    get_your_client = Column(Boolean)
    get_all_clients = Column(Boolean)
    edit_client = Column(Boolean)
    delete_client = Column(Boolean)

    create_pdf = Column(Boolean)
