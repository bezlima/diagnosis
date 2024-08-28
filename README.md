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
    pip install InquirerPy


# criar role adm
python cli.py init-admin-role

# inicio personalizado
python cli.py main-menu

# proximos passos

[x] editar role schemas e services

[x] criar report schema, models, services e routes

[x] criar pdf routes

[] alterar pdf generator = alterar geração - criar template

[x] criar rota de autenticação para professionals

[] ------ conectar rotas aos serviços -------

[] adicionar JWT em rotas

[] criar api Key para o projeto > adcionar as rotas

[] criar requirements.txt > pip freze

[] criar função de inicialização para gerar role incial(todas a permissões) e usuário adm inicial