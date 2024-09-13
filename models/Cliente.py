from models import db  # Importa o db da inicialização em models/__init__.py

class Cliente(db.Model):
    __tablename__ = 'clientes'
    cliente_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=db.func.current_timestamp())
