from jinja2 import Template
from weasyprint import HTML

html_template = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { color: #333; }
        p { font-size: 14px; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
</body>
</html>
"""

def pdf_template(data):

    template = Template(html_template)
    html_content = template.render(title=data["title"], content=data["content"])

    pdf = HTML(string=html_content).write_pdf()

    return pdf