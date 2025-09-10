
<br>
<br>

# Git, Github, alguns comandos

Resumo de alguns comandos, básicos, do git/gitHub.
<br>
<br>

### 𓃦 Git:

Sistema de controle de versão do código = versionamento.

Registra mudanças realizadas no código e as mantém organizadas.

Sistema distribuído = código possui histórico completo que pode ser - compartilhado, usado e modificado por outros desenvolvedores .
<br>
<br>

### 𓃢 GitHub:

Plataforma online, para salvar os repositório (remoto), públicos ou privados.
<br>
<br>

### 𓃡 Commit:

Promessa de envio de uma nova versão do projeto.

Registra um ponto onde houve mudanças
<br>
<br>

### 𓄿 Branch:

A branch Main/master é o braço, ou a linha principal do projeto. Ela recebe as outras linhas/branches do projeto.

A branch que vai para produção

Geralmente, para não ter problemas nos projetos, os desenvolvedores utilizam outra branch para criar e testar os códigos e só depois juntam( merge) à branch principal
<br>
<br>

### 𓅯 Origin:

Nome, apelido dado para o url do git

Ao invés de ter de sempre digitar todo url, usa-se a palavra origin no lugar do endereço URL
<br>
<br>

### 𓅰 Comando para configurar o git local ao remoto
<br>

<b>--global </b>
<br>

Irá modificar todos os repositório, deste para os diante.

SEM POR --global = irá modificar apenas o <u> repositório em questão </u>
<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Configuração de e-mail</b>

<span style="color:#119da4;font-size: 21px">git config --global user.email "e-mail"</span>

git config --global user.email "alle@gmail.com"

<span style="color:#119da4;font-size: 21px">git config user.email "e.mail"</span>
<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Configuração do usuário</b>

<span style="color: #3f8efc;font-size: 21px">git config --global user.name "nome"</span>

git config --global user.name "Alle"

git config user.name "Alle"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Verificar usuário e e-mail</b>

<span style="color:#947bd3;font-size: 21px">git config user.name</span>

<span style="color:#947bd3;font-size: 21px">git config user.email</span>
<br>
<br>

### 𓅮 Comando iniciar novo projeto:

<b>1° no gitHub - Temos algumas formas de iniciar:</b>


- Your profile

    - image

    - Repositories

    - image
<br>

- Dashboard
    - image

Em REPOSITORY NAME ➪ colocar o nome do projeto.

No caso deste bootcamps coloquei dio_riach.

DESCRIPTION ➪ breve descrição do projeto, deixei em branco

CONFIGURATION - CHOOSE VISIBILITY ➪ para escolher entre público (todos podem ver e mexer no projeto) - escolhi público

privado (apenas o criador e seus colaboradores podem ver e atuar no projeto)

ADD README ➪ README.md é capa do projeto, nele estão informações do que é o projeto, tecnologias usadas, estrutura do projeto, autores e outras informações.

Eu não coloco (deixo no off), pois, ao final do projeto e costumo criar o meu próprio, direto do GitHub, para não ter problemas de configuração.

ADD GITIGNORE ➪ Gitignore é uma pasta com conteúdos que deverão ser ignorados na hora de commitar e dar push, já tive de usar, mas, geralmente deixo No.gitignore

ADD LINCENSE ➪ diria que é como outros pode usar, divulgar o conteúdo, se tem permissão de atuar no projeto.

Esta parte não tenho muitos conhecimentos, mas, quando coloco eu ponho MIT License - pessoa pode usar mas deve informar que é seu

O mais adequado é estudar cada uma delas e ver qual se adequa ao tipo de projeto.

Com tudo já escolhido é só clicar em ➪ CREATE REPOSITORY

Após esta ação, irá abrir a página do repositório, nela <b>haverá um quadro, que possui o endereço HTTPS do projeto,<span style="color: #b1740f">copiar, guardar este endereço</span></b> para poder clonar ou incializar o repositório local, no computador.
<br>

<b>2° A - no computador, comando para projeto <u>vazio</u>, como o criado a cima:</b>

