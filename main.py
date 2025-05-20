from termcolor import colored
from funcs import hashstring
from database import db

def main():
    print(colored("Версия Python 3.11.2.", "blue"))
    print(colored("Рекомендую использовать DB Browser for SQLite", "cyan"))
    print(colored("-> https://sqlitebrowser.org/dl/ ", "magenta"))

    if input(colored('Продолжить? (Y)es/(N)o: ', 'cyan')).lower() != 'y':
        return
    
    text1, text2 = "Макухин Артем Сергеевич", "090301-ПОВа-о24"

    hexhash1 = hashstring(text1)
    hexhash2 = hashstring(text2)

    print(colored(f"🔐 Хэш строки '{text1}': {hexhash1}", "yellow"))
    print(colored(' часто применяется для сравнивания паролей\nВозьмем вторую строку, и сравним хэши', "cyan"))
    print(colored(f"🔐 Хэш строки '{text2}': {hexhash2}", "yellow"))

    result = colored("✔ Все норм, хэши не равны. так и надо", "green") if (hexhash1 != hexhash2) else colored("💩 Хеши равны, значит у меня говнокод", "red")
    print(result)

    print(colored("\nхэширование и хэш-таблицу можно разобрать на примере :)", "cyan"))
    
    while True:
        print(colored("\n=== Регистрация пользователя ===", "blue"))
        login = input(colored("Введите логин: ", "blue"))
        password = input(colored("Введите пароль: ", "blue"))
        password_hash = hashstring(password)
        if db.register(login, password_hash):
            break
        
    while True:
        print(colored("\n=== Вход в систему ===", "blue"))
        login_input = input(colored("Введите логин: ", "blue"))
        pass_input = input(colored("Введите пароль: ", "blue"))
        pass_hash = hashstring(pass_input)
        if db.login(login_input, pass_hash):
            break
        

    print(colored("\n=== Попытки сравнения паролей по их хэшу ===", "blue"))
    for i in range(2):
        print(colored(f"Попытка {i+1}/2", "yellow"))
        wheakpass = input(colored("Введу пароль: ", "blue"))
        anothertry = input(colored("Введу второй пароль, верный или нет, не важно: ", "blue"))

        print(colored("🔎 Сравнение хешей...", "magenta"))
        result = colored("🎉 Пароли одинаковы ♥", "green") if hashstring(wheakpass) == hashstring(anothertry) else colored("💥 Пароли разные, упс...", "red")
        print(result)

    print('Спасибо за уделенное время :)')

if __name__ == "__main__":
    db.init_db()
    main()