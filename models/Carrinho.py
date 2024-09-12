from . import db
from datetime import datetime

class Carrinho(db.Model):
    __tablename__ = 'carrinhos'
    carrinho_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data_adicao = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento com cliente e produto
    cliente = db.relationship('Cliente', backref='carrinhos')
    produto = db.relationship('Produto', backref='carrinhos')
