
#### Default start server command:

uvicorn app.main:app --reload

# Dependences
    fastapi
    sqlalchemy
    uvicorn
    python-dotenv
    bcrypt
    jinja2
    weasyprint
    pyjwt
    InquirerPy
    tabulate

# inicio personalizado
python cli.py main-menu - menu de inicio

python cli.py start - Inicio

python cli.py init-admin-role - Create a start role with all permissions

python cli.py get-apikeys - Get all api keys

python cli.py get-apikey - Get api key bt owner

python cli.py create-apikey  - Create a api key

python cli.py - Get all cli commands