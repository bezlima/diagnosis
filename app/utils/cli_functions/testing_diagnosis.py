import click
from .start_admin_role import start_admin_role
from .start_database import start_db
from .start_professional import start_professional
from .start_server import start_server
from .start_client import start_client
from .start_report import start_report

def testing_diagnosis():
    """Initialize Disgnosis testing"""

    click.echo(" Iniciando modelo de teste ... ")

    start_db()

    start_admin_role()

    start_professional()

    start_client()

    # start_report()

    start_server()