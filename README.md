# ⚽ Bot de Giro do Futebol com IA (Gemini & GNews)

Este é um bot do Telegram inteligente que automatiza o processo de busca de notícias de futebol brasileiro através da **GNews API**, processa os textos usando o modelo **Google Gemini 2.5-Flash** e envia análises personalizadas e bem-humoradas direto no chat.

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **Google GenAI SDK** (`gemini-2.5-flash`)
- **Python Telegram Bot** (Arquitetura assíncrona)
- **GNews API** (Agregação de notícias estruturadas)
- **Python-Dotenv** (Gerenciamento seguro de variáveis de ambiente)

## 🔧 Como Rodar o Projeto

1. Clone o repositório.
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt

   Crie um arquivo .env na raiz do projeto e configure suas chaves de acesso:
   ```

Plaintext
TELEGRAM_TOKEN=seu_token_aqui
GEMINI_API_KEY=sua_chave_gemini_aqui
GNEWS_API_KEY=sua_chave_gnews_aqui
Inicie o bot:

Bash
python main.py
No Telegram, busque pelo bot e envie o comando /futebol.

---

## 📤 Subir para o GitHub pelo VS Code

Com os 4 arquivos prontos na pasta (`main.py`, `.env`, `.gitignore`, `requirements.txt` e `README.md`), faça o upload de forma super visual:

1. No menu lateral esquerdo do VS Code, clique no terceiro ícone de cima para baixo: o de **Controle de Versão** (parece uma ramificação/nó de árvore).
2. Clique no botão **"Inicializar Repositório"** (Initialize Repository).
3. Repare que o arquivo `.env` vai sumir da lista ou ficar cinza. Isso prova que o seu `.gitignore` está funcionando e protegendo suas chaves.
4. Na caixinha de texto "Mensagem", escreva: `Primeiro commit: Bot de futebol funcionando`.
5. Clique no botão **"Commit"** (ou no visto ✔️).
6. Clique no botão azul **"Publicar Branch"** (Publish Branch).
7. O VS Code vai te perguntar se quer publicar como repositório **Público** ou Privado. Escolha **Público** para as pessoas poderem ver no seu portfólio!

Seu projeto está oficialmente na nuvem com nível de organização profissional! Quer ajuda pa
