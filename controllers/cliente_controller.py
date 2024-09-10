from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Cliente, db

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('cliente/listar_clientes.html', clientes=clientes)

@cliente_bp.route('/clientes/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
        db.session.add(novo_cliente)
        db.session.commit()

        flash('Cliente cadastrado com sucesso!', 'success')
        return redirect(url_for('cliente.listar_clientes'))
    return render_template('cliente/cadastrar_cliente.html')

@cliente_bp.route('/clientes/editar/<int:cliente_id>', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.email = request.form['email']
        cliente.telefone = request.form['telefone']
        db.session.commit()

        flash('Cliente editado com sucesso!', 'success')
        return redirect(url_for('cliente.listar_clientes'))
    return render_template('cliente/editar_cliente.html', cliente=cliente)

@cliente_bp.route('/clientes/excluir/<int:cliente_id>', methods=['POST'])
def excluir_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente excluído com sucesso!', 'success')
    return redirect(url_for('cliente.listar_clientes'))
