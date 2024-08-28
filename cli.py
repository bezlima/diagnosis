import click
from InquirerPy import prompt
from app.utils.cli_functions.start_admin_role import start_admin_role
from app.utils.cli_functions.start_database import start_db
from app.utils.cli_functions.start_server import start_server
from app.utils.cli_functions.start_professional import start_professional
from app.utils.cli_functions.testing_diagnosis import testing_diagnosis

@click.group()
def cli():
    """CLI to manage the application"""
    pass

def exit_cli():
    """Exit the CLI"""
    click.echo("Exiting the CLI.")
    return False

@cli.command()
def main_menu():
    """Main menu to select an action"""
    while True:
        questions = [
            {
                "type": "list",
                "message": "Select an action",
                "name": "action",
                "choices": [
                    "Testing Diagnosis",
                    "Initialize Admin Role",
                    "Start Server",
                    "Start Database",
                    "Start Professional",
                    "Exit",
                ],
            }
        ]

        answers = prompt(questions)

        actions = {
            "Testing Diagnosis": testing_diagnosis,
            "Initialize Admin Role": start_admin_role,
            "Start Server": start_server,
            "Start Database": start_db,
            "Start Professional": start_professional,
            "Exit": exit_cli,
        }

        action = actions.get(answers["action"])
        if action:
            if action() is False:
                break

if __name__ == "__main__":
    cli()
