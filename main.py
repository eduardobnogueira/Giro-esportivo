import os
import logging
import requests
from dotenv import load_workbook, load_dotenv
from google import genai
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- 1. CARREGAMENTO SEGURO DE CHAVES ---
# O python-dotenv vai ler o arquivo .env e carregar as senhas na memória do computador
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

# Inicializa o cliente oficial do Google Gemini
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Configura o sistema de logs para mostrar mensagens no terminal
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# --- 2. COLETA DE DADOS VIA GNEWS API ---
def buscar_noticias_gnews():
    """Busca notícias de futebol em tempo real usando a GNews API."""
    url = f"https://gnews.io/api/v4/search?q=futebol&lang=pt&country=br&max=4&apikey={GNEWS_API_KEY}"
    
    try:
        resposta = requests.get(url, timeout=10)
        dados = resposta.json()
        artigos = dados.get('articles', [])
        noticias = []
        
        for item in artigos:
            noticias.append({
                'titulo': item.get('title'),
                'link': item.get('url'),
                'descricao': item.get('description', 'Sem detalhes disponíveis.')
            })
        return noticias
    except Exception as e:
        print(f"[DEBUG] Erro ao acessar a API da GNews: {e}")
        return []


# --- 3. INTELIGÊNCIA ARTIFICIAL (GEMINI) ---
def gerar_comentario_gemini(titulo, descricao):
    """O Gemini usa os dados da GNews para criar a análise esportiva."""
    try:
        resposta = gemini_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"""
            Você é um comentarista esportivo de TV muito dinâmico, inteligente e bem-humorado. 
            Resuma a notícia a seguir em até 3 frases explicativas. 
            Termine o resumo com um jargão ou frase típica de quem ama esportes e futebol.
            
            Manchete: {titulo}
            Contexto: {descricao}
            """
        )
        return resposta.text.strip()
    except Exception as e:
        return f"Não consegui analisar esse lance agora. (Erro na IA: {e})"


# --- 4. COMANDOS DO TELEGRAM ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name
    mensagem = (
        f"Fala, {nome}! ⚽\n\n"
        "Seu Bot de Futebol com a API da GNews e a inteligência do Gemini está pronto.\n"
        "Envie o comando /futebol para buscar o giro de notícias do momento!"
    )
    await update.message.reply_text(mensagem)

async def enviar_giro_futebol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Entrando em campo e acionando os servidores da GNews... Segura aí!")
    noticias = buscar_noticias_gnews()
    
    if not noticias:
        await update.message.reply_text("🏟️ Não consegui puxar dados da GNews agora.")
        return

    for idx, art in enumerate(noticias):
        resumo_ia = gerar_comentario_gemini(art['titulo'], art['descricao'])
        mensagem_formatada = (
            f"⚽ *{idx+1}. {art['titulo']}*\n\n"
            f"🎙️ *Análise do Gemini:* {resumo_ia}\n\n"
            f"🔗 [Ler matéria completa]({art['link']})"
        )
        await update.message.reply_text(mensagem_formatada, parse_mode="Markdown", disable_web_page_preview=True)


# --- 5. EXECUÇÃO ---
def main():
    print("🚀 Bot de Futebol Seguro Ativo!")
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("futebol", enviar_giro_futebol))
    app.run_polling()

if __name__ == "__main__":
    main()