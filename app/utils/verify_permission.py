from ..models.professional_model import Professional
from ..services import role_services, professional_services
from sqlalchemy.orm import Session

def verify_permission(professional : Professional, db: Session):
    
    professional_id = professional.professional_id

    current_professional_db = professional_services.get_professional_by_id(db, professional_id)

    role_id = current_professional_db.role_id

    role = role_services.get_role_by_id(db, role_id)

    return role