Abrir o IDE que deseja usar, neste caso darei exemplo no VSCode para poder usar os comandos, sem atalhos, já que Intellij há atalhos.

Não irei detalhar como se cria um projeto novo, mas eu escolho a pasta que desejo

- No terminal

cd é comando para entrar em uma pasta

<span style="color:#119da4;font-size: 21px"> cd .\Documents\ </span>

cd .. é comando para sair/voltar uma pasta

<span style="color:#119da4;font-size: 21px"> cd ..

Comando para criar uma pasta, se necessário

<span style="color:#3f8efc;font-size: 21px"> mkdir nome_da_pasta</span>

Observação, caso dê erro, observar se uma mensagem do Windows aparece, nela você pode mudar a permissão desta pasta

- criar pasta, entrar, abrir a pasta nomeada como java_dio

<span style="color:#947bd3;">mkdir java_dio</span>

<span style="color:#947bd3;">cd java_dio</span>

Comando para abrir Windows do projeto, entrar de fato no projeto (apenas para vscode)

<span style="color:#947bd3;">code .</span>

<b>comando para iniciar a criação de repositório local, <u>vazio, no computador</u></b>

git init

// para conectar o repositório remoto ao repositório local

// traduzo assim, git pega do repositório remoto e adiciona, relaciona à palavra origin este url

git remote add origin url

