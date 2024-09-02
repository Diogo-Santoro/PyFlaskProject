# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Produto
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# Consultar produtos
@app.route('/produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('listar_produtos.html', produtos=produtos)

from models import Categoria  # Não esqueça de importar a model de Categoria

@app.route('/produtos/novo', methods=['GET', 'POST'])
def cadastrar_produto():
    categorias = Categoria.query.all()  # Carrega todas as categorias do banco
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        estoque = request.form['estoque']
        categoria_id = request.form['categoria_id']
        produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque=estoque, categoria_id=categoria_id)
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('listar_produtos'))
    return render_template('cadastrar_produto.html', categorias=categorias)


@app.route('/produtos/<int:id>/editar', methods=['GET', 'POST'])
def editar_produto(id):
    produto = Produto.query.get_or_404(id)
    categorias = Categoria.query.all()  # Carrega todas as categorias do banco
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']
        produto.preco = request.form['preco']
        produto.estoque = request.form['estoque']
        produto.categoria_id = request.form['categoria_id']
        db.session.commit()
        return redirect(url_for('listar_produtos'))
    return render_template('editar_produto.html', produto=produto, categorias=categorias)

# Excluir produto
@app.route('/produtos/<int:id>/excluir', methods=['POST'])
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('listar_produtos'))

if __name__ == '__main__':
    app.run(debug=True)
