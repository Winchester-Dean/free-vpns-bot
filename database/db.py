import sqlite3

class DataBase:
    def __init__(
        self,
        directory: str = "database/database.db"
    ):
        self.connect = sqlite3.connect(directory)
        self.cursor = self.connect.cursor()

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    referer INTEGER,
                    balance INTEGER DEFAULT 0
                )
            """)
        
        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS keys(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL UNIQUE,
                    key TEXT NOT NULL UNIQUE,
                    country TEXT NOT NULL,
                    expired_date TEXT NOT NULL
                )
            """)

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS keys_list(
                    id INTEGER PRIMARY KEY,
                    key TEXT NOT NULL UNIQUE,
                    country TEXT NOT NULL,
                    expired_date TEXT NOT NULL
                )
            """)
        
        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS channels(
                    id INTEGER PRIMARY KEY,
                    channel_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    link TEXT NOT NULL
                )
            """)
        
        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS admins(
                    id INTEGER PRIMARY KEY,
                    admin_id INTEGER NOT NULL UNIQUE,
                    name TEXT NOT NULL
                )
            """)
    
    def add_user(
        self,
        user_id: int,
        name: str,
        referer: int = None
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO users(user_id, name, referer) "
                "VALUES(?, ?, ?)",
                [user_id, name, referer]
            )

    def add_key(
        self,
        user_id: int,
        key: str,
        country: str,
        expired_date: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO keys(user_id, key, country, expired_date) "
                "VALUES(?, ?, ?, ?)",
                [user_id, key, country, expired_date]
            )
    
    def add_keys_list(
        self,
        key: str,
        country: str,
        expired_date: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO keys_list(key, country, expired_date) "
                "VALUES(?, ?, ?)",
                [key, country, expired_date]
            )

    def add_channel(
        self,
        channel_id: int,
        name: str,
        link: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO channels(channel_id, name, link) "
                "VALUES(?, ?, ?)",
                [channel_id, name, link]
            )

    def add_admin(
        self,
        admin_id: int,
        name: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO admins(admin_id, name) "
                "VALUES(?, ?)",
                [admin_id, name]
            )

    def get_users(self):
        self.cursor.execute(
            "SELECT user_id, name, balance FROM users"
        )
        return self.cursor.fetchall()

    def get_users_id(self):
        self.cursor.execute(
            "SELECT users_id FROM users"
        )
        return self.cursor.fetchall()

    def get_referals(
        self,
        user_id: int
    ):
        self.cursor.execute(
            "SELECT COUNT(*) FROM users "
            "WHERE referer=?",
            [user_id]
        )
        return self.cursor.fetchone()

    def get_user_keys(
        self,
        user_id: int
    ):
        self.cursor.execute(
            "SELECT key, country, expired_date "
            "FROM keys WHERE user_id=?",
            [user_id]
        )
        return self.cursor.fetchall()

    def get_keys_list(self):
        self.cursor.execute(
            "SELECT key, country, expired_date FROM keys_list"
        )
        return self.cursor.fetchall()
    
    def get_channels(self):
        self.cursor.execute(
            "SELECT name, link FROM channels"
        )
        return self.cursor.fetchall()

    def get_channels_id(self):
        self.cursor.execute(
            "SELECT channel_id FROM channels"
        )
        return self.cursor.fetchall()

    def get_admins(self):
        self.cursor.execute(
            "SELECT admin_id, name FROM admins"
        )
        return self.cursor.fetchall()
    
    def get_admins_id(self):
        self.cursor.execute(
            "SELECT admin_id FROM admins"
        )
        return self.cursor.fetchall()
    
    def update_balance(
        self,
        user_id: int,
        balance: int
    ):
        with self.connect:
            self.cursor.execute(
                "UPDATE users SET balance=balance+? "
                "WHERE user_id=?",
                [balance, user_id]
            )

