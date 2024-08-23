from fastapi import APIRouter, Response
from ..utils.pdf_generator import pdf_template

pdf_router = APIRouter()

@pdf_router.get('/pdf/{report_id}')
def generate_pdf(report_id: str):

    data = {
        "title" : report_id,
        "content" : "content"
    }

    pdf = pdf_template(data)

    return Response(content=pdf, media_type="application/pdf")