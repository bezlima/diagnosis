from fastapi import FastAPI
from .models import professional_model, role_model, client_model, report_models
from .db.db import engine

from .routes.professional_route import professional_router
from .routes.pdf_route import pdf_router
from .routes.client_route import client_router
from .routes.role_route import role_router
from .routes.login_routes import login_router
from .routes.report_route import report_router

# Inicio do aplicativo
app = FastAPI(
    title="Seu Projeto API",
    description="Descrição detalhada da sua API",
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
)

# inicio da base de dados
professional_model.Base.metadata.create_all(bind=engine)
role_model.Base.metadata.create_all(bind=engine)
client_model.Base.metadata.create_all(bind=engine)
report_models.Base.metadata.create_all(bind=engine)

# Inclusão de rotas ao projeto
app.include_router(login_router)
app.include_router(role_router)
app.include_router(professional_router)
app.include_router(client_router)
app.include_router(report_router)
app.include_router(pdf_router)