#rotas

from flask import Blueprint, render_template, request, jsonify, abort
from apps.config import get_engine as getEn
import apps.model as mod
import http

# bp =  blueprint
# aqui será o "link" entre rotas a app
bp = Blueprint("main", __name__)

#________________________________ DEFININDO ROTAS _______________________________________

#_________________ PAG PRINCIPAL GET

@bp.route("/", methods=["GET"])

def rota_pricipal():
    #função para que busca dados do bd e envia para pag web
    #criar a conexão entre py e bd
    # eng = engine
    #Session expplicado em model.py
    eng = getEn()
    servicos = mod.get_all_serv(eng)
    return render_template("index.html", servicos=servicos)

#_________________ PAG PRINCIPAL POST

@bp.route("/cadastro", methods=["GET", "POST"])
def rota_cadastro():
    if request.method == "POST":
        # get o dados
        dados_servico = {
            "categoria": request.form.get("categoria"),
            "tipo": request.form.get("tipo"),
            "sexo": request.form.get("sexo"),
            "servico": request.form.get("servico"),
            "detalhes": request.form.get("detalhes")
        }
        
        # valisar os dados
        if not all(dados_servico.values()):
            return render_template("cadastro.html", erro="Preencher todos os campos"), http.HTTPStatus.BAD_REQUEST

        eng = getEn()
        try:
            novo_servico_id = mod.put_serv(eng, dados_servico)
            return render_template("cadastro_feito.html", servico_id=novo_servico_id), http.HTTPStatus.CREATED
        except Exception as e:
            print(f"Erro ao criar serviço: {e}")
            return render_template("erro.html", mensagem="Falha ao criar o serviço, tente mais tarde"), http.HTTPStatus.INTERNAL_SERVER_ERROR
    
    #renderiza pag de cadastro
    return render_template("cadastro.html")

#Erros não encontrados
@bp.errorhandler(http.HTTPStatus.NOT_FOUND)
def pag_nao_encont(e):
    return render_template("erro.html", mensagem="Serviço não encontrado"), http.HTTPStatus.NOT_FOUND

#apps/route.py