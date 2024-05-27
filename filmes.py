import pandas as pd
import telebot
from telebot import types

bot = telebot.TeleBot('CHAVE_API')

@bot.message_handler(commands=['start'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=4)

    acao = types.InlineKeyboardButton('Ação', callback_data='action')
    aventura = types.InlineKeyboardButton('Aventura', callback_data='adventure')
    animacao = types.InlineKeyboardButton('Animação', callback_data='animation')
    anime = types.InlineKeyboardButton('Anime', callback_data='anime')
    biografia = types.InlineKeyboardButton('Biografia', callback_data='biography')
    comedia = types.InlineKeyboardButton('Comédia', callback_data='comedy')
    crime = types.InlineKeyboardButton('Crime', callback_data='crime')
    documentario = types.InlineKeyboardButton('Documentário', callback_data='documentary')
    drama = types.InlineKeyboardButton('Drama', callback_data='drama')
    entretenimento = types.InlineKeyboardButton('Entretenimento', callback_data='entertainment')
    fantasia = types.InlineKeyboardButton('Fantasia', callback_data='fantasy')
    historia = types.InlineKeyboardButton('História', callback_data='history')
    feriado = types.InlineKeyboardButton('Feriado', callback_data='holiday')
    terror = types.InlineKeyboardButton('Terror', callback_data='horror')
    musica = types.InlineKeyboardButton('Música', callback_data='music')
    musical = types.InlineKeyboardButton('Musical', callback_data='musical')
    natureza = types.InlineKeyboardButton('Natureza', callback_data='nature')
    noticiario = types.InlineKeyboardButton('Noticiário', callback_data='news')
    reality = types.InlineKeyboardButton('Reality', callback_data='reality')
    romance = types.InlineKeyboardButton('Romance', callback_data='romance')
    curta = types.InlineKeyboardButton('Curta', callback_data='short')
    esporte = types.InlineKeyboardButton('Esporte', callback_data='sports')
    viagem = types.InlineKeyboardButton('Viagem', callback_data='travel')
    variedade = types.InlineKeyboardButton('Variedade', callback_data='variety')
    guerra = types.InlineKeyboardButton('Guerra', callback_data='war')
    velho_oeste = types.InlineKeyboardButton('Velho Oeste', callback_data='western')

    markup.add(acao, aventura, animacao, anime, biografia, comedia, crime, 
               documentario, drama, entretenimento,  fantasia, historia, feriado,
               terror, musica, musical, natureza, noticiario, reality, romance,
               curta, esporte, viagem, variedade, guerra, velho_oeste)
    
    bot.send_message(message.chat.id, 'Que tipo de filme gostaria de ver hoje?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.message:
        if callback.data == 'action':
            filmes_acao = pd.read_csv('filmes.csv')
            bot.send_message(callback.message.chat.id, f'💣 Filmes de Ação 💣')
            for i in range(len(filmes_acao)):
                mensagem = f"{filmes_acao['Nome'].iloc[0]} : {filmes_acao['Lançamento'].iloc[1]}
                                                               : {filmes_acao['Critica'].iloc[2]}
                                                               : {filmes_acao['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'adventure':
            filmes_aventura = pd.read_csv('filmes.csv')
            bot.send_message(callback.message.chat.id, f'🧭 Filmes de Aventura 🧭')
            for i in range(len(filmes_aventura)):
                mensagem = f"{filmes_aventura['Nome'].iloc[0]} : {filmes_aventura['Lançamento'].iloc[1]}
                                                               : {filmes_aventura['Critica'].iloc[2]}
                                                               : {filmes_aventura['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)


        elif callback.data == 'animation':
            filmes_animacao = pd.read_csv('filmes.csv')
            bot.send_message(callback.message.chat.id, f'🏰 Filmes de Animação 🏰')
            for i in range(len(filmes_animacao)):
                 mensagem = f"{filmes_animacao['Nome'].iloc[0]} : {filmes_animacao['Lançamento'].iloc[1]}
                                                               : {filmes_animacao['Critica'].iloc[2]}
                                                               : {filmes_animacao['Audiência'].iloc[3]}"
            bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'anime':
            filmes_anime = pd.read_csv('filmes.csv')
            bot.send_message(callback.message.chat.id, f'🐲 Filmes de Anime 🐲')
            for i in range(len(filmes_anime)):
                mensagem = f"{filmes_anime['Nome'].iloc[0]} : {filmes_anime['Lançamento'].iloc[1]}
                                                               : {filmes_anime['Critica'].iloc[2]}
                                                               : {filmes_anime['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'biography':
            bot.send_message(callback.message.chat.id, f'🧐 Filmes de Biografia 🧐')
            filmes_biografia = pd.read_csv('filmes.csv')
            for i in range(len(filmes_biografia)):
                mensagem = f"{filmes_biografia['Nome'].iloc[0]} : {filmes_biografia['Lançamento'].iloc[1]}
                                                               : {filmes_biografia['Critica'].iloc[2]}
                                                               : {filmes_biografia['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)


        elif callback.data == 'comedy':
            bot.send_message(callback.message.chat.id, f'🤣 Filmes de Comédia 🤣')
            filmes_comedia = pd.read_csv('filmes.csv')
            for i in range(len(filmes_comedia)):
                mensagem = f"{filmes_comedia['Nome'].iloc[0]} : {filmes_comedia['Lançamento'].iloc[1]}
                                                               : {filmes_comedia['Critica'].iloc[2]}
                                                               : {filmes_comedia['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'crime':
            bot.send_message(callback.message.chat.id, f'🔫 Filmes de Crime 🔫')
            filmes_crime = pd.read_csv('filmes.csv')
            for i in range(len(filmes_crime)):
                mensagem = f"{filmes_crime['Nome'].iloc[0]} : {filmes_crime['Lançamento'].iloc[1]}
                                                               : {filmes_crime['Critica'].iloc[2]}
                                                               : {filmes_crime['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'documentary':
            bot.send_message(callback.message.chat.id, f'🧾 Documentários 🧾')
            filmes_documentario = pd.read_csv('filmes.csv')
            for i in range(len(filmes_documentario)):
                mensagem = f"{filmes_documentario['Nome'].iloc[0]} : {filmes_documentario['Lançamento'].iloc[1]}
                                                               : {filmes_documentario['Critica'].iloc[2]}
                                                               : {filmes_documentario['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'drama':
            bot.send_message(callback.message.chat.id, f'😿 Filmes de Drama 😿')
            filmes_drama = pd.read_csv('filmes.csv')
            for i in range(len(filmes_drama)):
                mensagem = f"{filmes_drama['Nome'].iloc[0]} : {filmes_drama['Lançamento'].iloc[1]}
                                                               : {filmes_drama['Critica'].iloc[2]}
                                                               : {filmes_drama['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'entertainment':
            bot.send_message(callback.message.chat.id, f'🗣️ Filmes de Entretenimento 🗣️')
            filmes_entretenimento = pd.read_csv('filmes.csv')
            for i in range(len(filmes_entretenimento)):
                mensagem = f"{filmes_entretenimento['Nome'].iloc[0]} : {filmes_entretenimento['Lançamento'].iloc[1]}
                                                               : {filmes_entretenimento['Critica'].iloc[2]}
                                                               : {filmes_entretenimento['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'fantasy':
            bot.send_message(callback.message.chat.id, f'👻 Filmes de Fantasia 👻')
            filmes_fantasia = pd.read_csv('filmes.csv')
            for i in range(len(filmes_fantasia)):
                mensagem = f"{filmes_fantasia['Nome'].iloc[0]} : {filmes_fantasia['Lançamento'].iloc[1]}
                                                               : {filmes_fantasia['Critica'].iloc[2]}
                                                               : {filmes_fantasia['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'history':
            bot.send_message(callback.message.chat.id, f'🏯 Filmes de História 🏯')
            filmes_historia = pd.read_csv('filmes.csv')
            for i in range(len(filmes_historia)):
                mensagem = f"{filmes_historia['Nome'].iloc[0]} : {filmes_historia['Lançamento'].iloc[1]}
                                                               : {filmes_historia['Critica'].iloc[2]}
                                                               : {filmes_historia['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'holiday':
            bot.send_message(callback.message.chat.id, f'🎅 Filmes de Feriado 🎅')
            filmes_feriado = pd.read_csv('filmes.csv')
            for i in range(len(filmes_feriado)):
                mensagem = f"{filmes_feriado['Nome'].iloc[0]} : {filmes_feriado['Lançamento'].iloc[1]}
                                                               : {filmes_feriado['Critica'].iloc[2]}
                                                               : {filmes_feriado['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'horror':
            bot.send_message(callback.message.chat.id, f'🫨 Filmes de Terror 🫨')
            filmes_terror = pd.read_csv('filmes.csv')
            for i in range(len(filmes_terror)):
                mensagem = f"{filmes_terror['Nome'].iloc[0]} : {filmes_terror['Lançamento'].iloc[1]}
                                                               : {filmes_terror['Critica'].iloc[2]}
                                                               : {filmes_terror['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'music':
            bot.send_message(callback.message.chat.id, f'🎼 Filmes de Música 🎼')
            filmes_musica = pd.read_csv('filmes.csv')
            for i in range(len(filmes_musica)):
                mensagem = f"{filmes_musica['Nome'].iloc[0]} : {filmes_musica['Lançamento'].iloc[1]}
                                                               : {filmes_musica['Critica'].iloc[2]}
                                                               : {filmes_musica['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'musical':
            bot.send_message(callback.message.chat.id, f'🎵 Filmes de Musical 🎵')
            filmes_musical = pd.read_csv('filmes.csv')
            for i in range(len(filmes_musical)):
                mensagem = f"{filmes_musical['Nome'].iloc[0]} : {filmes_musical['Lançamento'].iloc[1]}
                                                               : {filmes_musical['Critica'].iloc[2]}
                                                               : {filmes_musical['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'nature':
            bot.send_message(callback.message.chat.id, f'🌱 Filmes de Natureza 🌱')
            filmes_natureza = pd.read_csv('filmes.csv')
            for i in range(len(filmes_natureza)):
                mensagem = f"{filmes_natureza['Nome'].iloc[0]} : {filmes_natureza['Lançamento'].iloc[1]}
                                                               : {filmes_natureza['Critica'].iloc[2]}
                                                               : {filmes_natureza['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'news':
            bot.send_message(callback.message.chat.id, f'🗞️ Noticiários 🗞️')
            filmes_noticiarios = pd.read_csv('filmes.csv')
            for i in range(len(filmes_noticiarios)):
                mensagem = f"{filmes_noticiarios['Nome'].iloc[0]} : {filmes_noticiarios['Lançamento'].iloc[1]}
                                                               : {filmes_noticiarios['Critica'].iloc[2]}
                                                               : {filmes_noticiarios['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'reality':
            bot.send_message(callback.message.chat.id, f'💅 Reality Shows 💅')
            filmes_reality = pd.read_csv('filmes.csv')
            for i in range(len(filmes_reality)):
                mensagem = f"{filmes_reality['Nome'].iloc[0]} : {filmes_reality['Lançamento'].iloc[1]}
                                                               : {filmes_reality['Critica'].iloc[2]}
                                                               : {filmes_reality['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'romance':
            bot.send_message(callback.message.chat.id, f'💘 Filmes de Romance 💘')
            filmes_romance = pd.read_csv('filmes.csv')
            for i in range(len(filmes_romance)):
                mensagem = f"{filmes_romance['Nome'].iloc[0]} : {filmes_romance['Lançamento'].iloc[1]}
                                                               : {filmes_romance['Critica'].iloc[2]}
                                                               : {filmes_romance['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'shorts':
            bot.send_message(callback.message.chat.id, f'⏳ Curtas ⏳')
            filmes_curtas = pd.read_csv('filmes.csv')
            for i in range(len(filmes_curtas)):
                mensagem = f"{filmes_curtas['Nome'].iloc[0]} : {filmes_curtas['Lançamento'].iloc[1]}
                                                               : {filmes_curtas['Critica'].iloc[2]}
                                                               : {filmes_curtas['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'sports':
            bot.send_message(callback.message.chat.id, f'⚽ Esportes ⚽')
            filmes_esportes = pd.read_csv('filmes.csv')
            for i in range(len(filmes_esportes)):
                mensagem = f"{filmes_esportes['Nome'].iloc[0]} : {filmes_esportes['Lançamento'].iloc[1]}
                                                               : {filmes_esportes['Critica'].iloc[2]}
                                                               : {filmes_esportes['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'travel':
            bot.send_message(callback.message.chat.id, f'✈️ Filmes de Viagens ✈️')
            filmes_viagem = pd.read_csv('filmes.csv')
            for i in range(len(filmes_viagem)):
                mensagem = f"{filmes_viagem['Nome'].iloc[0]} : {filmes_viagem['Lançamento'].iloc[1]}
                                                               : {filmes_viagem['Critica'].iloc[2]}
                                                               : {filmes_viagem['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'variety':
            bot.send_message(callback.message.chat.id, f'🪭 Filmes Variados 🪭')
            filmes_variados = pd.read_csv('filmes.csv')
            for i in range(len(filmes_variados)):
                mensagem = f"{filmes_variados['Nome'].iloc[0]} : {filmes_variados['Lançamento'].iloc[1]}
                                                               : {filmes_variados['Critica'].iloc[2]}
                                                               : {filmes_variados['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        elif callback.data == 'war':
            bot.send_message(callback.message.chat.id, f'⚔️ Filmes de Guerra ⚔️')
            filmes_guerra = pd.read_csv('filmes.csv')
            for i in range(len(filmes_guerra)):
                mensagem = f"{filmes_guerra['Nome'].iloc[0]} : {filmes_guerra['Lançamento'].iloc[1]}
                                                               : {filmes_guerra['Critica'].iloc[2]}
                                                               : {filmes_guerra['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)
        
        elif callback.data == 'western':
            bot.send_message(callback.message.chat.id, f'🏇 Filmes de Velho-Oeste 🏇')
            filmes_velho_oeste = pd.read_csv('filmes.csv')
            for i in range(len(filmes_velho_oeste)):
                mensagem = f"{filmes_velho_oeste['Nome'].iloc[0]} : {filmes_velho_oeste['Lançamento'].iloc[1]}
                                                               : {filmes_velho_oeste['Critica'].iloc[2]}
                                                               : {filmes_velho_oeste['Audiência'].iloc[3]}"
                bot.send_message(callback.message.chat.id, mensagem)
            bot.send_message(callback.message.chat.id, '-' *40)

        else:   
            bot.send_message(callback.message.chat.id, 'ERROR')
    
bot.polling()
