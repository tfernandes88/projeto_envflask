'''
#### Estrutura de um projeto em Flask ###

project/
│
├── app/
│   ├── __init__.py         # Inicialização da aplicação
│   ├── routes.py           # Rotas da aplicação
│   ├── models.py           # Modelos (ORM)
│   ├── forms.py            # Formulários (opcional)
│   ├── templates/          # Templates HTML (Jinja2)
│   │   ├── base.html       # Template base
│   │   ├── index.html      # Página inicial
│   │   └── ...             # Outros templates
│   ├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── css/
│   │   │   └── styles.css  # Estilos personalizados
│   │   ├── js/
│   │   └── img/
│   └── utils.py            # Funções utilitárias (opcional)
│
├── migrations/             # Arquivos de migração do banco de dados
├── tests/                  # Testes unitários e de integração
│   ├── __init__.py
│   └── test_routes.py      # Testes das rotas
│
├── .env                    # Variáveis de ambiente (opcional)
├── config.py               # Configurações da aplicação
├── requirements.txt        # Dependências do projeto
├── run.py                  # Ponto de entrada para rodar o servidor
└── README.md               # Documentação do projeto
'''
import os

# Nome das pastas
folders = [
    'app',
    'app/templates',
    'app/static',
    'app/static/css',
    'app/static/js',
    'app/static/img',
    'migrations',
    'tests',
    '.venv'
    ]

# Nome dos arquivos

arquivos = [
    'app/__init__.py',
    'app/routes.py',
    'app/models.py',
    'app/forms.py',
    'app/utils.py',
    'app/static/css/styles.css',
    'tests/__init__.py',
    'tests/__test_routes.py',
    './config.py',
    './run.py',
    './README.md',
    './Pipfile'
]

# Criar pastas
for folder in folders:
    if not os.path.exists(folder):
        # Cria as pastas, incluindo subdir
        os.makedirs(folder)
        print(f"Pasta '{folder}' foi criada com sucesso!")
    else:
        print(f"A pasta '{folder}' já existe.")

# Criar arquivos

for arquivo in arquivos:
    if not os.path.exists(arquivo):
        # Garantir que o diretório do arquivo exista antes de criá-lo
        os.makedirs(os.path.dirname(arquivo), exist_ok=True)
        with open(arquivo, 'w') as file:
            '''
            if arquivo.endswith('.py'):
                file.write('# Arquivo Python\n')
            '''
            if arquivo == './run.py':
                file.write(
                    "from app import create_app\n\n"
                    "app = create_app()\n\n"
                    "if __name__ == \"__main__\":\n"
                    "    app.run(debug=True)\n"
                )
            elif arquivo == 'app/__init__.py':
                file.write(
                    "from flask import Flask\n"
                    "from flask_sqlalchemy import SQLAlchemy\n\n"

                    "db = SQLAlchemy()\n\n"

                    "def create_app():\n"
                    "    app = Flask(__name__)\n"
                    "    app.config.from_object('config.Config')\n\n"
                    
                    "db.init_app(app)\n\n"

                    "# Registrar rotas\n"
                    "with app.app_context():\n"
                    "    from . import routes\n"
                    "    db.create_all()\n"
                    "return app"
                )
            elif arquivo == 'app/routes.py':
                file.write(
                    "from flask import render_template,\n"
                    "from flask import request,\n"
                    "from flask import redirect,\n"
                    "from flask import url_for,\n"
                    "from .models import db, User\n\n"

                    "@app.route('/')\n"
                    "def index():\n"
                    "users = User.query.all()\n"
                    "return render_template('index.html', users=users)\n\n"

                    "@app.route('/add_user', methods=['POST'])\n"
                    "def add_user():\n"
                    "    name = request.form.get('name')\n"
                    "    if name:\n"
                    "        new_user = User(name=name)\n"
                    "        db.session.add(new_user)\n"
                    "        db.session.commit()\n"
                    "    return redirect(url_for('index'))\n"
                )
            elif arquivo == 'app/models.py':
                file.write(
                    "from . import db\n\n"

                    "class User(db.Model):\n"
                    "    id = db.Column(db.Integer, primary_key=True)\n"
                    "    name = db.Column(db.String(100), nullable=False)\n"
                )
            elif arquivo == './config.py':
                file.write(
                    "import os\n\n"

                    "class Config:\n"
                    "    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')\n"
                    "    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')\n"
                    "    SQLALCHEMY_TRACK_MODIFICATIONS = False\n"
                )
            elif arquivo == 'app/templates/index.html':
                file.write(
                    "<!DOCTYPE html>\n"
                    "<html lang=\"en\">\n"
                    "<head>\n"
                    "    <meta charset=\"UTF-8\">\n"
                    "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
                    "    <title>Flask App</title>\n"
                    "</head>\n"
                    "<body>\n"
                    "    <h1>Lista de Usuários</h1>\n"
                    "    <ul>\n"
                    "        {% for user in users %}\n"
                    "        <li>{{ user.name }}</li>\n"
                    "        {% endfor %}\n"
                    "    </ul>\n"
                    "    <form action=\"{{ url_for('add_user') }}\" method=\"POST\">\n"
                    "        <input type=\"text\" name=\"name\" placeholder=\"Nome\">\n"
                    "        <button type=\"submit\">Adicionar</button>\n"
                    "    </form>\n"
                    "</body>\n"
                    "</html>"
                )
            elif arquivo.endswith('.md'):
                file.write('# Documentação #\n')
            elif arquivo.endswith('.css'):
                file.write('/* Arquivo CSS */\n')
            elif arquivo == 'Pipfile':
                file.write('# Arquivo Pipfile\n')
            else:
                file.write('# Arquivo vazio\n')

        print(f"Arquivo '{arquivo}' criado com sucesso!")
    else:
        print(f"Arquivo '{arquivo}' já existe.")
