import telebot
from telebot import types
import pandas as pd
import csv

chave_api = 'nossa_chave_api'
bot = telebot.TeleBot(chave_api)

@bot.callback_query_handler(func=lambda call:True)
def resposta(callback):
    if callback.data == 's':
        markup = types.InlineKeyboardMarkup(row_width=2)

        acao = types.InlineKeyboardButton('💣 Ação 💣', callback_data='action')
        aventura = types.InlineKeyboardButton('🧭 Aventura 🧭', callback_data='adventure')
        animacao = types.InlineKeyboardButton('🏰 Animação 🏰', callback_data='animation')
        anime = types.InlineKeyboardButton('🐲 Anime 🐲', callback_data='anime')
        biografia = types.InlineKeyboardButton('🧐 Biografia 🧐', callback_data='biography')
        comedia = types.InlineKeyboardButton('🤣 Comédia 🤣', callback_data='comedy')
        crime = types.InlineKeyboardButton('🔫 Crime 🔫', callback_data='crime')
        documentario = types.InlineKeyboardButton('🧾 Documentário 🧾', callback_data='documentary')
        drama = types.InlineKeyboardButton('😿 Drama 😿', callback_data='drama')
        entretenimento = types.InlineKeyboardButton('🗣️ Entretenimento 🗣️', callback_data='entertainment')
        fantasia = types.InlineKeyboardButton('👻 Fantasia 👻', callback_data='fantasy')
        historia = types.InlineKeyboardButton('🏯 História 🏯', callback_data='history')
        feriado = types.InlineKeyboardButton('🎅 Feriado 🎅', callback_data='holiday')
        terror = types.InlineKeyboardButton('🫨 Terror 🫨', callback_data='horror')
        musica = types.InlineKeyboardButton('🎼 Música 🎼', callback_data='music')
        musical = types.InlineKeyboardButton('🎵 Musical 🎵', callback_data='musical')
        natureza = types.InlineKeyboardButton('🌱 Natureza 🌱', callback_data='nature')
        noticiario = types.InlineKeyboardButton('🗞️ Noticiário 🗞️', callback_data='news')
        reality = types.InlineKeyboardButton('💅 Reality 💅', callback_data='reality')
        romance = types.InlineKeyboardButton('💘 Romance 💘', callback_data='romance')
        curta = types.InlineKeyboardButton('⏳ Curta Metragem ⏳', callback_data='short')
        esporte = types.InlineKeyboardButton('⚽ Esporte ⚽', callback_data='sports')
        viagem = types.InlineKeyboardButton('✈️ Viagem ✈️', callback_data='travel')
        variedade = types.InlineKeyboardButton('🪭 Variedade 🪭', callback_data='variety')
        guerra = types.InlineKeyboardButton('⚔️ Guerra ⚔️', callback_data='war')
        velho_oeste = types.InlineKeyboardButton('🏇 Velho Oeste 🏇', callback_data='western')

        markup.add(acao, aventura, animacao, anime, biografia, comedia, crime, 
                documentario, drama, entretenimento,  fantasia, historia, feriado,
                terror, musica, musical, natureza, noticiario, reality, romance,
                curta, esporte, viagem, variedade, guerra, velho_oeste)
        
        bot.send_message(callback.message.chat.id, 'Que tipo de filme gostaria de ver hoje?', reply_markup=markup)

    elif callback.data == 'n':
        bot.send_message(callback.message.chat.id, 'Ok então, nos vemos outra hora.')

@bot.message_handler(commands=['start'])
def generos(callback):
    genres = ['acao', 'aventura', 'animacao', 'anime', 'biografia', 'comedia', 'crime', 
                'documentario', 'drama', 'entretenimento',  'fantasia', 'historia', 'feriado',
                'terror', 'musica', 'musical', 'natureza', 'noticiario', 'reality', 'romance',
                'curta', 'esporte', 'viagem', 'variedade', 'guerra', 'velho_oeste']
    for genero in genres:
        if genero == callback.data:
            filmes = pd.read_csv('/Users/rober/Desktop/Estudos/filmes.csv')
            bot.send_message(callback.message.chat.id, f'Trazendo uma lista de filmes de {genero}...')
            for i, linha in enumerate(filmes):
                if i[4] == {genero}:
                    print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")
    
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    markup = types.InlineKeyboardMarkup(row_width=4)
    texto = '''Olá, Bem-vindo ao What Movie!'''
    bot.reply_to(mensagem, texto)
    op1 = types.InlineKeyboardButton('Bora', callback_data='s')
    op2 = types.InlineKeyboardButton('Hoje não', callback_data='n')

    markup.add(op1, op2)

    bot.send_message(mensagem.chat.id, '''E ai?! Vai um filminho hoje?? 👀🍿🎥''', reply_markup=markup)

bot.polling()