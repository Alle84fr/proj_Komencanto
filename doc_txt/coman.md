### Teste docker

ctrl j = abre terminal no vscode

deve estar na raiz da pasta (proj_komecanto)

caminho PS C:\Users\a\Documents\python_geral\proj_Komencanto>

cd nomePasta = para entrar em uma pasta

cd .. para voltar um pasta

fora do VSCode, abrir Docker file( se não abrir dará erro)

// lê o docker-compose

- docker-compose -f docker-compose.yaml config 

saída poser ser assim
docker compose -f docker-compose.yaml config
name: proj_komencanto
services:
  db:
    environment:
      POSTGRES_DB: komicanto_db
      POSTGRES_PASSWORD: "123987"
      POSTGRES_USER: admin
    image: postgres:14-alpine
    networks:
      default: null
    restart: always
    volumes:
      - type: bind
        source: C:\Users\arfur\Documents\python_geral\proj_Komencanto\data\db
        target: /var/lib/postgresql/data
        bind:
          create_host_path: true
  web:
    build:
      context: C:\Users\arfur\Documents\python_geral\proj_Komencanto
      dockerfile: Dockerfile
    depends_on:
      db:
        condition: service_started
        required: true
    networks:
      default: null
    ports:
      - mode: ingress
        target: 5000
        published: "5000"
        protocol: tcp
    restart: always
    volumes:
      - type: bind
        source: C:\Users\arfur\Documents\python_geral\proj_Komencanto
        target: /app
        bind:
          create_host_path: true
networks:
  default:
    name: proj_komencanto_default

segundo teste - subir os contêiners

- docker compose -f docker-compose.yaml up --build

erro
failed to solve: process "/bin/sh -c pip install --no-cache-dir -r requirements.txt" did not complete successfully: exit code: 1

docker não subiu um ou mais pacotes, pode ser pacote não atualizado, inexistente, etc

web-1 exited with code 2
web-1 -> nome do contêiner de aplicação web, -1 é a instância
exited with code 2 - app.py não foi encontrada

-docker compose -f docker-compose.yaml down

depois que para docker rodar para remover os contêineres e a rede criada (mas manter os dados do banco de dados 
