uvicorn app.main:app --reload

pip install
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

# criar role adm
python cli.py init-admin-role

# inicio personalizado
python cli.py main-menu - menu de inicio

python cli.py start - inicio

python cli.py get-apikeys - 

python cli.py get-apikeys - 

# proximos passos

[x] editar role schemas e services

[x] criar report schema, models, services e routes

[x] criar pdf routes

[x] criar rota de autenticação para professionals

[x] cors policy

[x] conectar rotas aos serviços - professional, roles, clients, report

[x] adicionar JWT em rotas

[x] criar api Key para o projeto > adcionar as rotas
 
[x] criar cli para iniciar servidor

[x] criar cli para iniciar uma api key

[x] criar cli para criar um api key

[x] criar função de inicialização para gerar role incial(todas a permissões) e usuário adm inicial

[x] alterar pdf generator = alterar geração - criar template

[] verificar dicionario em serviços, escolher se coloca model_dump() no serviço ou na rota

[] criar regras de negocio nas rotas
    [x] client
    [x] login
    [x] pdf
    [x] professional
    [] report
    [] role

[] verificar resposta de rota
    [x] client
    [x] login
    [x] pdf
    [x] professional
    [] report
    [] role

[x] alterar role entitie

[] adicionar response models

[] modificar o schema para teste em swagger

[] criar requirements.txt > pip freze

[] refatorar e organizar imports se necessário 

[] adicionar refresh token