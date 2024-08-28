from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.db_connect import get_db
from ..schemas import client_schema
from typing import Literal

#rotas deve receber professional id para verificar se tem permissão para x

client_router = APIRouter(tags=["Clients"], prefix="/clients")

@client_router.post('/{professional_id}')
def create_client(professional_id: int, client: client_schema.ClientCreate, db: Session = Depends(get_db)):
    return

@client_router.get('/{professional_id}')
def get_clients(professional_id: int):
    return

@client_router.get('/{professional_id}/{client_id}')
def get_client_by_id(client_id: int):
    return

@client_router.get('/{professional_id}/{search_apotion}/{client_id}')
def get_client_by_search_apotion(professional_id: int, search_apotion: Literal["rg", "cpf", "email", "name"], client_id: int):
    return

@client_router.put('/{professional_id}/{client_id}')
def update_client(client: client_schema.UpdateClient ,client_id: int):
    return

@client_router.delete('/{professional_id}/{client_id}')
def delete_client(client_id: int):
    return