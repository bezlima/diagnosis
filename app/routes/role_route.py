from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..db.db_connect import get_db
from ..schemas.role_schema import RoleBase
from ..services import role_services
from typing import Optional

role_router = APIRouter(tags=["Roles"], prefix='/role')

#rotas deve receber professional id para verificar se tem permissão para x

@role_router.post('/')
def create_role(role: RoleBase, db: Session = Depends(get_db)):
    try :
        has_role = role_services.get_role_by_name(db, role.role_name)
        if has_role:
            raise HTTPException(status_code=400, detail='Role already exists')
        
        new_role = role_services.create_role(db, role)
        return new_role
    
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

@role_router.get('/')
def get_roles(db: Session = Depends(get_db), list_permission: Optional[bool] = Query(False)):
    try:
        roles = role_services.get_roles(db)
        if list_permission:
            return roles
        else:
            return[{"role_id": role.role_id,"role_name": role.role_name} for role in roles]

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

@role_router.get('/{role_id}')
def get_role_by_id():
    return

@role_router.put('/{role_id}')
def update_role():
    return

@role_router.delete('/{role_id}')
def delete_role():
    return