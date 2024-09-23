from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Pagamento import Pagamento
from models.Pedido import Pedido
from models import db

pagamento_bp = Blueprint('pagamento', __name__)

@pagamento_bp.route('/pagamentos')
def listar_pagamentos():
    pagamentos = db.session.query(Pagamento).all()
    return render_template('pagamentos/listar_pagamentos.html', pagamentos=pagamentos)

@pagamento_bp.route('/pagamentos/novo', methods=['GET', 'POST'])
def novo_pagamento():
    pedidos = db.session.query(Pedido).all()
    if request.method == 'POST':
        pedido_id = request.form['pedido_id']
        valor = request.form['valor']
        metodo_pagamento = request.form['metodo_pagamento']
        novo_pagamento = Pagamento(pedido_id=pedido_id, valor=valor, metodo_pagamento=metodo_pagamento)
        db.session.add(novo_pagamento)
        db.session.commit()
        flash('Pagamento registrado com sucesso!', 'success')
        return redirect(url_for('pagamento.listar_pagamentos'))
    return render_template('pagamentos/cadastrar_pagamento.html', pedidos=pedidos)

@pagamento_bp.route('/pagamentos/<int:id>/editar', methods=['GET', 'POST'])
def editar_pagamento(id):
    pagamento = db.session.query(Pagamento).get_or_404(id)
    pedidos = db.session.query(Pedido).all()
    if request.method == 'POST':
        pagamento.valor = request.form['valor']
        pagamento.pedido_id = request.form['pedido_id']
        pagamento.metodo_pagamento = request.form['metodo_pagamento']
        db.session.commit()
        flash('Pagamento atualizado com sucesso!', 'success')
        return redirect(url_for('pagamento.listar_pagamentos'))
    return render_template('pagamentos/editar_pagamento.html', pagamento=pagamento, pedidos=pedidos)

@pagamento_bp.route('/pagamentos/<int:id>/excluir', methods=['POST'])
def excluir_pagamento(id):
    pagamento = db.session.query(Pagamento).get_or_404(id)
    db.session.delete(pagamento)
    db.session.commit()
    flash('Pagamento excluído com sucesso!', 'success')
    return redirect(url_for('pagamento.listar_pagamentos'))
