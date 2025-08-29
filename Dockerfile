# Irá buildar em sequência, então as ordens dos fatores alteram o resultado
# Criará a imagem de minha aplicação com minhas configurações

#1° cria imagem
#2° especifica o diretório
#3° instala as bibliotecas
#4° copiar projeto no contêiner
#5° incia a aplicação


#slim-buster = versão mais leve baseada no Debian Buster, é a imagem a ser construída
FROM python:3.11-slim-buster

#Workdir - diretório padrão
#/app -  pasta do contêiner (da vvolumes: .:/app)
WORKDIR /app

#aqui o docker não precisa reinstalar toda vez que reinicia
COPY requirements.txt .

#Run executa comando do contêiner
#pip install - comando para installar
#--no-cache-dir - não armazena dados no cache do diretóro, isso deixa a image menor
# -r - acho que para read from file, ler dependências de arquivo
RUN pip install --no-cache-dir -r requirements.txt

#copia todo projeto para o contêiner
#1° "." todos os arquivos e pastas (da raiz do projeto)
#2° "." para pasta do workdir
COPY . .

#inicializar a aplicação
#CMD = comando
#será na linguagem py
#será na pasta app.py
CMD ["python","app.py"]
