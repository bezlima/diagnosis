# Diagnosis


Diagnosis é um sistema de gerenciamento voltado para a área de saúde, permitindo o cadastro e controle de profissionais e clientes. O sistema oferece ferramentas para que os profissionais escrevam diagnósticos sobre os clientes e gerem relatórios em PDF de maneira eficiente e organizada.

Focado no ambiente empresarial, o Diagnosis permite a criação de cargos personalizados para os profissionais, com permissões ajustáveis de acordo com suas responsabilidades. Dessa forma, é possível garantir que cada profissional tenha acesso apenas aos recursos necessários para realizar suas funções no sistema.

## Autor
#### Lucas Lima  - *Desenvolvedor web*

[![github](https://img.shields.io/badge/github-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bezlima)

[![linkedin](https://img.shields.io/badge/linkedin-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bezlima/)

[![portfolio](https://img.shields.io/badge/portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://bezlima-portfolio.vercel.app/)

## Rodando localmente

Em seu terminal:

Clone o projeto

```bash
  git clone https://github.com/bezlima/diagnosis.git
```

Entre no diretório do projeto

```bash
  cd diagnosis
```
## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente na raiz do seu projeto.

#### `.env`

```toml
SECRET_KEY = "String" 
ALGORITHM = "String"
SQLALCHEMY_DATABASE_URL = "String"
```

## Instalação

Em seu terminal:

Crie um ambiente de virtual

```bash
python -m venv .venv
```

Verifique o ambiente

```bash
which python
```

Ative o ambeiente

```bash
source .venv/bin/activate
```

Instale as dependencias

```bash
pip install -r requirements.txt
```

## Rode o projeto

Iniciando o servidor

```bash
uvicorn app.main:app --reload
```
Parando o projeto

```bash 
Ctrl + C
```
Finalizando o ambiente

```bash
deactivate
```

## Comandos personalizados

| Comando                              | Descrição                                |
|--------------------------------------|------------------------------------------|
| `python cli.py main-menu`            | Menu de início                           |
| `python cli.py start`                | Início     do servidor                              |
| `python cli.py init-admin-role`      | Cria uma role inicial com todas as permissões |
| `python cli.py get-apikeys`          | Obtém todas as chaves de API             |
| `python cli.py get-apikey`           | Obtém uma chave de API por proprietário  |
| `python cli.py create-apikey`        | Cria uma chave de API                    |
| `python cli.py`                      | Lista todos os comandos do CLI           |

## Documentação da API

http://localhost:8000/docs

OU

http://localhost:8000/redoc