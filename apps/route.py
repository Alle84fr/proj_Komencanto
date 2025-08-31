#rotas

from flask import Blueprint, render_template
from config import get_engine as getEn
from model import Servico
from sqlalchemy.orm import sessionmaker

bp = Blueprint("main", __name__)

#________________________________ DEFININDO ROTAS _______________________________________

@bp.route("/", methods=["GET"])

def rota_pricipal():
    #função para que busca dados do bd e envia para pag web
    #criar a conexão entre py e bd
    # eng = engine
    #Session expplicado em model.py
    eng = getEn()
    Session = sessionmaker(bind=eng)
    session = Session()

    #_________________ Consulta todos dados

    servicos = session.query(Servico).all()

    #_________________ Fechar sessão

    session.close()

    #_________________ Renderização

    # index refere-se à pag inicial, principal
    return render_template("index.html", servicos = servicos)