# PROJETO DE PLATAFORMA WEB SIMPLES COM LOGIN.

# login, cadastramento,leitura, atualização, deleção.



## TECNOLOGIAS: 

* flask
* python
* html
* css
* bootstrap-v5
* mysql
* sqlalchemy
* flask-login


## NOME DO BANCO: 
- storage.db

## NOME DA TABELA: 
- info

## COLUNAS: 
- name
- email 
- password 
- id



## comandos
- para criar ambiente virtual=> python -m venv environment
- para ativar venv => cd environment > scripts\activate
- para instalar modulos=> pip install -r requirements.txt
- para salvar os modulos=> pip freeze> requirements.txt
- para rodar projeto ==> python ./run.py

## criar a entidade no bco mysql com ORM sqlalchemy==2 =>
* db.create-all()

## criar a entidade no bco mysql com ORM sqlalchemy==3 =>
* with app.app_context():
*    db.create_all()



## comando para criação de tabelas no bco mysql ==>

´´´

CREATE TABLE IF NOT EXISTS info(
    name text(50) NOT NULL,
    email text(100) NOT NULL,
    password text(128) NOT NULL,
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY(id)
)

´´´
