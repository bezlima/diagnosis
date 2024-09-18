import click
from InquirerPy import prompt
from tabulate import tabulate

from app.utils.cli_functions.start_database import start_db
from app.utils.cli_functions.start_server import start_server
from app.utils.cli_functions.create_api_key import generate_api_key
from app.utils.cli_functions.start_admin_role import start_admin_role
from app.utils.cli_functions.testing_diagnosis import testing_diagnosis
from app.utils.cli_functions.start_professional import start_professional
from app.utils.cli_functions.get_api_keys import get_api_keys, get_key

@click.group()
def cli():
    """CLI to manage the application"""
    pass

def exit_cli():
    """Exit the CLI"""
    click.echo("Exiting the CLI.")
    return False

@cli.command()
def start():
    """Command to start server""" 
    start_server()

@cli.command()
@click.option('--owner', prompt='Enter the owner of the API key', help='Owner of the API key')
@click.option('--contact', prompt='Enter the contact for the API key', help='Contact for the API key')
def create_apikey(owner, contact):
    """Command to create an API Key"""
    generate_api_key(owner, contact)

@cli.command()
def get_apikeys():
    """Command to get all API Keys""" 
    keys = get_api_keys()
    if keys:
        table_data = [
            [key.api_key_id, key.key, key.owner, key.contact] for key in keys
        ]
        headers = ["ID", "Key", "Owner", "Contact"]
        click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        click.echo("No API keys found.")

@cli.command()
@click.option('--owner', prompt='Enter the owner of the API key', help='Owner of the API key')
def get_apikey(owner):
    """Command to get a single API Key by owner"""
    key = get_key(owner)
    if key:
        table_data = [[key.api_key_id, key.key, key.owner, key.contact]]
        headers = ["ID", "Key", "Owner", "Contact"]
        click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        click.echo(f"No API key found for owner: {owner}")

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
