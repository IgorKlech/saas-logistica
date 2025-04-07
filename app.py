from flask import Flask
from routes import routes
from models import db, Usuario  # Importe seu modelo de Usuário
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Configuração do Banco de Dados (substitua com suas informações)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cybersapo:Sapo1513@localhost:5432/conexao_logistica_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'S@po1513' # Defina uma chave secreta para segurança

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes.login' # Define a rota para a página de login

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, int(user_id)) # Função para carregar o usuário pelo ID

app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)