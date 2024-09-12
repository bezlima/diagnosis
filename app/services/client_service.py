from sqlalchemy.orm import Session
from ..models import client_model
from ..schemas import client_schema

def get_all_clients(db: Session, skip: int = 0, limit: int = 100):
    clients = db.query(client_model.Client).offset(skip).limit(limit).all()
    return clients

def get_clients_by_professional_id(db: Session, professional_id: int, skip: int = 0, limit: int = 100):
    clients = db.query(client_model.Client).filter(client_model.Client.professional_id == professional_id).offset(skip).limit(limit).all()
    return clients

def get_clients_by_name(db: Session, client_name: str, skip: int = 0, limit: int = 100):
    clients = db.query(client_model.Client).filter(client_model.Client.name == client_name).offset(skip).limit(limit).all()
    return clients

def get_client_by_email(db: Session, client_email: str):
    client = db.query(client_model.Client).filter(client_model.Client.email == client_email).first()
    return client

def get_client_by_id(db: Session, client_id: int):
    client = db.query(client_model.Client).filter(client_model.Client.client_id == client_id).first()
    return client

def get_client_by_CPF(db: Session, client_document_CPF: str):
    client = db.query(client_model.Client).filter(client_model.Client.client_document_CPF == client_document_CPF).first()
    return client

def get_client_by_RG(db: Session, client_document_RG: str):
    client = db.query(client_model.Client).filter(client_model.Client.client_document_RG == client_document_RG).first()
    return client

def update_client(db: Session, client_id: int, update_infos: client_schema.UpdateClient):
    client = db.query(client_model.Client).filter(client_model.Client.client_id == client_id).first()
    if client:
        update_data = update_infos.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
        return client
    return None

def delete_client(db: Session, client_id: int):
    client = db.query(client_model.Client).filter(client_model.Client.client_id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
        return True
    return False

def create_client(db: Session, client: client_schema.ClientCreate):
    client = client_model.Client(
        email = client.email,
        address = client.address,
        name = client.name,
        age = client.age,
        client_document_RG = client.client_document_RG,
        client_document_CPF = client.client_document_CPF,
        professional_id = client.professional_id,
    )
    db.add(client)
    db.commit()
    db.refresh(client)
    return(client)