from . import db
from datetime import datetime

class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'
    avaliacao_id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'), nullable=False)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text)
    data_avaliacao = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento com produto e cliente
    produto = db.relationship('Produto', backref='avaliacoes')
    cliente = db.relationship('Cliente', backref='avaliacoes')
