from fastapi import APIRouter, Response, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from ..utils.pdf_generator import pdf_template
from ..utils.verify_permission import verify_permission
from ..services import report_services
from ..services import client_service
from ..services import professional_services
from ..db.db_connect import get_db
from sqlalchemy.orm import Session
import logging
from ..auth.dependencie.auth_dependencie import get_current_user
 
logger = logging.getLogger(__name__)

pdf_router = APIRouter(prefix= '/pdf',tags=["PDF Generator"])

@pdf_router.get('/{report_id}', status_code=200)
def generate_pdf(report_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        report = report_services.get_report_by_id(db, report_id)
        client = client_service.get_client_by_id(db, client_id=report.client_id)
        professional = professional_services.get_professional_by_id(db, professional_id=report.professional_id)
        data = {
            "report": report,
            "professional": professional,
            "client": client,
        }
        pdf = pdf_template(data)

        if not permission.create_pdf: 
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if not permission.get_all_reports or not permission.get_your_report:
            raise HTTPException(status_code=401, detail="Unauthorized professional")

        if permission.get_your_report and not permission.get_all_reports:
            if  current_professional.professional_id != report.professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
                                    
        if not report:
            logger.error(f"Report with id {report_id} not found.")
            raise HTTPException(status_code=404, detail="Report Not Found")
        
        if not client:
            logger.error(f"Client with id {report.client_id} not found.")
            raise HTTPException(status_code=404, detail="Client Not Found")

        if not professional:
            logger.error(f"Professional with id {report.professional_id} not found.")
            raise HTTPException(status_code=404, detail="Professional Not Found")

        return Response(content=pdf, media_type="application/pdf")
        
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
