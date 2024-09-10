from . import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    cliente_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    cep = db.Column(db.String(20))
    telefone = db.Column(db.String(20))
    data_cadastro = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
