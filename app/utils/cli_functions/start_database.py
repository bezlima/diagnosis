import click
from sqlalchemy import inspect
from app.models import professional_model, role_model, client_model, report_models
from app.db.db import engine

def check_table_exists(engine, table_name):
    """Check if a table exists in the database"""
    inspector = inspect(engine)
    return inspector.has_table(table_name)

def start_db():
    """Start the Database"""
    tables_to_check = {
        "professionals": professional_model.Base,
        "roles": role_model.Base,
        "clients": client_model.Base,
        "reports": report_models.Base
    }
    
    for table_name, model_base in tables_to_check.items():
        if check_table_exists(engine, table_name):
            click.echo(f"Table '{table_name}' already exists.")
        else:
            click.echo(f"Creating table '{table_name}'.")
            model_base.metadata.create_all(bind=engine)

    click.echo("Database initialization completed!")

