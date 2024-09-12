from .start_admin_role import start_admin_role
from .start_database import start_db
from .start_professional import start_professional
from .start_server import start_server
from .start_client import start_client
from .start_report import start_report
from .create_api_key import generate_api_key

def testing_diagnosis():
    """Initialize Diagnosis testing"""

    start_db()

    start_admin_role()

    generate_api_key('SISTEM', '--')

    start_professional()

    start_client()

    start_report()

    start_server()