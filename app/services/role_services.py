from sqlalchemy.orm import Session
from ..models import role_model
from ..schemas import role_schema

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    roles = db.query(role_model.Role).offset(skip).limit(limit).all()
    return roles

def get_role_by_id(db: Session, role_id: int):
    role = db.query(role_model.Role).filter(role_model.Role.role_id == role_id).first()
    return role

def get_role_by_name(db: Session, role_name: str):
    role = db.query(role_model.Role).filter(role_model.Role.role_name == role_name).first()
    return role

def get_role_by_id(db: Session, role_id: int):
    role = db.query(role_model.Role).filter(role_model.Role.role_id == role_id).first()
    return role

def update_role(db: Session, role_id: int, update_infos: role_schema.RoleBase):
    role = db.query(role_model.Role).filter(role_model.Role.role_id == role_id).first()
    if role:
        update_data = update_infos.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(role, key, value)
        db.commit()
        db.refresh(role)
        return True
    return False

def delete_role(db: Session, role_id: int):
    role = db.query(role_model.Role).filter(role_model.Role.role_id == role_id).first()
    if role:
        db.delete(role)
        db.commit()
        return True
    return False

def create_role(db: Session, role: role_model.Role):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role