from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Pedido, Cliente, Produto, PedidoItem, db

pedido_bp = Blueprint('pedido', __name__)

@pedido_bp.route('/pedidos')
def listar_pedidos():
    pedidos = Pedido.query.all()
    return render_template('pedido/listar_pedidos.html', pedidos=pedidos)

@pedido_bp.route('/pedidos/novo', methods=['GET', 'POST'])
def cadastrar_pedido():
    clientes = Cliente.query.all()
    produtos = Produto.query.all()
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
                    produto = Produto.query.get(produto_id)
                    item = PedidoItem(pedido_id=pedido.pedido_id, produto_id=produto_id, quantidade=quantidade, preco=produto.preco)
                    db.session.add(item)

        db.session.commit()
        flash('Pedido cadastrado com sucesso!', 'success')
        return redirect(url_for('pedido.listar_pedidos'))
    return render_template('pedido/cadastrar_pedido.html', clientes=clientes, produtos=produtos)

@pedido_bp.route('/pedidos/<int:id>/editar', methods=['GET', 'POST'])
def editar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    clientes = Cliente.query.all()
    produtos = Produto.query.all()
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
                    produto = Produto.query.get(produto_id)
                    item = PedidoItem(pedido_id=pedido.pedido_id, produto_id=produto_id, quantidade=quantidade, preco=produto.preco)
                    db.session.add(item)

        db.session.commit()
        flash('Pedido editado com sucesso!', 'success')
        return redirect(url_for('pedido.listar_pedidos'))
    return render_template('pedido/editar_pedido.html', pedido=pedido, clientes=clientes, produtos=produtos)

@pedido_bp.route('/pedidos/<int:id>/excluir', methods=['POST'])
def excluir_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    for item in pedido.itens:
        db.session.delete(item)
    db.session.delete(pedido)
    db.session.commit()
    flash('Pedido excluído com sucesso!', 'success')
    return redirect(url_for('pedido.listar_pedidos'))
