from models import db  # Importa o db da inicialização em models/__init__.py

class Produto(db.Model):
    __tablename__ = 'produtos'
    produto_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.categoria_id'), nullable=False)

    # Relacionamento com Categoria
    categoria = db.relationship('Categoria', backref='produtos')
