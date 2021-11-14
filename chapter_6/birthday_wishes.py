# День рождения
# Демонстрирует именованные аргументы и значения параметров по умолчанию
# позиционные параметры
def birthday1(name, age):
    print(f"С днем рождения {name}! Вам сегодня исполняется {age}, не так ли?\n")


def birthday2(name = "товарищ Иванов", age = 1):
    print(f"С днем рождения {name}! Вам сегодня исполняется {age}, не так ли?\n")


birthday1("товарищ Иванов", 1)
birthday1(1, "товарищ Иванов")
birthday1(name = "товарищ Иванов", age = 1)
birthday1(age = 1, name = "товарищ Иванов")
birthday2()
birthday2(name = "Катя")
birthday2(age = 12)
birthday2(name = "Катя", age = 12)
birthday2("Катя", 12)
input("\nНажмите Enter, чтобы выйти.")