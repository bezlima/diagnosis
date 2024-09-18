import click
from app.db.db import SessionLocal
from sqlalchemy import inspect
from app.db.db import engine
from app.models.client_model import Client
from app.models.professional_model import Professional
from app.services.client_service import create_client
from app.schemas.client_schema import ClientCreate

def start_client():

    """Initialize Client"""
    inspector = inspect(engine)
    has_client_table = inspector.has_table('clients')
    has_professional_table = inspector.has_table('professionals')

    if has_professional_table & has_client_table:

        db = SessionLocal()
        has_professional = db.query(Professional.professional_id == 1).first()

        if has_professional:
            try:
                if not db.query(Client).first():
                    professinal = ClientCreate(
                        
                        name = "Diagnosis Client Example",
                        email = "example.client@diagnosis.com",
                        address = "SP / BR, 0000",
                        age = 30,
                        client_document_RG = "00000000000",
                        client_document_CPF = "00000000000",
                        professional_id = 1

                    )

                    create_client(db, professinal)
                    click.echo("Client created successfully!")
                
                else:
                    click.echo("Client already exists.")

            finally:
                db.close()
        else:
            return click.echo("Professional id 1 does not exist.")
    else:
        return click.echo("Professional's or Client's table does not exist.")
