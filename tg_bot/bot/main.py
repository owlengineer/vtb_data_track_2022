import telebot
from telebot import types

bot = telebot.TeleBot("5425321398:AAGGMPgwdkCiSAN-l7voKp2e5TMIV6Mn3Ns")

ROLES = ["Менеджер", "Аналитик"]

# bad store :(
store_roles_by_id = {}


@bot.message_handler(commands=["change_role"])
def change_role(message):
    choose_role(message)


@bot.message_handler(commands=["help", "start"])
def get_help(message):
    bot.send_message(message.chat.id, '''Привет, наш бот умеет следующие команды:
/help -  Cправка по боту, короткий обзор команд
/change_role -  здесь можно сменить или установить свою роль
/news - а здесь по роли можно получить релевантные новости)
''')


@bot.message_handler(commands=['news'])
def get_news(message):
    try:
        bot.send_message(message.chat.id, f"some news for {store_roles_by_id[message.chat.id]}")
    except KeyError:
        bot.send_message(message.chat.id, "Нет роль. Воспользуйтесь командой /change_role")

@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    text = message.text
    if text in ROLES:
        print("1")
    else:
        bot.send_message(message.chat.id, "Используйте /help, чтобы узнать что умеет это бот")


def choose_role(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for role in ROLES:
        markup.add(types.KeyboardButton(role))
    bot.send_message(message.chat.id, "Выбери свою роль", reply_markup=markup)
    # bot.reply_to()
    bot.register_next_step_handler(message, update_role)


def update_role(message):
    role = message.text
    store_roles_by_id[message.chat.id] = role
    bot.send_message(message.chat.id, f"Теперь у тебя роль: {role}, и ты можешь воспользоваться командой /news")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
