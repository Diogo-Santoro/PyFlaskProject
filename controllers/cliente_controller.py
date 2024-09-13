from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Cliente import Cliente
from models import db
from werkzeug.security import generate_password_hash

cliente_bp = Blueprint('cliente', __name__)

# Cadastrar novo cliente
@cliente_bp.route('/clientes/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        endereco = request.form['endereco']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        telefone = request.form['telefone']

        if not nome or not email or not senha or not endereco or not cidade or not estado or not cep or not telefone:
            flash('Todos os campos são obrigatórios!', 'danger')
            return redirect(url_for('cliente.cadastrar_cliente'))

        senha_hash = generate_password_hash(senha)

        novo_cliente = Cliente(
            nome=nome,
            email=email,
            senha=senha_hash,
            endereco=endereco,
            cidade=cidade,
            estado=estado,
            cep=cep,
            telefone=telefone
        )
        db.session.add(novo_cliente)
        db.session.commit()

        flash('Cliente cadastrado com sucesso!', 'success')
        return redirect(url_for('cliente.listar_clientes'))

    return render_template('clientes/cadastrar_cliente.html')

# Listar clientes
@cliente_bp.route('/clientes')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/listar_clientes.html', clientes=clientes)
