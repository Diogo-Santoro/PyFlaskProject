from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar todas as entidades individuais
from .Cliente import Cliente
from .Categoria import Categoria
from .Produto import Produto
from .Pedido import Pedido
from .PedidoItem import PedidoItem
from .Avaliacao import Avaliacao
from .Favorito import Favorito
from .Pagamento import Pagamento
from .Carrinho import Carrinho