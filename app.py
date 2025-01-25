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
#    'app',
#    'app/templates',
#    'app/static',
#   'app/static/css',
#   'app/static/js',
#   'app/static/img',
#   'migrations',
#   'tests',
#   '.venv'
    ]

# Nome dos arquivos

arquivos = [
#    'app/__init__.py',
#    'app/routes.py',
#    'app/models.py',
#    'app/forms.py',
#    'app/utils.py',
#    'app/static/css/styles.css',
#    'tests/__init__.py',
#    'tests/__test_routes.py',
#    './config.py',
    './run.py',
#    './README.md',
#    './Pipfile'
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
            else:
                file.write('# Arquivo vazio\n')
            '''
            elif arquivo.endswith('.md'):
                file.write('# Documentação\n')
            elif arquivo.endswith('.css'):
                file.write('/* Arquivo CSS */\n')
            elif arquivo == 'Pipfile':
                file.write('# Arquivo Pipfile\n')
            
            else:
                file.write('# Arquivo vazio\n')
            '''
        print(f"Arquivo '{arquivo}' criado com sucesso!")
    else:
        print(f"Arquivo '{arquivo}' já existe.")
