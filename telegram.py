import asyncio
from aiogram import Bot
import csv
import os


async def enviar_mensagem_promocao(bot, chat_id, mensagem):
    await bot.send_message(chat_id=chat_id, text=mensagem)

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pular o cabeçalho
        return [linha for linha in leitor]  # Retornar todas as linhas do arquivo

async def enviar_promocoes(bot, chat_id, arquivo_filmes):
    filmes = ler_arquivo_csv(arquivo_filmes)
    for filme in filmes:
        if len(filme) < 5:
            continue
        titulo, data, critica, audiencia, genero = filme
        mensagem = f"🎬 {titulo} 🎬\n\n📅 Data: {data}\n\n👥 Crítica: {critica}\n\n👥 Audiência: {audiencia}\n\n🎭 Gênero: {genero}"
        await bot.send_message(chat_id=chat_id, text=mensagem)

async def main():
    bot_token = ('6753015460:AAHQ6R8HkaqIpFQ-ieu5ddFzJxUn1BleQyI')
    if bot_token is None:
        raise Exception('Token não definido. Por favor, defina a variável de ambiente BOT_TOKEN.')
    bot = Bot(token=bot_token)
    chat_id = '6753015460'
    mensagem = '---------------🔥 Lançamentos de Filmes! 🔥---------------'
    await enviar_mensagem_promocao(bot, chat_id, mensagem)
    await enviar_promocoes(bot, chat_id, 'filmes.csv')

asyncio.run(main())