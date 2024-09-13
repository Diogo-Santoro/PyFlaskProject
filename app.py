from flask import Flask, render_template
from models import db  # Certifique-se de importar o `db` diretamente de models/__init__.py
from models.Produto import Produto
from models.Categoria import Categoria
from models.Cliente import Cliente
from models.Pedido import Pedido
from config import Config
from controllers.produto_controller import produto_bp
from controllers.categoria_controller import categoria_bp
from controllers.cliente_controller import cliente_bp
from controllers.pedido_controller import pedido_bp
import os

app = Flask(__name__)
app.config.from_object(Config)

# Definindo a secret key para proteger sessões
app.secret_key = os.urandom(24)

# Inicializa o banco de dados com a instância do aplicativo Flask
db.init_app(app)

# Caminho base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

# Função que cria o banco de dados e as tabelas se não existirem
with app.app_context():
    db_path = os.path.join(basedir, 'app.db')
    if not os.path.exists(db_path):
        db.create_all()  # Cria o banco de dados e as tabelas automaticamente
        print("Banco de dados criado com sucesso!")

# Registra os blueprints
app.register_blueprint(produto_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(pedido_bp)

# Rota principal que renderiza um template HTML
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o template index.html

if __name__ == '__main__':
    app.run(debug=True)
