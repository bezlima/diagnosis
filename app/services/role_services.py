from sqlalchemy.orm import Session
from ..models import role_model
from ..schemas import role_schema

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    roles = db.query(role_model.Roles).offset(skip).limit(limit).all()
    return roles

def get_role(db: Session, role_id: int):
    role = db.query(role_model.Roles).filter(role_model.Roles.role_id == role_id)
    return role

def update_role(db: Session, role_id: int, update_infos: role_schema.RoleBase):
    role = db.query(role_model.Roles).filter(role_model.Roles.role_id == role_id)

    if role:
        role.create_role = update_infos.create_role
        role.edit_role = update_infos.edit_role
        role.delete_role = update_infos.delete_role
        role.get_all_roles = update_infos.get_all_roles
        role.get_all_users = update_infos.get_all_users
        role.edit_all_user = update_infos.edit_all_user
        role.delete_all_user = update_infos.delete_all_user
        role.get_all_reports = update_infos.get_all_reports
        role.edit_all_reports = update_infos.edit_all_reports
        role.delete_all_reports = update_infos.delete_all_reports

        db.commit()
        db.refresh(role)

        return True
    
    return False

def delete_role(db: Session, role_id: int):
    role = db.query(role_model.Roles).filter(role_model.Roles.role_id == role_id)
    if role:
        db.delete(role)
        db.commit()
        return True
    return False

def create_role(db: Session, role: role_schema.RoleBase):
    db.add(role)
    db.connection()
    db.refresh(role)
    return role