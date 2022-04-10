import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Я тоже тебя люблю")
    item2 = types.KeyboardButton("Вау! Как круто!")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Приветы!")
    pic = open("static/mom_and_car.jpg", 'rb')
    bot.send_photo(message.chat.id, pic)
    
    bot.send_message(message.chat.id, "Это моя самая красивая, умная, деловая и заботливая мама! Я ее очень люблю! И этот бот я сделала, что бы сказать ей то, что у меня не всегда получается \nМама, я тебя очень ценю и считаю, что ты сделала для меня очень много и я счастлива, что родилась именно у тебя.".format(message.from_user, bot.get_me()), parse_mode = 'html',
        reply_markup=markup)


@bot.message_handler(content_types = ['text'])
def lalala(message):
    if message.chat.type == 'private':
        # первый уровень
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("Ты хорошая дочь!")
        item2 = types.KeyboardButton("Какая же ты у меня смешная😁😁")
        markup.add(item1, item2)
        if message.text == 'Вау! Как круто!':

            bot.send_message(message.chat.id, "Я знаю😎 Еще у меня не всегда получается попросить у тебя денежек, мне очень стыдно из-за этого, и я думаю, что я плохая дочь".format(message.from_user, bot.get_me()), parse_mode = 'html',
            reply_markup=markup)

        elif message.text == 'Я тоже тебя люблю':
            sti = open("static/tsom.tgs", 'rb')
            bot.send_sticker(message.chat.id, sti)         

            bot.send_message(message.chat.id, "Еще у меня не всегда получается попросить у тебя денежек, мне очень стыдно из-за этого, и я думаю, что я плохая дочь".format(message.from_user, bot.get_me()), parse_mode = 'html',
                reply_markup=markup)

        # второй уровень
        elif (message.text == 'Ты хорошая дочь!' or message.text == 'Какая же ты у меня смешная😁😁'):
            markup = types.InlineKeyboardMarkup(row_width = 2)
            item1 = types.InlineKeyboardButton("отправить деняк", callback_data = 'good')
            markup.add(item1)

            pic2 = open("static/mom.jpg", 'rb')
            bot.send_photo(message.chat.id, pic2) 

            bot.send_message(message.chat.id, "Мне приятно это слышать😊 Смотри, как мы похожи, неужели тебе никогда не хотелось простого человеческого деняк", reply_markup = markup)      
        else: 
            bot.send_message(message.chat.id, 'этого он еще не умеет)')

    



@bot.callback_query_handler(func = lambda call:True)
def callback_inline(call):
    try:
        # третий уровень
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, "СПАСИБА!!")

                bot.answer_callback_query(callback_query_id = call.id, show_alert = False, text = "Я ТЕБЯ ЛЮБЛЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮ")

            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Смотри, как мы похожи, неужели тебе никогда не хотелось простого человеческого деняк", reply_markup = None)
    except Exception as e:
        print(repr(e))
            
# RUN
bot.polling(none_stop = True)



# SIMPLE TBOT кнопки, инлайновые кнопки, алярмы
