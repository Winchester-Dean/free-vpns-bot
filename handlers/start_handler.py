import utils

from database.db import DataBase
from config import balance

from aiogram import types
from dispatcher import dp

from .keyboards.keyboard import *

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    args = utils.get_args()
    user_id = msg.from_user.id
    name = msg.from_user.first_name
    status = await utils.check_sub(user_id)
    user_status = utils.user_in_db(user_id)

    if status is False:
        return await msg.answer(
            "Пожалуйста подпишитесь на каналы:",
            reply_markup=inline_channels
        )

    if user_status is False:
        if len(args) == 2:
            if args[1].isdigit():
                referer_id = int(args[1])
                
                try:
                    database.add_user(
                        user_id, name, referer_id
                    )
                except Exception as error:
                    await msg.answer(error)

                try:
                    database.update_balance(
                        referer_id, balance
                    )
                except Exception as error:
                    await msg.answer(error)
                
                await msg.answer(
                    "Добропожаловать в нашем боте!",
                    reply_markup=menu
                )
        else:
            try:
                database.add_user(
                    user_id, name
                )
            except Exception as error:
                await msg.answer(error)

            await msg.answer(
                "Добропожаловать в нашем боте!",
                reply_markup=menu
            )
    
    await msg.answer(
        "Добропожаловать в нашем боте!",
        reply_markup=menu
    )

