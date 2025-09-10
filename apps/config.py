#guarda inforações ad api e bd

#biblioteca para interagir com sistema operacional
import os
from sqlalchemy import create_engine

class Config:
    #DATABASE = banco de dados
    #URL - endereço -: postgresql://user:senha@db:5432portaPadrãoDoPostgreSQL/nome bd do envviroment
    # método get() tem dois parâmetros (chave que deve procurar, valor padrão (opcinal), caso não encontre a chave)
    # esta classe de conexão com o banco de dados
    #lê o ambinete do banco de dados
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://admin:17539@localhost:5432/komincanto_bd")

def get_engine():
    return create_engine(Config.DATABASE_URL)

#apps/config.py