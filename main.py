import time

login = '1'
password = '1'

# Хранение
class SteamUser:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
        self.games = {}
        self.friends = []

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

    def buy_game(self, game, price):
        if price <= self.balance:
            self.games[game] = price
            self.balance -= price
            print("Поздравляю! Вы купили игру", game)
            print("Остаток на счете:", self.balance)
        else:
            print("У вас недостаточно средств для покупки игры", game)

    def add_friend(self, friend):
        self.friends.append(friend)
        print("Вы добавили друга", friend)

    def show_games(self):
        print("\nСписок игр в магазине:")
        for game, price in self.games.items():
            print(game, "- $", price)

    def show_friends(self):
        print("\nСписок ваших друзей:")
        for friend in self.friends:
            print(friend)

    def view_balance(self):
        print("Ваш текущий баланс: $", self.balance)

# Создание инфы о пользователе
user1 = SteamUser("1", "1", 1000)
user1.games = {
    "Counter-Strike 2": 15,
    "Among Us": 1,
    "GTA V": 100
}

# Создание логина + пароля (конечно сложно, но по другому не получалось)
username_input = input("Введите ваш логин: ")
password_input = input("Введите ваш пароль: ")

if user1.login(username_input, password_input): 
    print("Вы успешно вошли в систему!")
    # Функционал
    while True:
        print("\nДоступные команды:")
        print("1. Посмотреть список игр")
        print("2. Купить игру")
        print("3. Добавить друга")
        print("4. Посмотреть список друзей")
        print("5. Посмотреть баланс")
        print("6. Выйти из Steam")

        choice = input("Введите номер команды: ")

        if choice == '1':
            user1.show_games()
        elif choice == '2':
            game_choice = input("Введите название игры, которую хотите купить: ")
            if game_choice in user1.games:
                user1.buy_game(game_choice, user1.games[game_choice])
            else:
                print("Данной игры нет в магазине.")
        elif choice == '3':
            friend_name = input("Введите имя друга: ")
            user1.add_friend(friend_name)
        elif choice == '4':
            user1.show_friends()
        elif choice == '5':
            user1.view_balance()
        elif choice == '6':
            print("До новых встреч в Steam!")
            time.sleep (1)
            break
        else:
            print("Неверная команда. Повторите ввод.")
else: 
    print("Ошибка входа. Пожалуйста, проверьте логин и пароль.")
    time.sleep (1)
    exit()                                                                                                                                                  
 
 # 1