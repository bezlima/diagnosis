from sqlalchemy.orm import Session
from ..models import professional_model
from ..utils.hash_password import encrypt_password
from ..schemas import professional_schema

def get_professionals(db: Session, skip: int = 0, limit: int = 100):
    professional = db.query(professional_model.Professional).offset(skip).limit(limit).all()
    return professional

def get_professional(db: Session, professional_id: int):
    professional = db.query(professional_model.Professional).filter(professional_model.Professional.professional_id == professional_id).first()
    return professional

def get_professional_by_email(db: Session, email: str):
    professional = db.query(professional_model.Professional).filter(professional_model.Professional.email == email).first()
    return professional

def get_professional_by_id(db: Session, professional_id: str):
    professional = db.query(professional_model.Professional).filter(professional_model.Professional.professional_id == professional_id).first()
    return professional

def get_professional_by_documentid(db: Session, professional_document: str):
    professional = db.query(professional_model.Professional).filter(professional_model.Professional.professional_document == professional_document).first()
    return professional

def delete_professional(db: Session, professional_id: int):
    professional = db.query(professional_model.Professional).filter(professional_model.Professional.professional_id == professional_id).first()
    if professional:
        db.delete(professional)
        db.commit()
        return True
    return False

def update_professional(db: Session, professionals_id: int, update_infos: professional_schema.UpdateProfessional):
    professional = db.query(professional_model.Professional).filter(professional_model.Professional.professional_id == professionals_id).first()
    if professional:
        update_data = update_infos.model_dump(exclude_unset=True)
        if 'new_password' in update_data:
            update_data['hashed_password'] = encrypt_password(update_data.pop('new_password'))
        for key, value in update_data.items():
            setattr(professional, key, value)
        db.commit()
        db.refresh(professional)
        return professional
    return None

def create_professional(db: Session, professional: professional_schema.ProfessionalCreate):
    hashed_password = encrypt_password(professional.password)
    professional = professional_model.Professional(
        name = professional.name,
        email = professional.email, 
        professional_document_RG = professional.professional_document_RG,
        professional_document_CPF = professional.professional_document_CPF,
        professional_document_type = professional.professional_document_type,
        professional_document = professional.professional_document,
        address = professional.address,
        role_id = professional.role_id,
        hashed_password = hashed_password
    )
    db.add(professional)
    db.commit()
    db.refresh(professional)
    return professional