from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..db.db_connect import get_db
from ..schemas import role_schema
from ..models import role_model
from ..services import role_services
from typing import Optional
import logging

logger = logging.getLogger(__name__)

role_router = APIRouter(tags=["Roles"], prefix='/role')

#rotas deve receber professional id para verificar se tem permissão para x
#adicionar http status_code=200 nas rotas

@role_router.post('/')
def create_role(role: role_schema.RoleBase, db: Session = Depends(get_db)):
    try :
        has_role = role_services.get_role_by_name(db, role.role_name)
        if has_role:
            raise HTTPException(status_code=400, detail='Role already exists')
        
        role_data = role_model.Role(**role.model_dump())
        new_role = role_services.create_role(db, role_data)
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

@role_router.get('/')
def get_roles(db: Session = Depends(get_db), list_permission: Optional[bool] = Query(False)):
    try:
        roles = role_services.get_roles(db)
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

@role_router.get('/{role_id}')
def get_role_by_id(role_id: int, db: Session = Depends(get_db)):
    try:
        role = role_services.get_role_by_id(db, role_id)
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

# mudar para fazer o dicioario fora so serviço ou mudar todos para dentro do serviço #
@role_router.put('/{role_id}')
def update_role(role_id: int, update_infos: role_schema.RoleBase, db: Session = Depends(get_db)):
    try:

        has_role = role_services.get_role_by_name(db, update_infos.role_name)
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

@role_router.delete('/{role_id}')
def delete_role(role_id: int, db: Session = Depends(get_db)):
    try:
        delete_roles = role_services.delete_role(db, role_id,)

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