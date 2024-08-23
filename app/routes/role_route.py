from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db

role_router = APIRouter()

@role_router.post('/role')
def create_role(role: int, db: Session = Depends(get_db)):
    return

@role_router.get('/role')
def get_roles():
    return

@role_router.get('/role/{role_id}')
def get_role_by_id():
    return

@role_router.put('/role/{role_id}')
def update_role():
    return

@role_router.delete('/role/{role_id}')
def delete_role():
    return