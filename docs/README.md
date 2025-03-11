Chatbot em Python

Este projeto implementa um chatbot simples utilizando SpaCy para processamento de linguagem natural e Flask (ou qualquer outra biblioteca web que preferir) para interação com o usuário. O chatbot foi projetado para entender e responder perguntas sobre um determinado conjunto de dados.
Índice

    Descrição do Projeto
    Tecnologias Utilizadas
    Instalação
    Estrutura de Pastas
    Como Usar
    Testes
    Contribuindo
    Licença

Descrição do Projeto

Este é um projeto de chatbot simples que utiliza SpaCy para o processamento de linguagem natural e é projetado para fornecer respostas a perguntas feitas por um usuário. Ele processa as perguntas, extrai as palavras-chave e, com base nessas palavras-chave, encontra a resposta mais relevante a partir de um banco de dados pré-definido de respostas.
Funcionalidades:

    Processamento de linguagem natural com SpaCy para entender perguntas.
    Respostas pré-definidas baseadas em palavras-chave.
    Interface interativa para conversas com o chatbot.
    Facilidade de expandir o conjunto de perguntas e respostas.

Tecnologias Utilizadas

    Python: Linguagem principal utilizada para o desenvolvimento.
    SpaCy: Biblioteca de processamento de linguagem natural (NLP).
    Flask (opcional, se estiver criando uma interface web): Framework para construir APIs e interfaces web em Python.
    Git: Sistema de controle de versão utilizado para gerenciamento do código.

Instalação
1. Clonando o Repositório

Primeiro, clone o repositório para sua máquina local:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Configuração do Ambiente Virtual

Para evitar conflitos de dependências, é altamente recomendável criar um ambiente virtual. Execute o seguinte comando:

python -m venv venv

Ative o ambiente virtual:

    Windows: .\venv\Scripts\activate
    Linux/macOS: source venv/bin/activate

3. Instalando Dependências

Depois de ativar o ambiente virtual, instale as dependências necessárias com o pip:

pip install -r requirements.txt

Certifique-se de que o arquivo requirements.txt contém as dependências do seu projeto. Por exemplo:

flask
spacy

4. Instalando o Modelo do SpaCy

Se você estiver utilizando SpaCy para processamento de linguagem natural, instale o modelo para o idioma português:

python -m spacy download pt_core_news_sm

5. Inicializando o Servidor (Caso esteja usando Flask)

Se o chatbot estiver integrado com o Flask ou outro framework web, inicie o servidor com:

python app.py

O servidor estará rodando localmente em http://127.0.0.1:5000 ou http://localhost:5000.
Estrutura de Pastas

Abaixo está a estrutura de diretórios do projeto:

/project-chat
│
├── /src                    # Código-fonte principal do chatbot
│   ├── chatbot.py           # Funções principais do chatbot
│   ├── respostas.py         # Banco de respostas do chatbot
│   └── preprocessamento.py  # Funções de pré-processamento de texto
│
├── /models                  # Modelos do SpaCy
│   └── pt_core_news_sm      # Modelo do SpaCy para português
│
├── /tests                   # Testes unitários e de integração
│   └── test_chatbot.py      # Testes do chatbot
│
├── requirements.txt         # Dependências do projeto
├── README.md                # Este arquivo
└── app.py                   # Servidor web (Flask) ou lógica de execução do chatbot

Como Usar

    Inicie o chatbot: Caso você tenha configurado o Flask ou outra API, inicie o servidor com o comando:

    python app.py

    Interação com o chatbot: Acesse o servidor local através do navegador ou use uma ferramenta como o Postman para enviar requisições HTTP.

    Enviando perguntas: A interface do chatbot aceitará perguntas através de POST ou GET (dependendo de como o Flask estiver configurado) e retornará uma resposta processada com base nas palavras-chave.

Exemplo de Requisição POST (se estiver usando Flask):

curl -X POST http://localhost:5000/perguntar -d "Qual é a previsão do tempo?" -H "Content-Type: application/json"

Exemplo de Código de Interação com o Chatbot:

from src.chatbot import iniciar_chatbot

iniciar_chatbot()

Testes

Para rodar os testes do projeto, utilize o pytest ou outro framework de testes de sua preferência.

Instale o pytest se necessário:

pip install pytest

E então, rode os testes com o comando:

pytest

Os testes devem estar na pasta /tests.
Contribuindo

Se você deseja contribuir para o projeto, siga as etapas abaixo:

    Fork o repositório.
    Crie uma nova branch:

git checkout -b minha-nova-feature

Faça as alterações necessárias e faça um commit:

git commit -m "Adiciona nova funcionalidade"

Push para o repositório remoto:

    git push origin minha-nova-feature

    Crie um pull request.

Licença

Este projeto está licenciado sob a MIT License - consulte o arquivo LICENSE para mais detalhes.