import utils

from aiogram import types
from dispatcher import dp

from .keyboards.keyboard import *

@dp.callback_query_handler(text="sub")
async def verify_user(call: types.CallbackQuery):
    status = await utils.check_sub(call.from_user.id)

    if status is False:
        return await call.message.answer(
            "Пожалуйста подпишитесь на каналы:",
            reply_markup=inline_channels
        )
    else:
        return await call.message.answer(
            "Добропожаловать в нашем боте!",
            reply_markup=menu
        )

