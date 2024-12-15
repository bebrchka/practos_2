from functools import reduce

def authenticate_user(users):
    login = input("LOGIN: ")
    password = input("PASSWORD: ")
    if login == users["login"] and password == users["password"]:
        print("ВЫ УСПЕШНО ВОШЛИ В АККАУНТ")
        return True
    return False

def authenticate_admin(admin):
    login = input("LOGIN: ")
    password = input("PASSWORD: ")
    if login == admin["login"] and password == admin["password"]:
        print("ВЫ УСПЕШНО ВОШЛИ В АККАУНТ администратора")
        return True
    return False

def view_attractions(dan_park):
    attractions = list(map(lambda d_p: d_p['аттракцион'], dan_park))
    print(f"\nСписок аттракционов: {attractions}")

def sort_attractions(dan_park):
    print("""
Укажите как вы хотите отсортировать данные о горках""")
    print("1. По цене от большего к меньшему")
    print("2. По цене от меньшего к большему")
    print("3. По алфавиту")
    print("4. По алфавиту от я до а")

    sort_choice = int(input("Ваш выбор: "))
    if sort_choice == 1:
        print("АТТРАКЦИОНЫ СОРТИРОВАНЫ ПО ЦЕНЕ(от max к min): ")
        elements = sorted(dan_park, key=lambda d_p: d_p["цена"], reverse=True)
    elif sort_choice == 2:
        print("АТТРАКЦИОНЫ СОРТИРОВАНЫ ПО ЦЕНЕ(от min к max): ")
        elements = sorted(dan_park, key=lambda d_p: d_p["цена"])
    elif sort_choice == 3:
        print("АТТРАКЦИОНЫ СОРТИРОВАНЫ ПО АЛФАВИТУ(от А до Я): ")
        elements = sorted(dan_park, key=lambda d_p: d_p["аттракцион"])
    elif sort_choice == 4:
        print("АТТРАКЦИОНЫ СОРТИРОВАНЫ ПО АЛФАВИТУ(от Я до А): ")
        elements = sorted(dan_park, key=lambda d_p: d_p["аттракцион"], reverse=True)
    else:
        print("Недопустимый выбор.")
        return

    # Используем zip для объединения аттракционов и цен
    attractions_and_prices = zip(map(lambda d_p: d_p['аттракцион'], elements), map(lambda d_p: d_p['цена'], elements))
    for attraction, price in attractions_and_prices:
        print(f"{attraction}: {price}")

def buy_ticket(dan_park, ist_pok):
    print(f"Выберите аттракцион (укажите его полное название): {list(map(lambda d_p: d_p['аттракцион'], dan_park))}")
    attrac_number = input()
    
    # Используем filter для поиска аттракциона
    found_attractions = list(filter(lambda attraction: attraction['аттракцион'] == attrac_number, dan_park))
    
    if found_attractions:
        attraction = found_attractions[0]  # Берем первый найденный аттракцион
        price = attraction['цена']
        oplata = int(input(f"К оплате {price}. Укажите сумму для оплаты: "))
        if oplata == price:
            print("ОПЛАТА ПРОШЛА УСПЕШНО! ПОЗДРАВЛЯЕМ С ПОКУПКОЙ БИЛЕТА")
            ist_pok.append({"билет на аттракцион": attrac_number, "оплата": "успешна!", "дата": "сегодня"})
        else:
            print("ВЫ НЕПРАВИЛЬНО УКАЗАЛИ СУММУ! ВАШ ПЛАТЕЖ ОТКЛОНЕН")
    else:
        print("Аттракцион не найден.")

def view_purchase_history(ist_pok):
    print("ВАША ИСТОРИЯ ПОКУПОК")
    print("аттракцион / оплата / дата")
    for ist in ist_pok:
        print(f"{ist['билет на аттракцион']} ({ist['оплата']}) - {ist['дата']}")

def update_user_data(users):
    print("ВАШИ ДАННЫЕ")
    print(users)

