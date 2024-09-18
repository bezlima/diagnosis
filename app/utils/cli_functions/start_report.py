import click
from app.db.db import SessionLocal
from sqlalchemy import inspect
from app.db.db import engine
from app.models.client_model import Client
from app.models.professional_model import Professional
from app.models.report_models import Report
from app.services.report_services import create_report
from app.schemas.report_schema import ReportBase

def start_report():
    """Initialize Report"""

    inspector = inspect(engine)

    has_client_table = inspector.has_table('clients')
    has_professional_table = inspector.has_table('professionals')
    has_report_table = inspector.has_table('reports')

    if has_professional_table and has_client_table and has_report_table:

        db = SessionLocal()

        has_professional = db.query(Professional.professional_id == 1).first()
        has_client = db.query(Client.client_id == 1).first()

        if has_professional and has_client:

            try:
                
                if not db.query(Report).first():
                    report = Report(
                        
                        professional_id = 1,
                        client_id = 1,
                        title = "Placeholder",
                        content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

                    )

                    create_report(db, report)
                    click.echo("Report created successfully!")
                
                else:
                    click.echo("Report already exists.")

            finally:
                db.close()
            
        else:
            return click.echo("Professional_id 1 and client_id 1 does not exist.")
    else:
        return click.echo("Professional's, Client's or Report's table does not exist.")
