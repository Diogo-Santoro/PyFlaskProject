from flask import Flask, render_template
from controllers.categoria_controller import categoria_bp
from controllers.produto_controller import produto_bp
from controllers.cliente_controller import cliente_bp
from controllers.pedido_controller import pedido_bp
from controllers.pagamento_controller import pagamento_bp
from controllers.carrinho_controller import carrinho_bp
from controllers.avaliacao_controller import avaliacao_bp
from models import db
import config

app = Flask(__name__)

# Configurações da aplicação (importando do config.py)
app.config.from_object(config.Config)

# Inicializando o banco de dados com SQLAlchemy
db.init_app(app)

# Registro de blueprints
app.register_blueprint(categoria_bp, url_prefix='/')
app.register_blueprint(produto_bp, url_prefix='/')
app.register_blueprint(cliente_bp, url_prefix='/')
app.register_blueprint(pedido_bp, url_prefix='/')
app.register_blueprint(pagamento_bp, url_prefix='/')  # Blueprint de pagamentos
app.register_blueprint(carrinho_bp, url_prefix='/')   # Blueprint de carrinhos
app.register_blueprint(avaliacao_bp, url_prefix='/')  # Blueprint de avaliações

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Executar a aplicação
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados, se não existirem
    app.run(debug=True)
