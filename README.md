# Template API FLASK + Python

Esse é um template para desenvolvimento de API's utilizando Flask + Python

![alt text](https://instructobit.com/posts/111/post_preview_image(111).jpg)

## Setup
* git clone https://gitlab.com/trustvox/ai/template-api-flask.git
* cd template-api-flask
- Dica: utilize uma virtual env para melhor organizar as dependências:

      $ conda create --name nome_env python= versão_python
      $ conda activate nome_env

* pip install -r requirements.txt
* adicionar e configurar modelo de i.a em ./machine_learning/modelo.py
* configurar app.py para utilizar o modelo
* pode adicionar mais arquivos ao projeto caso necessário
* altere o arquivo ./static/js/index.js para integrar API com Html+JS

## Run
* python app.py
* Visit you app em http://localhost:5000

## Deploy
- No arquivo ./playbooks/deploy.yml substituir NOME_PROJETO pelo nome do seu projeto
- Alterar o número da porta no arquivo ./playbooks/deploy.yml
- Caso não esteja utilizando Python 3.6 pode alterar a versão no arquivo runtime.txt
- pip freeze > requirements.txt
- Execute o deploy passando a branch, e o ambiente de destino.

      $ bin/deploy staging master

* É preciso possuir o ansible instalado na máquina.


*Build with <3 by Trustvox Development Team*

*#Software Engineering <3*