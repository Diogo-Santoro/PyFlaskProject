from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Cliente import Cliente
from models import db

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes')
def listar_clientes():
    clientes = db.session.query(Cliente).all()
    return render_template('clientes/listar_clientes.html', clientes=clientes)

@cliente_bp.route('/clientes/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']  # Capturar a senha do formulário
        endereco = request.form['endereco']
        
        # Verificar se a senha foi fornecida
        if not senha:
            flash('A senha é obrigatória.', 'danger')
            return redirect(url_for('cliente.cadastrar_cliente'))

        cliente = Cliente(nome=nome, email=email, senha=senha, endereco=endereco)  # Adicionar a senha ao objeto Cliente
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente cadastrado com sucesso!', 'success')
        return redirect(url_for('cliente.listar_clientes'))
    return render_template('clientes/cadastrar_cliente.html')

@cliente_bp.route('/clientes/editar/<int:cliente_id>', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    cliente = db.session.query(Cliente).get_or_404(cliente_id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.email = request.form['email']
        cliente.senha = request.form['senha']  # Capturar a nova senha
        cliente.endereco = request.form['endereco']
        db.session.commit()
        flash('Cliente editado com sucesso!', 'success')
        return redirect(url_for('cliente.listar_clientes'))
    return render_template('clientes/editar_clientes.html', cliente=cliente)

@cliente_bp.route('/clientes/excluir/<int:cliente_id>', methods=['POST'])
def excluir_cliente(cliente_id):
    cliente = db.session.query(Cliente).get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente excluído com sucesso!', 'success')
    return redirect(url_for('cliente.listar_clientes'))
