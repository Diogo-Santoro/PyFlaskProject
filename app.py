from flask import Flask, render_template
from models import db
from config import Config   
from controllers.produto_controller import produto_bp
from controllers.categoria_controller import categoria_bp
from controllers.cliente_controller import cliente_bp
from controllers.pedido_controller import pedido_bp
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(produto_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(pedido_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
