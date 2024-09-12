from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db
from ..schemas import client_schema
from typing import Literal
from ..services import client_service
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

#rotas deve receber professional id para verificar se tem permissão para x

client_router = APIRouter(tags=["Clients"], prefix="/clients")

@client_router.post('/', status_code=201)
def create_client(client: client_schema.ClientCreate, db: Session = Depends(get_db)):
    try:
        new_client = client_service.create_client(db, client)
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
def get_clients(db: Session = Depends(get_db)):
    try:
        clients = client_service.get_all_clients(db)
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
def get_clients_by_professional(professional_id: int, db: Session = Depends(get_db)):
    try:
        clients = client_service.get_clients_by_professional_id(db, professional_id)
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
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
    try:
        print(client_id)
        client = client_service.get_client_by_id(db, client_id)
        print(client)
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
def get_client_by_search_apotion(search_option: Literal["rg", "cpf", "email", "name"], client_ref: str, db: Session = Depends(get_db)):
    try:

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
def update_client(client: client_schema.UpdateClient, client_id: int, db: Session = Depends(get_db)):
    try:
        update_client = client_service.update_client(db, client_id, client)
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
def delete_client(client_id: int, db: Session = Depends(get_db)):
    try:
        delete_client = client_service.delete_client(db, client_id)
        
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