import os

from aiogram.utils import executor
from dispatcher import dp
from handlers import *

if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    executor.start_polling(dp, skip_updates=True)

