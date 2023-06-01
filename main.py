import random

print("Игра: Камень, ножницы, бумага")

options = ["камень", "ножницы", "бумага"]

while True:
    player_choice = input("Выберите ваш вариант: ")
    while player_choice.lower() not in options:
        print("Некорректный ввод. Попробуйте еще раз.")
        player_choice = input()
    
    computer_choice = random.choice(options)
    print(f"Вы выбрали {player_choice}, а компьютер выбрал {computer_choice}.")
    
    if player_choice.lower() == computer_choice:
        print("Ничья!")
    elif (player_choice.lower() == "камень" and computer_choice == "ножницы") or \
         (player_choice.lower() == "ножницы" and computer_choice == "бумага") or \
         (player_choice.lower() == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли!")
    
    play_again = input("Сыграем еще раз? (Да/Нет) ")
    if play_again.lower() == 'нет':
        break

print("Спасибо за игру!")
