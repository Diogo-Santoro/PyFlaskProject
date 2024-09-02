# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

class Categoria(db.Model):
    __tablename__ = 'categorias'
    categoria_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)

class Produto(db.Model):
    __tablename__ = 'produtos'
    produto_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.categoria_id'))
    imagem_url = db.Column(db.String(255))
    data_cadastro = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    pedido_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'))
    total = db.Column(db.Numeric(10, 2), nullable=False)
    status_pedido = db.Column(db.String(50), nullable=False, default='Pendente')
    data_pedido = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    endereco_entrega = db.Column(db.String(255))
    cidade_entrega = db.Column(db.String(100))
    estado_entrega = db.Column(db.String(100))
    cep_entrega = db.Column(db.String(20))

class ItemPedido(db.Model):
    __tablename__ = 'itens_pedido'
    item_id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'))
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)

class Pagamento(db.Model):
    __tablename__ = 'pagamentos'
    pagamento_id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'))
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    metodo_pagamento = db.Column(db.String(50))
    status_pagamento = db.Column(db.String(50), nullable=False, default='Pendente')
    data_pagamento = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Carrinho(db.Model):
    __tablename__ = 'carrinhos'
    carrinho_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'))
    quantidade = db.Column(db.Integer, nullable=False)
    data_adicao = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'
    avaliacao_id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'))
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text)
    data_avaliacao = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Favorito(db.Model):
    __tablename__ = 'favoritos'
    favorito_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'))
    data_adicao = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
