from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Carrinho import Carrinho
from models.Cliente import Cliente
from models.Produto import Produto
from models import db

carrinho_bp = Blueprint('carrinho', __name__)

@carrinho_bp.route('/carrinhos')
def listar_carrinhos():
    carrinhos = db.session.query(Carrinho).all()
    return render_template('carrinhos/listar_carrinhos.html', carrinhos=carrinhos)

@carrinho_bp.route('/carrinhos/novo', methods=['GET', 'POST'])
def novo_carrinho():
    clientes = db.session.query(Cliente).all()
    produtos = db.session.query(Produto).all()
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        produto_id = request.form['produto_id']
        quantidade = request.form['quantidade']
        novo_carrinho = Carrinho(cliente_id=cliente_id, produto_id=produto_id, quantidade=quantidade)
        db.session.add(novo_carrinho)
        db.session.commit()
        flash('Produto adicionado ao carrinho com sucesso!', 'success')
        return redirect(url_for('carrinho.listar_carrinhos'))
    return render_template('carrinhos/cadastrar_carrinho.html', clientes=clientes, produtos=produtos)

@carrinho_bp.route('/carrinhos/<int:id>/editar', methods=['GET', 'POST'])
def editar_carrinho(id):
    carrinho = db.session.query(Carrinho).get_or_404(id)
    clientes = db.session.query(Cliente).all()
    produtos = db.session.query(Produto).all()
    if request.method == 'POST':
        carrinho.cliente_id = request.form['cliente_id']
        carrinho.produto_id = request.form['produto_id']
        carrinho.quantidade = request.form['quantidade']
        db.session.commit()
        flash('Carrinho atualizado com sucesso!', 'success')
        return redirect(url_for('carrinho.listar_carrinhos'))
    return render_template('carrinhos/editar_carrinho.html', carrinho=carrinho, clientes=clientes, produtos=produtos)

@carrinho_bp.route('/carrinhos/<int:id>/excluir', methods=['POST'])
def excluir_carrinho(id):
    carrinho = db.session.query(Carrinho).get_or_404(id)
    db.session.delete(carrinho)
    db.session.commit()
    flash('Carrinho excluído com sucesso!', 'success')
    return redirect(url_for('carrinho.listar_carrinhos'))
