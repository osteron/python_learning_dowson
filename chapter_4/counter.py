# Считалка
# Демонстрирует использование функции range()
print("Посчитаем:")
for i in range(1, 11):
    print(i, end=' ')
print("\nПеречислим кратые пяти:")
for i in range(5, 50, 5):
    print(i, end=' ')
print("\nПосчитаем в обратном порядке:")
for i in range(10, 0, -1):
    print(i, end=' ')
input("\nНажмите Enter, чтобы выйти.")