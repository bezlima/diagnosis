from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..db.db_connect import get_db
from ..schemas import role_schema
from ..models import role_model
from ..services import role_services, professional_services
from typing import Optional
from ..auth.dependencie.auth_dependencie import get_current_user
from ..utils.verify_permission import verify_permission
import logging

logger = logging.getLogger(__name__)

role_router = APIRouter(tags=["Roles"], prefix='/role')

@role_router.post('/', status_code=201)
def create_role(role: role_schema.RoleBase, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try :
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        has_role = role_services.get_role_by_name(db, role.role_name)
        role_data = role_model.Role(**role.model_dump())
        new_role = role_services.create_role(db, role_data)

        if not permission.create_role:
            raise HTTPException(status_code=401, detail="Unauthorized professional")

        if has_role:
            raise HTTPException(status_code=400, detail='Role already exists')
        
        return new_role
    
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

@role_router.get('/', status_code=200)
def get_roles(db: Session = Depends(get_db), list_permission: Optional[bool] = Query(False), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        roles = role_services.get_roles(db)

        if not permission.get_all_roles:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if list_permission:
            return roles
        else:
            return[{"role_id": role.role_id,"role_name": role.role_name} for role in roles]

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

@role_router.get('/{role_id}', status_code=200)
def get_role_by_id(role_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        professional = professional_services.get_professional_by_id(db, current_professional.professional_id)
        role = role_services.get_role_by_id(db, role_id)

        if not permission.get_all_roles:
            if not permission.get_your_role:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not professional.role_id == role_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        return role

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

@role_router.put('/{role_id}', status_code=202)
def update_role(role_id: int, update_infos: role_schema.RoleBase, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        professional = professional_services.get_professional_by_id(db, current_professional.professional_id)
        has_role = role_services.get_role_by_name(db, update_infos.role_name)

        if not permission.get_all_roles:
            if not permission.get_your_role:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not professional.role_id == role_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")

        if not permission.edit_report:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if has_role:
            raise HTTPException(status_code=400, detail='Role already exists')
        
        update_roles = role_services.update_role(db, role_id, update_infos)
        return update_roles

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

@role_router.delete('/{role_id}', status_code=204)
def delete_role(role_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        professional = professional_services.get_professional_by_id(db, current_professional.professional_id)
        delete_roles = role_services.delete_role(db, role_id,)

        if not permission.get_all_roles:
            if not permission.get_your_role:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            elif not professional.role_id == role_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")

        if not permission.delete_report:
            raise HTTPException(status_code=401, detail="Unauthorized professional")

        if delete_roles:
            return 
        else:
            raise HTTPException(status_code=404, detail="Role not found")

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