(git remote add origin https://github.com/Alle84fr/Dio_riachu.git)

Agora comece a usar e codificar, seu repositório local já está adicionado



2° B - computador - comando para clonar projeto, quando já possui alguma dado:
// comando que irá dar um pull, trazer tudo que já foi criando e "postado" no repositório remoto/nuvem.

git clone url

(git clone https://github.com/Alle84fr/Dio_riachu.git)



3° Status, add, commit, push:
O ideal é de tempos em tempos, adicionar o que está fazendo a área do staged (área em que os arquivos ficam esperando comando de commit ou delete, se precisar).

-> para sabe -- nome da branch em que está

-- Changes to be comitted - mudanças já adicionadas que poderão ser commitadas, já estão no staged(local de espera)

-- Changes not Staged for commit - arquivos que o git já rastreou, ex, já foi adicionado anteriormente, mas tiveram modificações que não foram adicionadas

-- Untracked files - arquivos novos ainda não rastreados, não adicionados anteriormente.

git status

-> adicionar um único arquivo

git add nome_file.extensão

git add aula1.txt

-> mais de um arquivo, observe que há um espeço entre os nomes

git add nome_file.extensão nome_file.extensão

git add aula1.py aula2.py README.md

-> todos os arquivos de uma vez

git add .

-> commitar, deixar tudo pronto para envio ao repositório remoto

git commit -m "texto"

observações sobre commit

se abrir uma aspa, escrever uma linha e der enter, irá criar nova linhas, só será considerado fim do comentário do commit, quando a segunda aspas for posta
ex: git commit -m "Add file1

add file 2"

alguns verbos do commit usados para identificar o que foi feito no código
-- add = quando foi adicionado novos arquivos, funcionalidades, branches .....

-- fix - quando se corrigiu u bug

-- update - atualização, porém sem correção de bugs

-- remove - removeu, deletou algo

-- rename - renomeou algo como, variável, função, file, folder ....

-- refactor - melhoria do código, sem corrigir erros

-- move - moveu arquivo, código para outro lugar

-- merge - mesclou as merges

-- revert - desfez alteração

Atenção, commit diz o foi feito, então é bom nomear de forma clara, direta, e que ao ler saiba o que foi, ou onde foi feito a modificação

Curiosidade -m é atalho para mensagem ou nomear, neste caso, mensagem

-> enviar modificações do repositório local para remoto - push

// enviar uma branch local

git push origin nome_branch

(git push origin main)

(git push origin alle)

// enviar todas as branches local

git push --all

git push -a


Outros comandos:


+ Atualizar branch

-> trazer a branch remota para local, uma única

git pull origin nome_branch

-> trazer todas brancas (pode trazer conflitos)

git pull --all

-> trazer trodas infromações, SEM MESCLAR

git fetch --all


+ Branch:
-> saber todas as branches local

// a branch em que está terá um * antes do nomes

git branch

-> saber todas as branches, local e remota

// curiosidade o -a é de all, todas

git branch -a

-> mudar nome da branch

git branch -m novo_nome_branch

// o nome era main e agora será master

(git branch master)

-> criar branch sem entrar direto na nova branch

git branch nome_nova_branch

(git branch alle)

-> mudar de branch

// estava na branch main e quero ir para alle

git checkout nome_branch

(git checkout alle)

-> ciar uma branch e no mesmo comando ir para a nova branch

// -b de branch, comando que faz mudar a branch "automaticamente"

// ao dar enter, irá criar a branch e logo em seguida sair da main para lua, por exemplo

git checkout -d nome_branch

(git checkout -b lua)

-> enviar as branches para repositório remoto

// -u é atalho para o comando --set-upstream, conecta branch local à remota

git push origin -u nome_nova_branch

(git push origin -u alle lua)

-> copiar branch original (que será copiada) em outra branch destino (que receberá a cópia)

ATENÇÃO - SOBRESCEVE TODOS OS ARQUIVOS ATUAIS

// reset - desfaz alterações no histórico de commits

// --hard remove as alterações do diretório, staging e do commit

// quero deixar a branch alle exatamente igual a branch lua

1° estar na branch de destino, que receberá a cópia, para isso pode usar comando de mudar de branch

2°comando - git reset --hard nome_branch_original

// já está dentro da branch lua

(git --hard alle)

-> copiar branch mantendo historio, se tiver arquivos diferentes irá manter-nos, já os que tiverem iguais, irá sobrescrever

// merge mescla as alterações

// --stategy-option para o git resolver o conflito de merge

// theirs branch original sobrescreve a branch destino

1° já estar na branch destino

2° código git merge branch_original --stategy-option theirs

-> deletar branch local

git branch -d nome_da_sua_branch

-> deletar branch remoto no terminal

git push origin :nome_da_sua_branch



+ Commit
-> verifica histórico de commits, mostra a hash SHA-1 completo (40 caracteres)

o short hash pega os 7 primeiros n°s do hash SHA completo

PARA SAIR DEVE DIGITAR q

// informa:

hash SHA , se este for o último commit feito terá (HEAD -> branch, orignal/main)

autor <e-mail>

data

mensagem do commit

git log

-> para verificar histórico de commits, mas de forma compacta (short hash)

// este não precisa teclar q para sair, sai direto

// informará:

short hash mensagem do commit

se for o último commit feito será short hash (HEAD -> branch , origin/main) mensagem commit

git log --oneline

-> remover último commit (o head)

// desfaz commit e remove alterações do staged

// as alterações permanecerão no diretório

git reset Head~1

-> remover commit permanentemente

git reset --hard HEAD~1

DEPOIS DE ALTERAR DEVE DAR UM DESTES COMANDO

// para atualizar o repositório remoto

git push origin nome_branch -f OU --force

git push --all --force

-> excluir commit específico, não sendo o último

// com git log ou git log --oneline vc pode ver qual hash

git rebase -i hash_do_commit

// abrirá editor de texto, como os commits, mais ou menos assim

pick 5c6c04a Adiciona nova feature de login

pick a2b3c4d Corrige bug de cadastro

// troque pick por drop

// ou deleta a linha

drop e1f2g3h Commits para teste

pick 4d5e6f7 Mais correções

pick 8a9b0c1 Atualiza arquivo de configuração

tecle:

w - salvar

ws - salvar e sair

q - desistir

depois deve dar um gir push --all --force ou git push origin nome_branch -f



+ Merge - fazer direto no remoto/nuvem/github
// PRINTS DO VIDEO "HOW TO MERGE GITHUB BRANCHES TO MASTER

image

image

image

image

SEM CONFLITO

image

image



COM CONFLITO

image

image

image

RESOLVE CO CONFLITO E DEPOIS DÁ MARK AS RESOLVED

