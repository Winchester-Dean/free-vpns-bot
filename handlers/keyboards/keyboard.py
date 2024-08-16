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

inline_channels = InlineKeyboardMarkup(row_width=2)
inline_channels.add(*channels_list)
inline_channels.add(
    InlineKeyboardButton(
        text = "Я подписался",
        callback_data = "sub"
    )
)

one = [
    KeyboardButton("Профиль"),
    KeyboardButton("Мои ключи")
]

two = [
    KeyboardButton("Получить ключ"),
    KeyboardButton("Задания")
]

three = [
    KeyboardButton("Реферальная система")
]

menu = ReplyKeyboardMarkup(
    keyboard=[one, two, three],
    resize_keyboard=True,
    one_time_keyboard=False
)
