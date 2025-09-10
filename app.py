#equivalente ao método public static void main(String ... rags){}
# resumindo é o arquivo que será procurado para rodar todo o projeto
# aqui ele :
# inicializa
# chama funções
# define rotas

from flask import Flask, render_template
from apps.config import get_engine as getEn
import apps.model as mod
from apps.route import bp

#instanciando a classe Flask
#(__name__), é um ponto que referência, que linka a outro file
app = Flask(__name__)


#_________________________ CONFIGUARAÇÃK BD _____________________________________________

# explicação no route.py
eng = getEn()

mod.criar_tabela(eng)
mod.preencher_tabela(eng)

#_________________________ ROTAS BLUEPRINT ________________________________________________

# registro de rota, associando ao blueprint do rote.py
app.register_blueprint(bp)


#_________________________ INICIANDO SERVIDOR ___________________________________________

#ATÉ ONDE ENTEDI __MAIN__ SE CONECTA AO __NAME__ DO FILE ROTE
#inicializa se o file for o principal
if __name__ == "__main__":
    app.run(debug=True)
    
#app.py