import random
from src.respostas import obter_resposta

def iniciar_chatbot():
    print("Chatbot: Olá! Digite 'sair' para encerrar.")
    
    while True:
        usuario = input("Você: ").strip().lower()
        if usuario == "sair":
            print("Chatbot: Até logo!")
            break
        
        resposta = obter_resposta(usuario)
        print(f"Chatbot: {resposta}")
