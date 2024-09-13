from models import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    pedido_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'), nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    status_pedido = db.Column(db.String(50), default='Pendente')
    data_pedido = db.Column(db.DateTime, default=db.func.current_timestamp())
    endereco_entrega = db.Column(db.String(255))
    cidade_entrega = db.Column(db.String(100))
    estado_entrega = db.Column(db.String(100))
    cep_entrega = db.Column(db.String(20))

    # Relacionamento com Cliente
    cliente = db.relationship('Cliente', backref=db.backref('pedidos', lazy=True))
