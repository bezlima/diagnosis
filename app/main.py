from fastapi import FastAPI, Depends
from .db.db import engine
from .auth.dependencie.auth_dependencie import get_current_user

from .models import professional_model, role_model, client_model, report_models, api_key_model

from .routes.professional_route import professional_router
from .routes.pdf_route import pdf_router
from .routes.client_route import client_router
from .routes.role_route import role_router
from .routes.login_routes import login_router
from .routes.report_route import report_router

from fastapi.middleware.cors import CORSMiddleware
from .utils.veirfy_api_key import verify_api_key

app = FastAPI(
    title="Diagnosis",
    description="""
        Diagnosis é um sistema de gerenciamento voltado para a área de saúde, permitindo o cadastro e controle de profissionais e clientes. O sistema oferece ferramentas para que os profissionais escrevam diagnósticos sobre os clientes e gerem relatórios em PDF de maneira eficiente e organizada.
        Focado no ambiente empresarial, o Diagnosis permite a criação de cargos personalizados para os profissionais, com permissões ajustáveis de acordo com suas responsabilidades. Dessa forma, é possível garantir que cada profissional tenha acesso apenas aos recursos necessários para realizar suas funções no sistema.
    """,
    version="1.0.0",
    openapi_tags=[
        {"name": "Login", "description": "Login endpoint"},
        {"name": "Roles", "description": "Role's endpoints"},
        {"name": "Professionals", "description": "Professional's endpoints"},
        {"name": "Clients", "description": "Client's endpoints"},
        {"name": "Reports", "description": "Report's endpoints"},
        {"name": "PDF Generator", "description": "PDF's endpoints"},
    ],
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "Powered by Lucas Lima",
        "url": "https://www.linkedin.com/in/bezlima/",
    },
    terms_of_service="https://api.suporte.com/termos",
    dependencies=[Depends(verify_api_key)]
)

professional_model.Base.metadata.create_all(bind=engine)
role_model.Base.metadata.create_all(bind=engine)
client_model.Base.metadata.create_all(bind=engine)
report_models.Base.metadata.create_all(bind=engine)
api_key_model.Base.metadata.create_all(bind=engine)

app.include_router(login_router)
app.include_router(role_router, dependencies=[Depends(get_current_user)])
app.include_router(professional_router, dependencies=[Depends(get_current_user)])
app.include_router(client_router, dependencies=[Depends(get_current_user)])
app.include_router(report_router, dependencies=[Depends(get_current_user)])
app.include_router(pdf_router, dependencies=[Depends(get_current_user)])

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],  
)