# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли
# какая-либо буква в слове, причем программа может отвечать только "Да" или "Нет.
# Вслед за тем игрок должен попробовать отгадать слово.

import random
# создадим кортеж со словами
WORDS = ("первое", "второе", "третье", "четвертое", "десерт")
# создадим начальные переменные
user_try = 1
number_of_letters = None
result = ""
# начало программы
print("Добро пожаловать в игру 'Угадай слово'!")
print("Я загадаю слово и скажу сколько в нем букв.")
print("Вы предлагаете какую-либо букву, а я говорю, есть ли эта буква в слове или нет.")
print("Вы можете предложить только пять букв. Далее вам нужно угадать слово целиком. Готовы?")
# выбор слова
word = random.choice(WORDS)
# цикл подбора букв
while user_try <= 5:
    char = input("Введите букву: ")
    if char in word:
        print("Да")
    else:
        print("Нет")
    user_try += 1
# попытка отгадать слово
result = input("А теперь попробуйте отгадать слово: ")
if result.lower() == word:
    print("Верно, вы угадали!")
else:
    print("Увы, вы не угадали.")
input("\nНажмите Enter, чтобы выйти.")