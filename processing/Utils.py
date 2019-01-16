# ESSE É O ARQUIVO ONDE ESTÀ LOCALIZADO A LISTA DE VOGAIS COM E SEM ACENTOS PARA SER REALIZADA A REMOÇÃO NA ETAPA DE PRE-PROCESSAMENTO
# TAMBEM POSSUE STOPWORDS QUE O NLTK NÃO CONSEGUE IDENTIFICAR. AQUI TAMBEM PODE SER ADICIONADA NOVAS STOPWORDS

ACENTOS = ['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'ã', 'ẽ', 'ĩ', 'õ', 'ũ', 'â', 'ê', 'î', 'ô','û','ç']

S_ACENTOS = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o','u','c']

MORE_STOPWORDS = ['ja', 'q', 'd', 'ai', 'desse', 'dessa', 'disso', 'nesse', 'nessa', 'nisso', 'esse',
                               'essa', 'isso', 'so', 'mt', 'vc', 'voce', 'ne', 'ta', 'to', 'pq',
                               'cade', 'kd', 'la', 'e', 'eh', 'dai', 'pra', 'vai', 'olha', 'pois', 'fica', 'muito',
                               'muita', 'muitos', 'muitas', 'onde', 'mim', 'oi', 'ola', 'ate', 'com', ',', '.',
                               'nao', 'porque']
