from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Usuario, Pedido, Rota
import datetime

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    #Para obter o ano atual
    current_year = datetime.datetime.now().year
    # Passa a variavel 'year' para o template index.html
    return render_template('index.html', year=current_year)

@routes.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template('registrar.html')

@routes.route('/login')
def login():
    return render_template('login.html')

# Implemente outras rotas para login, criação de pedidos, cálculo de rotas, etc.