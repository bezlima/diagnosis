from sqlalchemy.orm import Session
from ..models import professional_model
from ..utils.hash_password import decrypt_password

def verify_password(db: Session, email: str, password: str) -> bool:
    professional = db.query(professional_model.User).filter(professional_model.User.email == email).first()
    if professional:
        if decrypt_password(password, professional.hashed_password):
            return True
    return False
