# Projeto

### docker-compose

Define TODOS serviços do projeto e como se relacionam
traz isolamento - cada banco de dados, app, roda me seu contêiner (local isolado)

reprodução - qualquer pessoa terá o mesmo ambiente, incluindo as versões

facilidade - único comando para rodas, gerenciar ou derrubar o programa

compose.yaml é raiz do projeto, deve estar na pasta raiz (komicanto)

### requirementes.txt

Define as depend~encias Python

local : pasta raiz do projeto

lista todas bibliotecas co suas versões

para anter padrão entre todos desenvolvedores e usuários

sua instalação está no Dockerfile

### Flask

Micro Framework ()

lista rotas, requisições  http, renderização de templates html

### SQLAlchemy

biblioteca OR (object relational mapper) - mapeamento de objeto relacional

faz integração do banco de dados

### psycopg2-binary

adaptador .py para usar postgres com classes e objetos?

