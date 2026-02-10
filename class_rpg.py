
from level_farm import level_farm

player = {
    "user": "",
    "age": 0,
    "hp": 0,
    "max_hp": 0,
    "damage": 0,
    "gold": 100,
    "exp": 0,
    "exp_to_lvl": 100,
    "hero": "",
    "levels_passed": 0
}

heroes = {
    1: {"name": "воин", "hp": 240, "max_hp": 240, "damage": 30},
    2: {"name": "ассасин", "hp": 180, "max_hp": 180, "damage": 44},
    3: {"name": "танк", "hp": 400, "max_hp": 400, "damage": 20}
}


def create_profile(player):
    input("нажмите - Enter, чтобы создать профиль:-> ")

    while True:
        
        user = input("придумайте уникальный юзер:-> ")
        if user.replace(" ", "").isalpha():
            player["user"] = user
            break
        else:
            print("ошибка ввода. попробуйте еще раз!")

    while True:

        age = input("введите ваш возраст:-> ")
        if age.isdigit():
            player["age"] = age
            break
        else:
            print("ошибка ввода. попробуйте еще раз!")

    



def edit_profile(player):
    if player["user"] == "":
        print("сначала создайте профиль!")
        return
    
    print("\n== выберите что изменить ==")
    print("1. user")
    print("2. age")
    print("3. ничего. выйти")

    edit_choice = input("выберите действие:-> ")

    if not edit_choice.isdigit():
        print("ошибка ввода. попробуйте еще раз!")
        return
    
    edit_choice = int(edit_choice)

    if edit_choice == 1:

        while True:
            
            new_user = input("придумайте новый юзер:-> ")
            if new_user.replace(" ", "").isalpha():
                player["user"] = new_user
                break
            else:
                print("ошибка ввода. попробуйте еще раз!")

    elif choice == 2:

        while True:

            new_age = input("введите ваш новый возраст:-> ")
            if new_age.isdigit():
                player["age"] = new_age
                break
            else:
                print("ошибка ввода. попробуйте еще раз!")

    elif choice == 3:
        print("выйти")
        return
    else:
        print("ошибка ввода. попробуйте еще раз!")


def choose_hero(player, heroes):
    print("\n== Герои ==")
    print("1. Воин: 240hp, 30dmg")
    print("2. ассасин: 180hp, 44dmg")
    print("3. танк: 400hp, 20dmg")

    hero_choice = input("выберите героя:-> ")

    if not hero_choice.isdigit():
        print("ошибка ввода. попробуйте еще раз!")
        return player
    
    hero_choice = int(hero_choice)

    if hero_choice == 1:
        player["hero"] = heroes[hero_choice]["name"]
        player["hp"] = heroes[hero_choice]["hp"]
        player["max_hp"] = heroes[hero_choice]["max_hp"]
        player["damage"] = heroes[hero_choice]["damage"]
        print(f"ваш новый герой: {player['hero']}")


    elif hero_choice == 2:
        player["hero"] = heroes[hero_choice]["name"]
        player["hp"] = heroes[hero_choice]["hp"]
        player["max_hp"] = heroes[hero_choice]["max_hp"]
        player["damage"] = heroes[hero_choice]["damage"]
        print(f"ваш новый герой: {player['hero']}")


    elif hero_choice == 3:
        player["hero"] = heroes[hero_choice]["name"]
        player["hp"] = heroes[hero_choice]["hp"]
        player["max_hp"] = heroes[hero_choice]["max_hp"]
        player["damage"] = heroes[hero_choice]["damage"]
        print(f"ваш новый герой: {player['hero']}")

    else:
        print("ошибка ввода. попробуйте еще раз!")


def battle_level(player, level):
    enemy = level_farm[level].copy()
    player["hp"] = player["max_hp"]
    print(f"вы встретили врага: {enemy['name']}")

    while player["hp"] > 0 and enemy["hp"] > 0:
        input("нажмите - Enter, чтобы атаковать:-> ")

        enemy["hp"] -= player["damage"]
        print(f"удар, у врага {enemy['hp']} хп")

        if enemy["hp"] <= 0:
            print(f"вы победили!")
            print(f"вы получили награду: {enemy['gold']} золота и {enemy['exp']} exp")
            player["gold"] += level_farm[level]["gold"]
            player["exp"] += level_farm[level]["exp"]
            break

        player["hp"] -= enemy["damage"]
        print(f"вас ударили, осталось {player["hp"]} хп")

        if player["hp"] <= 0:
            print("вы проиграли")
            break


def explore(player):
    print("\n== Исследование ==")
    print(f"пройденные уровни {player['levels_passed']}")
    print("0. выйти")

    for lvl in range(1, player['levels_passed'] + 2):
        print(f"{lvl}, {level_farm[lvl]['name']}" 
              f" hp: {level_farm[lvl]['hp']}, damage: {level_farm[lvl]['damage']}")
        
    choice = input("выберите уровень:-> ")

    if not choice.isdigit():
        print("ошибка ввода. попробуйте еще раз!")
        return
    
    choice = int(choice)

    if choice == 0:
        print("выйти")
        return
    
    if choice < 1 or choice > player['levels_passed'] + 1:
        print("этот уровень закрыт")
        return
    
    battle_level(player, choice)

    if player["hp"] > 0 and choice == player["levels_passed"] + 1:
        player["levels_passed"] += 1
        print(f"открыт новый уровень: {player['levels_passed']}")



while True:
    print("\n== Стартовое меню ==")
    print("1. создать профиль")
    print("2. изменить профиль")
    print("3. профиль")
    print("4. выбор класса")
    print("5. битва")
    print("6. выйти")

    choice = input("выберите действие:-> ")

    if not choice.isdigit():
        print("ошибка ввода. попробуйте еще раз!")
        continue

    choice = int(choice)

    if choice == 1:
        create_profile(player)

    elif choice == 2:
        edit_profile(player)

    elif choice == 3:
        if player["user"] == "" or player["hero"] == "":
            print("Сначала создайте профиль и выберите героя!")
        else:
            print("\n== Ваш профиль ==")
            print(f"user: {player['user']}")
            print(f"герой: {player['hero']}")
            print(f"hp: {player['hp']}")
            print(f"max_hp: {player['max_hp']}")
            print(f"damage: {player['damage']}")
            print(f"gold: {player['gold']}")
            print(f"exp: {player['exp']}")
            print(f"уровни пройдены: {player['levels_passed']}")

    elif choice == 4:
        choose_hero(player, heroes)

    elif choice == 5:
        explore(player)

    elif choice == 6:
        print("выйти")
        break
    else:
        print("ошибка ввода. попробуйте еще раз!")

