from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db
from ..schemas import client_schema
from typing import Literal
from ..services import client_service
from sqlalchemy.exc import SQLAlchemyError
from ..auth.dependencie.auth_dependencie import get_current_user
from ..utils.verify_permission import verify_permission
import logging

logger = logging.getLogger(__name__)

client_router = APIRouter(tags=["Clients"], prefix="/clients")

@client_router.post('/', status_code=201)
def create_client(client: client_schema.ClientCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        new_client = client_service.create_client(db, client)

        if not permission.create_client: 
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        return new_client
    
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

@client_router.get('/', status_code=200)
def get_clients(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        clients = client_service.get_all_clients(db)

        if not permission.get_all_clients:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        return clients
    
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


@client_router.get('/professional/{professional_id}', status_code=200)
def get_clients_by_professional(professional_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        clients = client_service.get_clients_by_professional_id(db, professional_id)
        
        if not permission.get_all_clients or not permission.get_your_client:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if permission.get_your_client and not permission.get_all_clients:
            if  current_professional.professional_id != clients[0].professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        return clients

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

@client_router.get('/{client_id}', status_code=200)
def get_client_by_id(client_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        client = client_service.get_client_by_id(db, client_id)

        if not permission.get_all_clients or not permission.get_your_client:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if permission.get_your_client and not permission.get_all_clients:
            if  current_professional.professional_id != client.professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")

        return client

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

## ...rever metodo de busca para buscar com mais opções, todos os esquemas... ##
@client_router.get('/{search_option}/{client_ref}', status_code=200)
def get_client_by_search_apotion(search_option: Literal["rg", "cpf", "email", "name"], client_ref: str, db: Session = Depends(get_db),  current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)

        if not permission.get_all_clients or not permission.get_your_client:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        #  ---------------------------
        if permission.get_your_client and not permission.get_all_clients:
            if  current_professional.professional_id != client.professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        if search_option == 'rg':
            client = client_service.get_client_by_RG(db, client_ref)
            return client
        elif search_option == 'cpf':
            client = client_service.get_client_by_CPF(db, client_ref)
            return client
        elif search_option == 'email':
            client = client_service.get_client_by_email(db, client_ref)
            return client
        elif search_option == 'name':
            #busca com nome pegar parcial
            client = client_service.get_clients_by_name(db, client_ref)
            return client

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

@client_router.put('/{client_id}', status_code=202)
def update_client(client: client_schema.UpdateClient, client_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        update_client = client_service.update_client(db, client_id, client)

        if not permission.get_all_clients or not permission.get_your_client:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if permission.get_your_client and not permission.get_all_clients:
            if  current_professional.professional_id != client.professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        if not permission.edit_clients:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        return update_client
    
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
    
@client_router.delete('/{client_id}', status_code=204)
def delete_client(client_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        current_professional = current_user
        permission = verify_permission(current_professional, db)
        delete_client = client_service.delete_client(db, client_id)

        if not permission.get_all_clients or not permission.get_your_client:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if permission.get_your_client and not permission.get_all_clients:
            if  current_professional.professional_id != delete_client.professional_id:
                raise HTTPException(status_code=401, detail="Unauthorized professional")
            
        if not permission.delete_client:
            raise HTTPException(status_code=401, detail="Unauthorized professional")
        
        if delete_client:
            return 
        else:
            raise HTTPException(status_code=404, detail="Client not found")
        
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