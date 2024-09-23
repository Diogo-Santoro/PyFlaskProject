from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Avaliacao import Avaliacao
from models.Cliente import Cliente
from models.Produto import Produto
from models import db

avaliacao_bp = Blueprint('avaliacao', __name__)

@avaliacao_bp.route('/avaliacoes')
def listar_avaliacoes():
    avaliacoes = db.session.query(Avaliacao).all()
    return render_template('avaliacoes/listar_avaliacoes.html', avaliacoes=avaliacoes)

@avaliacao_bp.route('/avaliacoes/novo', methods=['GET', 'POST'])
def nova_avaliacao():
    clientes = db.session.query(Cliente).all()
    produtos = db.session.query(Produto).all()
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        produto_id = request.form['produto_id']
        nota = request.form['nota']
        comentario = request.form['comentario']
        nova_avaliacao = Avaliacao(cliente_id=cliente_id, produto_id=produto_id, nota=nota, comentario=comentario)
        db.session.add(nova_avaliacao)
        db.session.commit()
        flash('Avaliação registrada com sucesso!', 'success')
        return redirect(url_for('avaliacao.listar_avaliacoes'))
    return render_template('avaliacoes/cadastrar_avaliacao.html', clientes=clientes, produtos=produtos)

@avaliacao_bp.route('/avaliacoes/<int:id>/editar', methods=['GET', 'POST'])
def editar_avaliacao(id):
    avaliacao = db.session.query(Avaliacao).get_or_404(id)
    clientes = db.session.query(Cliente).all()
    produtos = db.session.query(Produto).all()
    if request.method == 'POST':
        avaliacao.cliente_id = request.form['cliente_id']
        avaliacao.produto_id = request.form['produto_id']
        avaliacao.nota = request.form['nota']
        avaliacao.comentario = request.form['comentario']
        db.session.commit()
        flash('Avaliação atualizada com sucesso!', 'success')
        return redirect(url_for('avaliacao.listar_avaliacoes'))
    return render_template('avaliacoes/editar_avaliacao.html', avaliacao=avaliacao, clientes=clientes, produtos=produtos)

@avaliacao_bp.route('/avaliacoes/<int:id>/excluir', methods=['POST'])
def excluir_avaliacao(id):
    avaliacao = db.session.query(Avaliacao).get_or_404(id)
    db.session.delete(avaliacao)
    db.session.commit()
    flash('Avaliação excluída com sucesso!', 'success')
    return redirect(url_for('avaliacao.listar_avaliacoes'))
