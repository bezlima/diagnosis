from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db
from ..schemas import professional_schema
from ..services import professional_services
from sqlalchemy.exc import SQLAlchemyError
from typing import List

professional_router = APIRouter(tags=["Professionals"], prefix='/professionals')

#rotas deve receber professional id para verificar se tem permissão para x

@professional_router.post('/', response_model=List[professional_schema.ProfessionalResponse])
def create_professional(professional: professional_schema.ProfessionalCreate, db: Session = Depends(get_db)):
    return

@professional_router.get('/', response_model=List[professional_schema.ProfessionalResponse])
def get_professionals(db: Session = Depends(get_db)):
    try:
        professionals = professional_services.get_professionals(db)
        
        return professionals

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail="Database error"
        ) from e
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        ) from e

@professional_router.get('/{professional_id}')
def get_professional_by_id():
    return

@professional_router.put('/{professional_id}')
def update_professional():
    return

@professional_router.delete('/{professional_id}')
def delete_professional():
    return