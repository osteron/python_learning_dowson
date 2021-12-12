# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try/except
try:
    num = float(input('Введите число: '))
except:
    print("Похоже, это не число!")
# обработка исключения определенного типа
try:
    num = float(input("Введите число: "))
except ValueError:
    print("Это не число!")
# обработка исключений нескольких разных типов
print()
for value in (None, 'Привет!'):
    try:
        print(f'Пытаюсь преобразовать в число: {value} -->', end=' ')
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже, это не число!")
print()
for value in (None, 'Привет!'):
    try:
        print(f'Пытаюсь преобразовать в число {value} -->', end=' ')
        print(float(value))
    except TypeError:
        print('Я умею преобразоывать только строки и числа!')
    except ValueError:
        print('Я умею преобразовывать только строки, составленные из цифр!')
# получение аргумента
try:
    num = float(input('\nВведите число: '))
except ValueError as e:
    print(f'Это не число! Интерпретатор как бы говорит нам: {e}')
# try/except/else
try:
    num = float(input('\nВведите число: '))
except ValueError:
    print("Это не число!")
else:
    print(f"Вы ввели число {num}.")
input('\nНажмите Enter, чтобы выйти.')