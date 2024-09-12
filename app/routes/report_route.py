from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..db.db_connect import get_db
from ..schemas import report_schema
from ..services import report_services, client_service
from ..models import report_models
from ..auth.dependencie.auth_dependencie import get_current_user
from ..utils.verify_permission import verify_permission
import logging

logger = logging.getLogger(__name__)

report_router = APIRouter(tags=["Reports"], prefix='/report')

@report_router.post('/', status_code=201)
def create_report(report: report_schema.ReportBase , db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):  
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        new_report = report_models.Report(**report.model_dump(exclude_unset=True))
        crate_report = report_services.create_report(db, new_report)

        if not permission.create_report: 
            raise HTTPException(status_code=401, detail="Unauthorized professional")

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


@report_router.get('/all', status_code=200)
def get_reports(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        reports = report_services.get_reports(db)

        if not permission.get_all_reports: 
            raise HTTPException(status_code=401, detail="Unauthorized professional")

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

@report_router.get('/professional/{professional_id}', status_code=200)
def get_reports_by_professional(professional_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        reports = report_services.get_report_by_professional_id(db, professional_id)

        if not permission.get_all_reports: 
            if not permission.get_your_report: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_user.professional_id == reports[0].professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if not permission.get_all_professionals:
            if not current_professional.professional_id == professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")

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
    
@report_router.get('/client/{client_id}', status_code=200)
def get_report_by_client(client_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        reports = report_services.get_report_by_client_id(db, client_id)
        client = client_service.get_client_by_id(db, reports[0].client_id)

        if not permission.get_all_reports: 
            if not permission.get_your_report: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_user.professional_id == reports[0].professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        if not permission.get_all_clients:
            if not permission.get_your_client:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_professional.professional_id == client.professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")

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

@report_router.get('/{report_id}', status_code=200)
def get_report_by_id(report_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        report = report_services.get_report_by_id(db, report_id)
        client = client_service.get_client_by_id(db, report.client_id)

        if not permission.get_all_reports: 
            if not permission.get_your_report: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_user.professional_id == report.professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        if not permission.get_all_clients:
            if not permission.get_your_client:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_professional.professional_id == client.professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
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

@report_router.put('/{report_id}', status_code=202)
def update_report(report_id: int, update_infos: report_schema.ReportBase, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        update_report = report_services.update_report(db, report_id, update_infos)
        client = client_service.get_client_by_id(db, update_report.client_id)

        if not permission.edit_report:
            raise HTTPException(status_code=401, detail="Unauthorized professional")

        if not permission.get_all_reports: 
            if not permission.get_your_report: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_user.professional_id == update_report.professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        if not permission.get_all_clients:
            if not permission.get_your_client:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_professional.professional_id == client.professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")

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

@report_router.delete('/{report_id}', status_code=204)
def delete_report(report_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        delete_report = report_services.delete_report(db, report_id)
        client = client_service.get_client_by_id(db, delete_report.client_id)


        if not permission.delete_report:
            raise HTTPException(status_code=401, detail="Unauthorized professional")

        if not permission.get_all_reports: 
            if not permission.get_your_report: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_user.professional_id == update_report.professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        if not permission.get_all_clients:
            if not permission.get_your_client:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not current_professional.professional_id == client.professional_id: 
                raise HTTPException(status_code=401, detail="Unauthorized professional")

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