# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None
while choice != 0:
    print(
        """
        Рекорды 2.0
        0 - выйти
        1 - показать рекорды
        2 - добавить рекорд
        """
    )
    choice = input("Ваш выбор: ")
    print()
    # выход
    if choice == "0":
        print("До свидания.")
    # вывод таблицы рекордов
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(f"{name}\t{score}")
    # добавить рекорд
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = score[:5]  # в списке остается только 5 рекордов
    # непонятный ввод пользователя
    else:
        print(f"Извините, в меню нет пункта {choice}.")
input("\nНажмите Enter, чтобы выйти.")