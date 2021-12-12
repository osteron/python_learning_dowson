# Отгадай число
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число, и компьютер говорит,
# предположение больше/меньше, чем загаданное число,
# или попало в точку
import random


def question():
    return "Ваше предположение: "


def ask_number(question):
    number = int(input(question))
    return number

def main():
    print("\tДобро пожаловать в игру 'Отгадай число'!")
    print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
    print("Постарайтесь отгадать его за минимальое число попыток.\n")
    # начальные значения
    the_number = random.randint(1, 100)
    guess = ask_number(question())
    tries = 1
    # цикл отгадывания
    while guess != the_number:
        if guess > the_number:
            print("Меньше...")
        else:
            print("Больше...")
        guess = ask_number(question())
        tries += 1
    print(f"Вам удалось отгадать число! Это в самом деле {the_number}.")
    print(f"Вы затратили на отгадывание всего лишь {tries} попыток!\n")


main()
input("\nНажмите Enter, чтобы выйти.")
