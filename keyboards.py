from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup
from pyrogram import emoji

btn_info = KeyboardButton(f"/info")
btn_start = KeyboardButton(f"/start")
btn_game = KeyboardButton(f"/game")
btn_accb = KeyboardButton(f"/account_balance")


kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_start, btn_info],
        [btn_game, btn_accb]
    ],
    resize_keyboard=True
)

btn_card = KeyboardButton(f"/Купить_карточку")
btn_back = KeyboardButton(f'/back')
btn_rps = KeyboardButton(f"/Камень_Ножницы_Бумага")
btn_accb = KeyboardButton(f"/account_balance")

kb_games = ReplyKeyboardMarkup(
    keyboard=[
        [btn_card, btn_rps],
        [btn_back, btn_accb]
    ],
    resize_keyboard=True
)


btn_gmenu = KeyboardButton(f'/games_menu')
btn_rock = KeyboardButton(f'{emoji.ROCK} Камень')
btn_scissors = KeyboardButton(f'{emoji.SCISSORS} Ножницы')
btn_paper = KeyboardButton(f'{emoji.PAGE_FACING_UP} Бумага')
btn_accb = KeyboardButton(f"/account_balance")

kb_rps = ReplyKeyboardMarkup(
    keyboard=[
        [btn_rock, btn_scissors, btn_paper],
        [btn_gmenu, btn_accb]
    ],
    resize_keyboard=True
)
