html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Diagnosis {{ report.report_id }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        @page {
            size: A4;
            margin: 20mm;
            @bottom-right {
                content: counter(page) " / " counter(pages);
                font-size: 12px;
                color: #666;
            }
        }
        header .content-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .header-span {
            display: flex;
            align-items: center;
            border: 1px solid #000;
            padding-top: 2px;
            padding-bottom: 2px;
            padding-left: 2px;
        }
        .header-span p {
            margin-right: 5px;
        }
        header .content-header span {
            display: flex;
            align-items: center;
            border: 1px solid #000;
            width: 50%;
            padding-top: 2px;
            padding-bottom: 2px;
            padding-left: 2px;
        }
        header .content-header span p{
            margin-right: 5px;
        }
        .content {
            text-align: justify;  
            margin-bottom: 60px;
        }
        .header-info {
            margin-bottom: 20px;
        }
        .header-info h2 {
            font-size: 20px;
            text-align: start;
            padding: 0;
            margin: 0;
        }
        h1 {
            font-size: 20px;
            color: #000;
        }
        p {
            font-size: 14px;
            text-align: justify;
            margin: 0;
        }
        .timestamp {
            font-size: 12px;
            color: #666;
            text-align: right;
        }
        .signature {
            display: flex;
            align-items: center;
            justify-content: space-evenly;
        }
        .signature div{
            border-top: 1px solid #000;
            width: 250px;
        }
        .signature div p {
            margin: 0;
            padding: 0;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="timestamp">
        Id do report: {{ report.report_id }};
        Gerado em: {{ timestamp }}
    </div>
    <header>
        <div class="header-info">
            <h2> Informações do cliente </h2>
            <span class="content-header">
                <span>
                    <p>Nome:</p>
                    <p><strong>{{ client.name }}</strong> - {{ client.client_id }}</p>
                </span>
                <span>
                    <p>Idade:</p>
                    <p>{{ client.age }}</p>
                </span>
            </span>
            <span class="header-span">
                <p>Contato:</p>
                <p>{{ client.email }}</p>
            </span>
            <span class="header-span">
                <p>Endereço:</p>
                <p>{{ client.address }}</p>
            </span>
            <span class="content-header">
                <span>
                    <p>RG:</p>
                    <p>{{ client.client_document_RG }}</p>
                </span>
                <span>
                    <p>CPF:</p>
                    <p>{{ client.client_document_CPF }}</p>
                </span>
            </span>
        </div>
        <div class="header-info">
            <h2> Informações do profissional </h2>
            <span class="content-header">
                <span>
                    <p>Nome:</p>
                    <p><strong>{{ professional.name }}</strong> - {{ professional.professional_id }}</p>
                </span>
                <span>
                    <p>Documento profisional:</p>
                    <p>{{ professional.professional_document_type }} - {{professional.professional_document}}</p>
                </span>
            </span>
            <span class="header-span">
                <p>Contato:</p>
                <p>{{ professional.email }}</p>
            </span>
            <span class="header-span">
                <p>Endereço:</p>
                <p>{{ client.address }}</p>
            </span>
        </div>
    </header>
    <div class="content">
        <h1>{{ report.title }}</h1>
        <p>{{ report.content }}</p>
    </div>
    <div class="signature">
        <div>
            <p>Assinatura do profisional</p>
            <p> <strong>{{professional.name}}, {{professional_document_type}} {{professional.professional_document}}</strong> </p>
        </div>
        <div>
            <p>Assinatura do cliente</p>
            <p> <strong>{{client.name}}</strong>  </p>
        </div>
    </div>
</body>
</html>

"""