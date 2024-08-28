from pydantic import BaseModel

class ClientBase(BaseModel):
    email : str
    address: str
    name: str
    age : int
    client_document_RG: str
    client_document_CPF: str
    professionals_id : int

class ClientCreate(ClientBase):
    email : str
    address: str
    name: str
    age : int
    client_document_RG: str
    client_document_CPF: str
    professionals_id : int


class UpdateClient(BaseModel):
    email : str
    address: str
    name: str
    age : int
    client_document_RG: str
    client_document_CPF: str
    professionals_id : int

class Client(ClientBase):
    client_id: int

    class Config:
        from_attributes = True