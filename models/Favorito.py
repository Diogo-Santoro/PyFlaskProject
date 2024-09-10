from . import db
from datetime import datetime

class Favorito(db.Model):
    __tablename__ = 'favoritos'
    favorito_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'), nullable=False)
    data_adicao = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento com cliente e produto
    cliente = db.relationship('Cliente', backref='favoritos')
    produto = db.relationship('Produto', backref='favoritos')
