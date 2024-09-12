from . import db
from datetime import datetime

class Pagamento(db.Model):
    __tablename__ = 'pagamentos'
    pagamento_id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    metodo_pagamento = db.Column(db.String(50))
    status_pagamento = db.Column(db.String(50), default='Pendente')
    data_pagamento = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento com pedido
    pedido = db.relationship('Pedido', backref='pagamentos')
