import random
import json
import spacy

# Carregar modelo em português do spaCy
nlp = spacy.load("pt_core_news_sm")

# Carregar respostas do JSON
def carregar_respostas():
    try:
        with open("data/perguntas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Dicionário de respostas padrão
RESPOSTAS_FIXAS = {
    "olá": ["Oi!", "Olá! Como posso te ajudar?", "E aí, tudo bem?"],
    "como você está": ["Estou bem, obrigado por perguntar!", "Estou funcionando perfeitamente!"],
    "qual seu nome": ["Sou um chatbot simples!", "Me chame de Botzinho!"],
    "adeus": ["Até mais!", "Tchau, volte sempre!", "Nos vemos em breve!"]
}

# Função para processar o texto com o spaCy
def preprocessar_texto(texto):
    doc = nlp(texto.lower())  # Analisa o texto
    palavras_filtradas = [token.lemma_ for token in doc if not token.is_stop]  # Remove stopwords e usa lematização
    return " ".join(palavras_filtradas)

# Obter resposta com NLP
def obter_resposta(pergunta):
    pergunta_limpa = preprocessar_texto(pergunta)
    respostas = carregar_respostas()
    
    # Tenta encontrar a pergunta processada
    resposta = respostas.get(pergunta_limpa, RESPOSTAS_FIXAS.get(pergunta_limpa, ["Desculpe, não entendi. Poderia reformular?"]))
    return random.choice(resposta)
