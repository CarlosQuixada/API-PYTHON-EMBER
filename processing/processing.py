# ESSA CLASSE É UTILIZADA NA ETAPA DE LIMPEZA DE DADOS, É ONDE TEM TODAS AS FUNÇÕES PARA LIMPAR DADOS STRING
import nltk
import processing.Utils as Utils
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class PreProcessing():
    def __init__(self):
        self.__acentos = Utils.ACENTOS
        self.__s_acentos = Utils.S_ACENTOS
        self.stop_words = set(stopwords.words("portuguese"))
        self.more_stopwords = Utils.MORE_STOPWORDS

    # ESSA FUNÇÃO REMOVE AS STOPWORDS JÁ EXISTENTES NO NLTK E AS QUE FORAM ADICIONADAS NO ARQUIVO Utils.py
    def removerStopWords(self, texto):
        texto = ' '.join([word for word in word_tokenize(texto) if word not in self.stop_words])
        texto = ' '.join([word for word in word_tokenize(texto) if word not in self.more_stopwords])
        texto.replace(',', ' ').replace('.', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('"', '') \
            .replace('*', ' ').replace('#', ' ').replace('%', ' ').replace('  ', ' ').lower()
        return texto

    # ESSA FUNÇÃO REMOVE AS DESINÊNCIAS DAS PALAVRAS DEIXANDO APENAS O RADICAL
    # Ex: FAZENDO -> FAZ
    def Stemming(self, instancia):
        stemmer = nltk.stem.RSLPStemmer()
        palavras = []
        for w in instancia.split():
            palavras.append(stemmer.stem(w))
        return (" ".join(palavras))

    # ESSA FUNÇÃO TROCA A VOGAIS QUE POSSUEM ACENTUAÇÃO PELA MESMA VOGAL SEM O ACENTO
    def removerAcentos(self, texto):
        for i in range(0, len(self.__acentos)):
            texto = texto.replace(self.__acentos[i], self.__s_acentos[i])
        return texto
