import time
from database.db import DataBase

database = DataBase()

print(
    str(database.get_referals(6099758454))
)
