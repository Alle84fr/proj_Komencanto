
from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm.exc import NoResultFound

dict_servicos = [
    {"categoria": "confecção", "tipo": "camiseta", "sexo": "feminina", "servico": " ","detalhes": "confecção de camiseta com gola careca, manga curta, justo"},
    {"categoria": "customização", "tipo": "camiseta", "sexo": "feminina", "servico": "estamparia", "detalhes": "estampa com nome ADS impacta"},
    {"categoria": "conserto", "tipo": "camiseta", "sexo": "feminina", "servico": "costurar lateral descosturada","detalhes": " "},
    {"categoria": "conserto", "tipo": "blazer", "sexo": "masculino", "servico": "troca de forro","detalhes": "Forro de cetin preto"}
]

# declarative_base = função, método. Conceito do SQLAlchemy que irá representar as tabelas de dados, local onde as tabelas (metadados - inforações sobre a estrutura- ficam), mapea atributos da classe .py, permite que gere comandos SQL como CREATE TABEL, SELECT ...
# o nome da variável inicia com B maiúsculo porque esta função tem a ação de criar novas classe (como se fossem objetos no java), e como classe tem início com letra maiúscula, o nome desta variável, que recebe nova classe, terá letra maiúscula
#BASE é o nome padrão usado

Base = declarative_base()

#_________________ CONFIGURAR TABELAS____________________________________________________


#cada atribuição é uma tabela
class Servico(Base):
    
    #atributo especial (dunder attribute) para mapear dados da tebala, ex nome dela. Liga .py ao bd
    # o nome da tabela será serviço
    __tablename__ = "servicos"
    
    #resuindo sem ser na ordem, aqui o a coluna id terá o tipo inteiro, será PK (primary key) e será gerada automaticamente.
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    #coluna categoria será do tipo texto, com máximo de 50 caracteres
    categoria = Column(String(50))
    
    tipo = Column(String(50))
    
    sexo = Column(String(50))
    
    servico = Column(String(250))
    
    detalhes = Column(String(255))
    
    #função (acho que método é mais para java) especial (dunder method) que representação oficial em string do objeto
    #self = próprio parâmetro (classe Servico), se auto chama
    #retorno dela seria como um "print(f"id = {valor de id}...")"
    # está dentro de <> por ser representação oficial(de um objeto), não uma comum
    def __repr__(self):
        return f"<Servico(id = {self.id}, categoria = {self.categoria}, tipo = {self.tipo}, sexo = {self.sexo}, servico = {self.servico}, detalhes = {self.detalhes})>"


#_________________ GERENCIADOR DE BD ______________________________________________________

def get_smk(engine):
    #função retorna a classe
    #1° criar nova classe que receberá irá interagir com o bd (classe de sessão)
    #sessionmaker() = função cria novas classes de sessão
    #bind=engine = qualquer sessão criada estará, automaticanete, conecta ao bd
    #1° será a classe, o 2° variável que recebe a classe recém criada
    #cria uma área de trabalho temporária de interação entre .py e bd
    #Session é nome comumente usado
    return sessionmaker(bind=engine)
    

#_________________ CRIAR TABELAS___________________________________________________________


#função de inicialização do bd
#recebe engenir (quem conecta .py ao bs) como args
#cria as tabelas 
def criar_tabela(engine):
    #classe mãe.atributo(características).método(ação)
    #Vá onde guarda os dados (Base), na parte de catálogos de tabelas criadas (metadado) e crie todas (create_all)
    Base.metadata.create_all(engine)
    

#_________________ PREENCHER TABELAS/ TRATAMENTO_______________________________________


# coloca os dados do dict_servicos, SOMENTE SE A TABELA ESTIVER VAZIA
def preencher_tabela(engine):
    
    
    Session = get_smk(engine)
    session = Session()
    
    try:
        # se (query) consuta da interação, com dados da classe serviço, for igual a "vazia"
        if session.query(Servico).count() == 0:
            #para cada dados_serviço no dicionário feito anterioremente
            for dados_servico in dict_servicos:
                novo_servico = Servico(
                    #variável categoria recebe = o dado_servico[na chave "categoria"]
                    categoria = dados_servico["categoria"],
                    tipo = dados_servico["tipo"],
                    sexo = dados_servico["sexo"],
                    servico = dados_servico["servico"],
                    detalhes = dados_servico["detalhes"]
                )

                #add novos serviços à sessão
                session.add(novo_servico)
                
            #confirmando
            session.commit()
    finally:
        #sempre fechar sessão depois de abrir
        session.close()
        
#______________________________________CRUD ____________________________________________

#_________________ GET ALL

def get_all_serv(engine):
    Session = get_smk(engine)
    session = Session()
    try:
        return session.query(Servico).all()
    finally:
        session.close()
    

#_________________ GET ID

def get_id_serv(engine, serv_id):
    Session = get_smk(engine)
    session = Session()
     
    try:
        # session - área de trabalho, interface entre .py e bd
        # query pesquisa
        # Serviço - classe file model.py
        # filter_by(valor) - filtrar pelo valor informado
        # variável id recebe serv_id
        # método que retorna apenas um único resultado
        return session.query(Servico).filter_by(id = serv_id).one()
    except:
        return None
    finally:
        # aqui é close, não closer
        session.close()
    
#_________________ POST

def put_serv(engine, add_serv):
    Session = get_smk(engine)
    session = Session()
    
    try:
        #** passa os dados do dict para a classe Servico
        novo_serv = Servico(**add_serv)        
        session.add(novo_serv)
        session.commit()
        return novo_serv.id
    finally:
        session.close()

#_________________ UPDATE

def update_serv(engine, serv_id, atualizar_serv):
    Session = get_smk(engine)
    session = Session()
    try:
        #.one_or_none é mais seguro que on()first(), porque  retorna ainstância ou não retona
        servicos = session.query(Servico).filter_by(id = serv_id).one_or_none()
        if servicos:
            for key, value in atualizar_serv.items():
                setattr(servicos, key, value)
            session.commit()
            return True
        return False
    finally:
        session.close()

#_________________ DELETE

def del_serv(engine, serv_id):
    Session = get_smk(engine)
    session = Session()
    try:
        servicos = session.query(Servico).filter_by(id = serv_id).first()
        if servicos:
            session.delete(servicos)
            session.commit()
            return True
        return False
    finally:
        session.close()

#apps/model.py