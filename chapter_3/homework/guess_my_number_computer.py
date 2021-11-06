# Отгадай число
#
# Компьютер должен угадать случайное число в диапазоне от 1 до 100
# Игрок загадывает число и говорит,
# предположение больше/меньше, чем загаданное число,
# или попало в точку

import random
print("\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЗагадайте натуральное число из диапазона от 1 до 100.")
print("У меня есть всего 10 попыток.\nВы должны отвечать больше, меньше или верно. Не мухлюйте!")
# начальные значения
start, end = 1, 100
the_number = int(input("Введите число в диапазоне от 1 до 100: "))
tries = 0
answer = ""
# цикл отгадывания
while tries < 10:
    tries += 1
    computer_number = random.randint(start, end)
    answer = input(f"Ваше число {computer_number}? ")
    if answer.lower() != "верно" and computer_number == the_number:
        print("Ага! Вы меня обманули! А я угадал!")
        break
    elif answer.lower() == "больше":
        print("Окей, попробую еще раз.")
        start = computer_number + 1
    elif answer.lower() == "меньше":
        print("Окей, попробую еще раз.")
        end = computer_number - 1
    elif answer.lower() == "верно":
        print("Ура! Я угадал! :)")
        break
print(f"Использованное количество попыток = {tries}")
input("\nНажмите Enter, чтобы выйти.")