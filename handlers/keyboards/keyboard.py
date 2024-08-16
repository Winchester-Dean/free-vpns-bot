from database.db import DataBase

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

channels_list = []

database = DataBase()
channels = database.get_channels()
for channel in channels:
    channel_name = channel[0]
    channel_link = channel[1]

    channels_list.append(
        InlineKeyboardButton(
            text = channel_name,
            url = channel_link
        )
    )

inline_channels = InlineKeyboardMarkup()
inline_channels.add(*channels_list)
inline_channels.add(
    InlineKeyboardButton(
        text = "Я подписался",
        callback_data = "sub"
    )
)

menu_buttons_list = []
texts = [
    "Профиль", "Мои ключи",
    "Получить ключ", "Реферальная система",
    "Задания"
]
for text in texts:
    menu_buttons_list.append(
        KeyboardButton(
            text=text
        )
    )

menu = ReplyKeyboardMarkup()
menu.add(*menu_buttons_list)

