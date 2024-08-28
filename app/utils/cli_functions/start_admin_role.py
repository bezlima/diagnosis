import click
from app.db.db import SessionLocal
from sqlalchemy import inspect
from app.models.role_model import Role
from app.services.role_services import create_role
from app.db.db import engine

def start_admin_role():
    """Initialize the administrator role"""
    inspector = inspect(engine)
    has_table = inspector.has_table('roles')
    if has_table:
        db = SessionLocal()
        try:
            if not db.query(Role).first():
                admin_role = Role(
                    role_name ="admin",

                    create_role=True,
                    edit_role=True,
                    delete_role=True,
                    get_all_roles=True,

                    create_professionals=True,
                    get_all_professionals=True,
                    edit_all_professional=True,
                    delete_all_professional=True,

                    create_report=True,
                    get_all_reports=True,
                    edit_all_reports=True,
                    delete_all_reports=True,

                    create_clients=True,
                    get_all_clients=True,
                    edit_all_client=True,
                    delete_all_client=True,
                )
                create_role(db, admin_role)
                click.echo("Admin role created successfully!")
            else:
                click.echo("Admin role already exists.")
        finally:
            db.close()
    return click.echo("Role's table does not exist.")