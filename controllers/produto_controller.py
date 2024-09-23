from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Produto import Produto  # Importar a classe Produto corretamente
from models.Categoria import Categoria  # Importar a classe Categoria corretamente
from models import db

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produtos')
def listar_produtos():
    produtos = db.session.query(Produto).all()
    return render_template('produto/listar_produtos.html', produtos=produtos)

@produto_bp.route('/produtos/novo', methods=['GET', 'POST'])
def cadastrar_produto():
    categorias = db.session.query(Categoria).all()
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        estoque = request.form['estoque']
        categoria_id = request.form['categoria_id']
        produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque=estoque, categoria_id=categoria_id)
        db.session.add(produto)
        db.session.commit()
        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('produto.listar_produtos'))
    return render_template('produto/cadastrar_produto.html', categorias=categorias)

@produto_bp.route('/produtos/<int:id>/editar', methods=['GET', 'POST'])
def editar_produto(id):
    produto = db.session.query(Produto).get_or_404(id)
    categorias = db.session.query(Categoria).all()
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']
        produto.preco = request.form['preco']
        produto.estoque = request.form['estoque']
        produto.categoria_id = request.form['categoria_id']
        db.session.commit()
        flash('Produto alterado com sucesso!', 'success')
        return redirect(url_for('produto.listar_produtos'))
    return render_template('produto/editar_produto.html', produto=produto, categorias=categorias)

@produto_bp.route('/produtos/<int:id>/excluir', methods=['POST'])
def excluir_produto(id):
    produto = db.session.query(Produto).get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('produto.listar_produtos'))
