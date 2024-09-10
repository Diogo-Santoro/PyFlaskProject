class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/ecommerce_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    import os
    SECRET_KEY = os.urandom(24)  # Defina uma chave secreta aqui