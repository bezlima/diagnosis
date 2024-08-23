from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db
from ..schemas import professional_schema

professional_router = APIRouter()

@professional_router.post('/professionals')
def create_professional(professional: professional_schema.ProfessionalCreate, db: Session = Depends(get_db)):
    return

@professional_router.get('/professionals')
def get_professionals():
    return

@professional_router.get('/professionals/{professional_id}')
def get_professional_by_id():
    return

@professional_router.put('/professionals/{professional_id}')
def update_professional():
    return

@professional_router.delete('/professionals/{professional_id}')
def delete_professional():
    return