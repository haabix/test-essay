import sqlite3
from funcs import hashstring
from termcolor import colored

import sqlite3
import hashlib
from termcolor import colored


def hashstring(string: str):
    return hashlib.sha256(string.encode()).hexdigest()


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def _execute(self, query, params=()):
        """Выполняет SQL-запрос и возвращает курсор с результатом"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    def init_db(self):
        self._execute("""
            CREATE TABLE IF NOT EXISTS users (
                login TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL
            )
        """)
        print(colored("[+] Таблица пользователей готова.", "green"))

    def register(self, login, password):
        password_hash = hashstring(password)
        try:
            self._execute(
                "INSERT INTO users (login, password_hash) VALUES (?, ?)",
                (login, password_hash)
            )
            print(colored(f"✅ Пользователь {login} зарегистрирован.", "green"))
            return True
        except sqlite3.IntegrityError:
            print(colored(f"❌ Ошибка: пользователь {login} уже существует.", "red"))
            return False

    def login(self, login, password):
        password_hash = hashstring(password)
        cursor = self._execute("SELECT password_hash FROM users WHERE login = ?", (login,))
        row = cursor.fetchone()

        if row and row[0] == password_hash:
            print(colored("✅ Вход разрешён.", "green"))
            return True
        else:
            print(colored("❌ Ошибка: неверный логин или пароль.", "red"))
            return False
                
db = Database('file.db')
