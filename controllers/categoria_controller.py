from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Categoria import Categoria  # Importar a classe Categoria corretamente
from models import db

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/categorias')
def listar_categorias():
    categorias = db.session.query(Categoria).all()  # Garantir que estamos acessando a classe corretamente
    return render_template('categoria/listar_categorias.html', categorias=categorias)

@categoria_bp.route('/categorias/cadastrar', methods=['GET', 'POST'])
def cadastrar_categoria():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        nova_categoria = Categoria(nome=nome, descricao=descricao)
        db.session.add(nova_categoria)
        db.session.commit()
        flash('Categoria cadastrada com sucesso!', 'success')  # Mensagem flash de sucesso
        return redirect(url_for('categoria.listar_categorias'))
    return render_template('categoria/cadastrar_categoria.html')

@categoria_bp.route('/categorias/editar/<int:categoria_id>', methods=['GET', 'POST'])
def editar_categoria(categoria_id):
    categoria = db.session.query(Categoria).get_or_404(categoria_id)
    if request.method == 'POST':
        categoria.nome = request.form['nome']
        categoria.descricao = request.form['descricao']
        db.session.commit()
        flash('Categoria editada com sucesso!', 'success')  # Mensagem flash de sucesso
        return redirect(url_for('categoria.listar_categorias'))
    return render_template('categoria/editar_categoria.html', categoria=categoria)

@categoria_bp.route('/categorias/excluir/<int:categoria_id>', methods=['POST'])
def excluir_categoria(categoria_id):
    categoria = db.session.query(Categoria).get_or_404(categoria_id)
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoria excluída com sucesso!', 'success')  # Mensagem flash de sucesso
    return redirect(url_for('categoria.listar_categorias'))