def admin_actions(dan_park, admin):
    while True:
        print("выберите действие")
        print("1. изменить логин и пароль")
        print("2. добавить новый аттракцион")
        print("3. удалить аттракцион")
        print("4. добавить скидки")  # если что уберу
        print("5. выйти")

        ad = int(input("Ваш выбор: "))
        if ad == 1:
            lg = input("NEW LOGIN: ")
            ps = input("NEW PASSWORD: ")
            admin.update({'login': lg, 'password': ps})
            print("вы успешно изменили логин и пароль!")
        elif ad == 2:
            na = input("Укажите новый аттракцион: ")
            ca = int(input("Укажите цену: "))
            dan_park.append({'аттракцион': na, 'цена': ca})
            print(f"Аттракцион '{na}' успешно добавлен.")
        elif ad == 3:
            existing_attractions = list(map(lambda d_p: d_p['аттракцион'], dan_park))
            print(f"Существующие аттракционы: {existing_attractions}")
            ld = input("Укажите аттракцион для удаления: ")
            # Используем filter для удаления аттракциона
            dan_park[:] = list(filter(lambda attraction: attraction['аттракцион'] != ld, dan_park))
            print(f"Аттракцион '{ld}' успешно удален." if ld in existing_attractions else "Аттракцион не найден.")
        elif ad == 4:
            print("Функция добавления скидок еще не реализована.")
        elif ad == 5:
            print("Вы вышли из аккаунта администратора.")
            break
        else:
            print("Недопустимый выбор.")

def main():
    print("Добро пожаловать в парк аттракционов!")
    print("Пожалуйста авторизуйтесь...")

    users = {
        "login": "user_1",
        "password": "12345",
        "role": "user",
        "subscribe": "premium",
        "visit_date": "12.12.2024"}

    admin = {
        "login": "ADMINISTRATOR",
        "password": "administrator",
        "role": "admin",}

    dan_park = [
        {"аттракцион": "американские горки", "цена": 1500},
        {"аттракцион": "молот судьбы", "цена": 1200},
        {"аттракцион": "бездна первого Крэнга", "цена": 800},
        {"аттракцион": "полет в тоннеле", "цена": 1000},
        {"аттракцион": "кобра", "цена": 900},
        {"аттракцион": "летняя школа", "цена": 500},
        {"аттракцион": "гонка будущего", "цена": 600}]

    ist_pok = [
        {"билет на аттракцион": "молот судьбы", "оплата": "успешна!", "дата": "12.12.2020"},
        {"билет на аттракцион": "полет в тоннеле", "оплата": "не прошла", "дата": "09.01.2021"},
        {"билет на аттракцион": "полет в тоннеле", "оплата": "успешна!", "дата": "09.01.2021"},
        {"билет на аттракцион": "гонка будущего", "оплата": "успешна!", "дата": "20.02.2021"},
        {"билет на аттракцион": "американские горки", "оплата": "успешна", "дата": "30.04.2021"}]

    while True:
        if authenticate_user(users):
            while True:
                print("Выберите действие: ")
                print("1. Просмотреть аттракционы")
                print("2. Сортировать цены и аттракционы")
                print("3. Купить билеты")
                print("4. Просмотреть историю покупок")
                print("5. Изdministratorменить данные профиля")

                d_u = int(input("Ваш выбор: "))
                if d_u == 1:
                    view_attractions(dan_park)
                elif d_u == 2:
                    sort_attractions(dan_park)
                elif d_u == 3:
                    buy_ticket(dan_park, ist_pok)
                elif d_u == 4:
                    view_purchase_history(ist_pok)
                elif d_u == 5:
                    update_user_data(users)
                else:
                    print("Недопустимый выбор.")

        elif authenticate_admin(admin):
            admin_actions(dan_park, admin)
        else:
            print("Пользователя с таким логином нет")

if __name__ == "__main__":
    main()