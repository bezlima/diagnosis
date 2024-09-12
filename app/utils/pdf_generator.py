from jinja2 import Template
from weasyprint import HTML
from ..templates.report_pdf_template import html_template
from datetime import datetime

def pdf_template(data):

    now = datetime.now()
    timestamp = now.strftime('%d/%m/%Y : %H:%M')
    template = Template(html_template)
    html_content = template.render(report=data["report"], client=data["client"], professional=data["professional"], timestamp=timestamp)
    pdf = HTML(string=html_content).write_pdf()

    return pdf