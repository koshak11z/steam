import time

# Создание массива
# [username, password, balance, games, friends]
user1 = ["1", "1", 1000, {"Counter-Strike 2": 15, "Among Us": 1, "GTA V": 100}, []]

# Ввод логина и пароля
username_input = input("Введите ваш логин: ")
password_input = input("Введите ваш пароль: ")

# Проверка логина и пароля
if user1[0] == username_input and user1[1] == password_input:
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
            print("\nСписок игр в магазине:")
            for game, price in user1[3].items():
                print(game, "- $", price)
                
        elif choice == '2':
            game_choice = input("Введите название игры, которую хотите купить: ")
            if game_choice in user1[3]:
                if user1[2] >= user1[3][game_choice]:
                    user1[2] -= user1[3][game_choice]
                    print("Поздравляю! Вы купили игру", game_choice)
                    print("Остаток на счете:", user1[2])
                else:
                    print("У вас недостаточно средств для покупки игры", game_choice)
            else:
                print("Данной игры нет в магазине.")
                
        elif choice == '3':
            friend_name = input("Введите имя друга: ")
            user1[4].append(friend_name)
            print("Вы добавили друга", friend_name)
            
        elif choice == '4':
            print("\nСписок ваших друзей:")
            for friend in user1[4]:
                print(friend)
                
        elif choice == '5':
            print("Ваш текущий баланс: $", user1[2])
            
        elif choice == '6':
            print("До новых встреч в Steam!")
            time.sleep(1)
            break
            
        else:
            print("Неверная команда. Повторите ввод.")
else:
    print("Ошибка входа. Пожалуйста, проверьте логин и пароль.")
    time.sleep(1)
    exit()
                                     