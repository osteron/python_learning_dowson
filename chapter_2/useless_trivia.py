# Бесполезные факты
#
# Узнает у пользователя его/ее личные данные и выдает несколько фактов
# о нем/ней. Эти факты истинны, но совершенно бесполезны.

name = input("Привет. Как тебя зовут? ")
age = input("Сколько тебе лет? ")
age = int(age)
weight = int(input("Хорошо, и последний вопрос. Сколько в тебе килограммов? "))

print("\nЕсли бы поэт Каммингс адресовал тебе письмо, он бы обратился к тебе так: ", name.lower())
print("А если бы это был рехнувшийся Каммингс, то так: ", name.upper())

called = name * 5
print("\nЕсли бы маленький ребенок решил привлечь твое внимание,")
print("он произнес бы твое имя так:")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nТвой нынешний возраст - свыше", seconds, "секунд.")

moon_weight = weight / 6
print("\nЗнаете ли вы, что на Луне весили бы всего", moon_weight, "кг?")
sun_weight = weight * 27.1
print("А вот находясь на Солнце, вы бы весили", sun_weight, "кг. (Но, увы, это продолжалось бы недолго...)")
input("\nНажмите Enter, чтобы выйти.")