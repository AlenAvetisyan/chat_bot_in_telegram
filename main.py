from datetime import*
import random
from pyrogram import Client, filters
import config
import json
import keyboards
from  cardcreator import card_cr

bot = Client(
    api_id = config.API_ID,
    api_hash = config.API_HASH,
    bot_token = config.BOT_TOKEN,
    name = "Alencho2025"
)

def button_filter(button):
    async def func(_, __, msg):
        return msg.text == button.text
    return  filters.create(func, "ButtonFilter", button=button)

@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply('Добро пожаловать! Этот бот создан для развлечения', reply_markup=keyboards.kb_main)
    with open('users.json', 'r') as file:
        users = json.load(file)
    if str(message.from_user.id) not in users.keys():
        users[message.from_user.id] = 100
        with open('users.json', 'w') as file:
            json.dump(users, file)

@bot.on_message(filters.command("info") | button_filter(keyboards.btn_info))
async def info(bot, message):
    await message.reply('Этот бот может сгенерировать для тебя футбольную карточку, поиграть с тобой в Камень Ножницы Бумага и не только!', reply_markup=keyboards.kb_main)

@bot.on_message(filters.command("account_balance") | button_filter(keyboards.btn_info))
async def info(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    await message.reply(f'Твой баланс: {users[str(message.from_user.id)]}')

@bot.on_message(filters.command("game") | button_filter(keyboards.btn_game))
async def game(bot, message):
    await message.reply("Выбери игру", reply_markup=keyboards.kb_games)

@bot.on_message(filters.command("Купить_карточку") | button_filter(keyboards.btn_card))
async def card(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    if users[str(message.from_user.id)] >= 5:
        with open("users.json", "r") as file:
            users = json.load(file)
            users[str(message.from_user.id)] -= 5
            with open('users.json', 'w') as file:
                json.dump(users, file)
        await message.reply(f'Твоя карточка: {card_cr()}')
    else:
        await message.reply(f"Не хватает средств."
                            f"на твоём счету {users[str(message.from_user.id)]}."
                            f"Минимальная сумма для игры - 5", reply_markup=keyboards.kb_main)

@bot.on_message(filters.command("buy_card"))
async def card(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    if users[str(message.from_user.id)] >= 5:
        with open("users.json", "r") as file:
            users = json.load(file)
            users[str(message.from_user.id)] -= 5
            with open('users.json', 'w') as file:
                json.dump(users, file)
        await message.reply(f'Твоя карточка: {card_cr()}')
    else:
        await message.reply(f"Не хватает средств."
                            f"на твоём счету {users[str(message.from_user.id)]}."
                            f"Минимальная сумма для игры - 5", reply_markup=keyboards.kb_main)

@bot.on_message(filters.command("back") | button_filter(keyboards.btn_back))
async def back(bot, message):
        await message.reply('Возвращаю в меню', reply_markup=keyboards.kb_main)

@bot.on_message(filters.command("Камень_Ножницы_Бумага") | button_filter(keyboards.btn_rps))
async def rps(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    if users[str(message.from_user.id)] >= 5:
        await message.reply("Твой ход", reply_markup=keyboards.kb_rps)
    else:
        await message.reply(f"Не хватает средств."
                            f"на твоём счету {users[str(message.from_user.id)]}."
                            f"Минимальная сумма для игры - 5", reply_markup=keyboards.kb_main)

@bot.on_message(filters.command("games_menu") | button_filter(keyboards.btn_gmenu))
async def menu(bot, message):
        await message.reply('Возвращаю в игровое меню', reply_markup=keyboards.kb_games)

@bot.on_message(button_filter(keyboards.btn_rock) | button_filter(keyboards.btn_scissors) | button_filter(keyboards.btn_paper))
async def choice_rps(bot, message):
    rock = keyboards.btn_rock.text
    scissors = keyboards.btn_scissors.text
    paper = keyboards.btn_paper.text
    user = message.text
    pc = random.choice([rock, scissors, paper])

    if user == pc:
        await message.reply('Ничья!')
        with open("users.json", "r") as file:
            users = json.load(file)
            users[str(message.from_user.id)] += 0
            with open('users.json', 'w') as file:
                json.dump(users, file)
    elif ((user == keyboards.btn_rock.text and pc == scissors) or
        (user == keyboards.btn_scissors.text and pc == paper) or
        (user == keyboards.btn_paper.text and pc == rock)):
        await message.reply(f'Ты выиграл! Бот выбрал {pc}',
                            reply_markup=keyboards.kb_games)
        with open("users.json", "r") as file:
            users = json.load(file)
            users[str(message.from_user.id)] += 5
            with open('users.json', 'w') as file:
                json.dump(users, file)
    else:
        await message.reply(f'Ты проиграл. Бот выбрал {pc}',
                            reply_markup=keyboards.kb_games)
        with open("users.json", "r") as file:
            users = json.load(file)
            users[str(message.from_user.id)] -= 5
            with open('users.json', 'w') as file:
                json.dump(users, file)

@bot.on_message(filters.command("time"))
async def start(bot, message):
    await message.reply(f"Текущие дата и время: {datetime.now()}")

bot.run()
