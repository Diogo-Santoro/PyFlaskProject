from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.Cliente import Cliente

cliente_bp = Blueprint('cliente', __name__)

# Listar clientes
@cliente_bp.route('/clientes')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('listar_clientes.html', clientes=clientes)

# Cadastrar novo cliente
@cliente_bp.route('/clientes/novo', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cliente = Cliente(nome=nome, email=email, telefone=telefone)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('cliente.listar_clientes'))
    return render_template('cadastrar_cliente.html')

# Editar cliente
@cliente_bp.route('/clientes/<int:id>/editar', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.email = request.form['email']
        cliente.telefone = request.form['telefone']
        db.session.commit()
        return redirect(url_for('cliente.listar_clientes'))
    return render_template('editar_cliente.html', cliente=cliente)

# Excluir cliente
@cliente_bp.route('/clientes/<int:id>/excluir', methods=['POST'])
def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('cliente.listar_clientes'))
