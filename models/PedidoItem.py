from . import db

class PedidoItem(db.Model):
    __tablename__ = 'itens_pedido'
    item_id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)

    # Relacionamento com pedido e produto
    pedido = db.relationship('Pedido', backref='itens')
    produto = db.relationship('Produto', backref='pedidos')
