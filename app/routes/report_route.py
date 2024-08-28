from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db

report_router = APIRouter(tags=["Reports"])

#rotas deve receber professional id para verificar se tem permissão para x

@report_router.post('/report')
def create_report(report_id: int, db: Session = Depends(get_db)):
    return

@report_router.get('/report')
def get_reports():
    return

@report_router.get('/report/{report_id}')
def get_report_by_id():
    return

@report_router.put('/report/{report_id}')
def update_report():
    return

@report_router.delete('/report/{report_id}')
def delete_report():
    return