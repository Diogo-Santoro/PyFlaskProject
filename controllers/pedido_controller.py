from flask import Blueprint, render_template, request, redirect, url_for
from models.Pedido import Pedido  # Importar a classe Pedido corretamente
from models.Cliente import Cliente  # Importar a classe Cliente corretamente
from models.PedidoItem import PedidoItem  # Importar a classe PedidoItem corretamente
from models.Produto import Produto  # Importar a classe Produto corretamente
from models import db

pedido_bp = Blueprint('pedido', __name__)

@pedido_bp.route('/pedidos')
def listar_pedidos():
    pedidos = db.session.query(Pedido).all()
    return render_template('pedido/listar_pedidos.html', pedidos=pedidos)

@pedido_bp.route('/pedidos/novo', methods=['GET', 'POST'])
def cadastrar_pedido():
    clientes = db.session.query(Cliente).all()
    produtos = db.session.query(Produto).all()

    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        total = request.form['total']
        pedido = Pedido(cliente_id=cliente_id, total=total)
        db.session.add(pedido)
        db.session.commit()

        for produto_id, quantidade in request.form.items():
            if produto_id.startswith('produto_'):
                produto_id = produto_id.split('_')[1]
                quantidade = int(quantidade)
                if quantidade > 0:
                    produto = db.session.query(Produto).get(produto_id)
                    item = PedidoItem(pedido_id=pedido.pedido_id, produto_id=produto_id, quantidade=quantidade, preco=produto.preco)
                    db.session.add(item)

        db.session.commit()
        return redirect(url_for('pedido.listar_pedidos'))

    return render_template('pedido/cadastrar_pedido.html', clientes=clientes, produtos=produtos)

@pedido_bp.route('/pedidos/<int:id>/editar', methods=['GET', 'POST'])
def editar_pedido(id):
    pedido = db.session.query(Pedido).get_or_404(id)
    clientes = db.session.query(Cliente).all()
    produtos = db.session.query(Produto).all()

    if request.method == 'POST':
        pedido.cliente_id = request.form['cliente_id']
        pedido.total = request.form['total']

        for item in pedido.itens:
            db.session.delete(item)

        for produto_id, quantidade in request.form.items():
            if produto_id.startswith('produto_'):
                produto_id = produto_id.split('_')[1]
                quantidade = int(quantidade)
                if quantidade > 0:
                    produto = db.session.query(Produto).get(produto_id)
                    item = PedidoItem(pedido_id=pedido.pedido_id, produto_id=produto_id, quantidade=quantidade, preco=produto.preco)
                    db.session.add(item)

        db.session.commit()
        return redirect(url_for('pedido.listar_pedidos'))

    return render_template('pedido/editar_pedido.html', pedido=pedido, clientes=clientes, produtos=produtos)

@pedido_bp.route('/pedidos/<int:id>/excluir', methods=['POST'])
def excluir_pedido(id):
    pedido = db.session.query(Pedido).get_or_404(id)
    for item in pedido.itens:
        db.session.delete(item)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('pedido.listar_pedidos'))
