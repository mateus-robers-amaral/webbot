import telebot
from telebot import types
import pandas as pd
import csv

chave_api = '6408775461:AAFIhWk40_iqu2prkLSpVUn0xwl1Yas5MXI'
bot = telebot.TeleBot(chave_api)

@bot.callback_query_handler(func=lambda call:True)
def opcao1(callback):
    if callback.message:
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

@bot.callback_query_handler(func=lambda call:True)
def resposta(callback):
    if callback.message:
        if callback.data == 'action':
            filmes_acao = pd.read_csv('filmes.csv')
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de ação...')
            for linha in filmes_acao:
                if linha[4] == 'action':
                    print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'adventure':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de aventura...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'adventure':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")
            
        elif callback.data == 'animation':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de animação...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'animation':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'anime':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de anime...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'anime':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'biography':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de biografias...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'biography':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'comedy':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de comédia...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'comedy':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'crime':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de crime...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'crime':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")
                    
        elif callback.data == 'documentary':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de documentários...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'documentary':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")
                    
        elif callback.data == 'drama':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de dramas...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'drama':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'entertainment':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de entretenimento...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'entertainment':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'fantasy':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de fantasia...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'fantasy':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'history':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de história...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'history':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'holiday':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes para feriados...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'holiday':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'horror':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de terror...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'horror':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'music':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de música...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'music':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'musical':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de musicais...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'musical':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'nature':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de natureza...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'nature':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'news':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de noticiários...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'news':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'reality':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de reality-shows...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'reality':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'romance':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de romance...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'romance':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'short':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de curta metragens...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'short':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'sports':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de esporte...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'sports':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'variety':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes variados...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'variety':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'war':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de guerra...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'war':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

        elif callback.data == 'western':
            bot.send_message(callback.message.chat.id, 'Trazendo uma lista de filmes de velho-oeste...')
            with open("/Users/rober/Desktop/Estudos/filmes.csv", mode='r') as file:
                leitor_csv = csv.reader(file)
                for linha in leitor_csv:
                    if linha[4] == 'western':
                        print(f"Título: {linha[0]}\nData de lançamento: {linha[1]}\nClassificação do Público: {linha[2]}\nClassificação da Crítica: {linha[3]}")

@bot.callback_query_handler(func=lambda call:True)
def opcao2(callback):
    if callback.message:
        if callback.data == 'n':
            bot.send_message(callback.message.chat.id, 'Ok então, nos vemos outra hora.')
    
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