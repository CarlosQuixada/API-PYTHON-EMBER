# ESSA CLASSE ARMAZENA AS FUNÇÕES RELACIONADAS AO MODELO DE MACHINE LEARNING UTILIZADO NO PROJETO
from processing.processing import PreProcessing
import pickle


class Modelo():
    def __init__(self):
        self.processo = PreProcessing()
        self.modelo, self.vectorizer = self.loadModelo()

    # ESSA FUNÇÃO É RESPONSAVEL POR CARREGAR MODELO DE MACHINE LEARNING
    def loadModelo(self):
        modelo = pickle.load(open('machine_learning/classificador.pkl', 'rb'))
        vectorizer = pickle.load(open('machine_learning/vectorizer.pkl', 'rb'))
        return modelo, vectorizer

    # ESSA FUNÇÃO É RESPONSAVEL POR EXECUTAR O MODELO DE MACHINE LEARNING
    def execute(self, review):
        review_classifier = []
        review_classifier.append(
            self.processo.Stemming(self.processo.removerAcentos(self.processo.removerStopWords(review))))
        freq_review = self.vectorizer.transform(review_classifier)
        print(freq_review)
        predicao = self.modelo.predict(freq_review)
        return predicao
