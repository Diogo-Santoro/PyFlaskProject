from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Cliente import Cliente  # Importar a classe Cliente corretamente
from models import db

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes')
def listar_clientes():
    clientes = db.session.query(Cliente).all()
    return render_template('cliente/listar_clientes.html', clientes=clientes)

@cliente_bp.route('/clientes/novo', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cliente = Cliente(nome=nome, email=email, senha=senha)
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente cadastrado com sucesso!', 'success')
        return redirect(url_for('cliente.listar_clientes'))
    return render_template('cliente/cadastrar_cliente.html')

@cliente_bp.route('/clientes/<int:id>/editar', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = db.session.query(Cliente).get_or_404(id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.email = request.form['email']
        cliente.senha = request.form['senha']
        db.session.commit()
        flash('Cliente editado com sucesso!', 'success')
        return redirect(url_for('cliente.listar_clientes'))
    return render_template('cliente/editar_cliente.html', cliente=cliente)

@cliente_bp.route('/clientes/<int:id>/excluir', methods=['POST'])
def excluir_cliente(id):
    cliente = db.session.query(Cliente).get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente excluído com sucesso!', 'success')
    return redirect(url_for('cliente.listar_clientes'))
