from fastapi import FastAPI
from .routes.professional_route import professional_router
from .routes.pdf_route import pdf_router
from .models import professional_model, role_model
from .db.db import engine

professional_model.Base.metadata.create_all(bind=engine)
role_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(professional_router)
app.include_router(pdf_router)