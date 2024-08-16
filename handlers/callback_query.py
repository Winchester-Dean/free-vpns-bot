import utils

from aiogram import types
from dispatcher import dp

from keyboards.keyboard import *

@dp.callback_query_handler(text="sub")
async def verify_user(msg: types.Message):
    status = await utils.check_sub(call.from_user.id)

    if status is False:
        return await msg.answer(
            "Пожалуйста подпишитесь на каналы:",
            reply_markup=inline_channels
        )
    else:
        return await msg.answer(
            "Добропожаловать в нашем боте!",
            reply_markup=menu
        )

