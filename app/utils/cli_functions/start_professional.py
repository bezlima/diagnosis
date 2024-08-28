import click
from app.db.db import SessionLocal
from sqlalchemy import inspect
from app.db.db import engine
from app.models.professional_model import Professional
from app.services.professional_services import create_professional
from app.models.role_model import Role
from app.schemas.professional_schema import ProfessionalCreate

def start_professional():
    """Initialize Professinal"""
    inspector = inspect(engine)
    has_professional_table = inspector.has_table('professionals')
    has_role_table = inspector.has_table('roles')

    if has_professional_table & has_role_table:

        db = SessionLocal()
        has_admin_role = db.query(Role.role_id == 1).first()

        if has_admin_role:
            try:
                if not db.query(Professional).first():
                    professinal = ProfessionalCreate(

                        
                        name = "Diagnosis Example",
                        email = "example@diagnosis.com",
                        professional_document_RG = "00000000000",
                        professional_document_CPF = "00000000000",
                        professional_document_type = "CRM",
                        professional_document = "000000/SP",
                        address = "SP / BR, 0000",
                        role_id = 1,
                        password = "example123"

                    )
                    create_professional(db, professinal)
                    click.echo("Professional created successfully! : email: example@diagnosis.com , password: example123")
                
                else:
                    click.echo("Professional already exists.")

            finally:
                db.close()

        return click.echo("Role id 1 does not exist.")
    
    return click.echo("Professional's or Role's table does not exist.")
