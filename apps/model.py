
from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

dict_servicos = [
    {"categoria": "confecção", "tipo": "camiseta", "sexo": "feminina", "servico": " ","detalhe": "confecção de camiseta com gola careca, manga curta, justo"},
    {"categoria": "customização", "tipo": "camiseta", "sexo": "feminina", "servico": "estamparia", "detalhes": "estampa com nome ADS impacta"},
    {"categoria": "conserto", "tipo": "camiseta", "sexo": "feminina", "servico": "costurar lateral descosturada","detalhe": " "},
    {"categoria": "conserto", "tipo": "blazer", "sexo": "masculino", "servico": "troca de forro","detalhe": "Forro de cetin preto"}
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


#_________________ CRIAR TABELAS_________________________________________________________


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
    
    #1° criar nova classe que receberá irá interagir com o bd (classe de sessão)
    #sessionmaker() = função cria novas classes de sessão
    #bind=engine = qualquer sessão criada estará, automaticanete, conecta ao bd
    #1° será a classe, o 2° variável que recebe a classe recém criada
    #cria uma área de trabalho temporária de interação entre .py e bd
    #Session é nome comumente usado
    Session = sessionmaker(bind=engine)
    session = Session()
    
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
    
    #sempre fechar sessão depois de abrir
    session.close()



