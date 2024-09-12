import click
from app.services.api_key_service import create_api_key
from ...models.api_key_model import APIKey
from app.db.db import SessionLocal, engine
from sqlalchemy import inspect

def generate_api_key(owner: str, contact: str):
    """Create a APIKEY"""
    inspector = inspect(engine)
    has_table = inspector.has_table('api_keys')

    if has_table:
        db = SessionLocal()
        try:
            api_key = APIKey(
                owner = owner,
                contact = contact
            )
            key = create_api_key(api_key, db)
            click.echo(f"Your key: {key.key}")
            click.echo("api key created successfully!")
        finally:
            db.close()  
    else:
        click.echo("api_key's table does not exist.")