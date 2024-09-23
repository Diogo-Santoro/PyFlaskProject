from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Pedido import Pedido
from models.Cliente import Cliente
from models import db

pedido_bp = Blueprint('pedido', __name__)

@pedido_bp.route('/pedidos')
def listar_pedidos():
    pedidos = db.session.query(Pedido).all()
    return render_template('pedido/listar_pedidos.html', pedidos=pedidos)

@pedido_bp.route('/pedidos/novo', methods=['GET', 'POST'])
def novo_pedido():
    clientes = db.session.query(Cliente).all()
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        total = request.form['total']
        novo_pedido = Pedido(cliente_id=cliente_id, total=total)
        db.session.add(novo_pedido)
        db.session.commit()
        flash('Pedido criado com sucesso!', 'success')
        return redirect(url_for('pedido.listar_pedidos'))
    return render_template('pedido/cadastrar_pedido.html', clientes=clientes)

@pedido_bp.route('/pedidos/<int:id>/editar', methods=['GET', 'POST'])
def editar_pedido(id):
    pedido = db.session.query(Pedido).get_or_404(id)
    if request.method == 'POST':
        pedido.total = request.form['total']
        db.session.commit()
        flash('Pedido atualizado com sucesso!', 'success')
        return redirect(url_for('pedido.listar_pedidos'))
    return render_template('pedido/editar_pedido.html', pedido=pedido)

@pedido_bp.route('/pedidos/<int:id>/excluir', methods=['POST'])
def excluir_pedido(id):
    pedido = db.session.query(Pedido).get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    flash('Pedido excluído com sucesso!', 'success')
    return redirect(url_for('pedido.listar_pedidos'))
