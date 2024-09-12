from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..db.db_connect import get_db
from ..schemas import report_schema
from ..services import report_services
from ..models import report_models
import logging

logger = logging.getLogger(__name__)

report_router = APIRouter(tags=["Reports"], prefix='/report')

#rotas deve receber professional id para verificar se tem permissão para x
#adicionar http status_code=200 nas rotas

@report_router.post('/')
def create_report(report: report_schema.ReportBase , db: Session = Depends(get_db)):
    
    try:
        new_report = report_models.Report(**report.model_dump(exclude_unset=True))
        crate_report = report_services.create_report(db, new_report)

        return crate_report

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


@report_router.get('/all')
def get_reports(db: Session = Depends(get_db)):
    try:
        reports = report_services.get_reports(db)

        return reports

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


@report_router.get('/professional/{professional_id}')
def get_reports_by_professional(professional_id: int, db: Session = Depends(get_db)):
    try:
        reports = report_services.get_report_by_professional_id(db, professional_id)

        return reports

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
    
@report_router.get('/client/{client_id}')
def get_report_by_client(client_id: int, db: Session = Depends(get_db)):
    try:
        reports = report_services.get_report_by_client_id(db, client_id)

        return reports

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

@report_router.get('/{report_id}')
def get_report_by_id(report_id: int, db: Session = Depends(get_db)):
    try:
        report = report_services.get_report_by_id(db, report_id)

        return report

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

@report_router.put('/{report_id}')
def update_report(report_id: int, update_infos: report_schema.ReportBase, db: Session = Depends(get_db)):
    try:
        update_report = report_services.update_report(db, report_id, update_infos)

        return update_report

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

@report_router.delete('/{report_id}')
def delete_report(report_id: int, db: Session = Depends(get_db)):
    try:
        delete_report = report_services.delete_report(db, report_id)

        return delete_report

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