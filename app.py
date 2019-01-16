from flask import Flask, request, jsonify, render_template
from machine_learning.modelo import Modelo
from  flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# ESSA FUNÇÃO RECEBE A REQUISIÇÃO E PROCESSA UTILIZANDO O MODELO DE MACHINE LEARNING
@app.route('/clusters', methods=['GET'])
def classify():
    #review = str(request.form['review'])
    #classifier = Modelo()
    #pred = classifier.execute(review)
    teste = [{'id':'1','name': 'Leanne Graham','username': 'Bret','email': 'Sincere@april.biz',},{'id':'2','name': 'Leanne Graham','username': 'Bret','email': 'Cuscuz',}]
    res = jsonify(teste)
    return res


# ESSA FUNÇÃO É EXECUTADA PARA RENDERIZAR PÁGINA HTML PARA TER UMA PRÉVIA DE COMO SERÁ A FUNCIONALIDADE DO MODELO MACHINE LEARNING
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("NOME_PROJETO/index.html")

    if request.method == 'POST':
        review = json.loads(request.data)["comment"]
        classifier = Modelo()
        pred = classifier.execute(review)
        res = jsonify({'review': review, 'predicao': pred[0]})
        return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
