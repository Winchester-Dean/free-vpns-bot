import time
from database.db import DataBase

database = DataBase()

print(
    str(database.get_users()),
    str(database.get_admins()),
    str(database.get_channels())
)
time.sleep(10)