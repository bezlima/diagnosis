from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db
from ..schemas import professional_schema
from ..services import professional_services
from sqlalchemy.exc import SQLAlchemyError
from ..auth.dependencie.auth_dependencie import get_current_user
from ..utils.verify_permission import verify_permission
from typing import List
import logging

logger = logging.getLogger(__name__)

professional_router = APIRouter(tags=["Professionals"], prefix='/professionals')

@professional_router.post('/', response_model=List[professional_schema.ProfessionalResponse], status_code=201)
def create_professional(professional: professional_schema.ProfessionalCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        new_professional = professional_services.create_professional(db, professional)

        if not permission.create_professional: 
            raise HTTPException(status_code=401, detail="Unauthorized professional")

        return new_professional
    
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Database error"
        ) from e
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        ) from e

@professional_router.get('/', response_model=List[professional_schema.ProfessionalResponse], status_code=200)
def get_professionals(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        professionals = professional_services.get_professionals(db)

        if not permission.get_all_professionals: 
            raise HTTPException(status_code=401, detail="Unauthorized professional")
         
        return professionals
    
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Database error"
        ) from e
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        ) from e

@professional_router.get('/{professional_id}', status_code=200)
def get_professional_by_id(professional_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        professional = professional_services.get_professional_by_id(db, professional_id)

        if not permission.get_all_professionals:
            if not current_professional.professional_id == professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        return professional
    
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Database error"
        ) from e
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        ) from e


@professional_router.put('/{professional_id}', status_code=202)
def update_professional(professional_id: int, update_infos: professional_schema.UpdateProfessional, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        update_professional = professional_services.update_professional(db, professional_id, update_infos)

        if not permission.get_all_professionals:
            if not current_professional.professional_id == professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if not permission.edit_professional:
            if not current_professional.professional_id == professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")

        return update_professional
    
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Database error"
        ) from e
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        ) from e

@professional_router.delete('/{professional_id}', status_code=204)
def delete_professional(professional_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        delete_professional = professional_services.delete_professional(db, professional_id)
        
        if not permission.get_all_professionals:
            if not current_professional.professional_id == professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        if not permission.delete_professional:
            if not current_professional.professional_id == professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        return delete_professional
    
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Database error"
        ) from e
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        ) from e