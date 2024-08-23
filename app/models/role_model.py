from sqlalchemy import Boolean, Column, Integer
from ..db.db import Base

class Roles(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    create_role = Column(Boolean, index=True)
    edit_role = Column(Boolean, index=True)
    delete_role = Column(Boolean, index=True)
    get_all_roles = Column(Boolean, index=True)
    get_all_users = Column(Boolean, index=True)
    edit_all_user = Column(Boolean, index=True)
    delete_all_user = Column(Boolean, index=True)
    get_all_reports = Column(Boolean, index=True)
    edit_all_reports= Column(Boolean, index=True)
    delete_all_reports= Column(Boolean, index=True)
