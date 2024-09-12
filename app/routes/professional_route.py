from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db
from ..schemas import professional_schema
from ..services import professional_services
from sqlalchemy.exc import SQLAlchemyError
from typing import List
import logging

logger = logging.getLogger(__name__)

professional_router = APIRouter(tags=["Professionals"], prefix='/professionals')

#rotas deve receber professional id para verificar se tem permissão para x
#adicionar http status_code=200 nas rotas

@professional_router.post('/', response_model=List[professional_schema.ProfessionalResponse])
def create_professional(professional: professional_schema.ProfessionalCreate, db: Session = Depends(get_db)):
    try:
        new_professional = professional_services.create_professional(db, professional)
        
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

@professional_router.get('/', response_model=List[professional_schema.ProfessionalResponse])
def get_professionals(db: Session = Depends(get_db)):
    try:
        professionals = professional_services.get_professionals(db)
        
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

@professional_router.get('/{professional_id}')
def get_professional_by_id(professional_id: int, db: Session = Depends(get_db)):
    try:
        professional = professional_services.get_professional_by_id(db, professional_id)
        
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


@professional_router.put('/{professional_id}')
def update_professional(professional_id: int, update_infos: professional_schema.UpdateProfessional, db: Session = Depends(get_db)):
    try:
        update_professional = professional_services.update_professional(db, professional_id, update_infos)
        
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

@professional_router.delete('/{professional_id}')
def delete_professional(professional_id: int, db: Session = Depends(get_db)):
    try:
        delete_professional = professional_services.delete_professional(db, professional_id)
        
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