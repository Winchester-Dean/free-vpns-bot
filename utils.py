from aiogram import types
from dispatcher import bot

from database.db import DataBase

database = DataBase()

def get_args(msg):
    args = msg.text.split()
    return args

def get_args_raw(msg):
    args = msg.text.split(maxsplit=1)
    return args

async def check_sub(user_id: int):
    channels = database.get_channels_id()
    stats = []
    
    for channel_id in channels:
        for chid in channel_id:
            status = await bot.get_chat_member(
                f"-100{chid}", user_id
            )
            stats.append(status["status"])
    
    if "left" in stats:
        return False
    else:
        return True

def check_admin(user_id: int):
    admins = database.get_admins_id()
    
    for admin in admins:
        if (user_id,) == admin:
            return True
        else:
            return False

def user_in_db(user_id: int):
    users = database.get_users_id()
    
    if (user_id,) not in users:
        return False
    else:
        return True

