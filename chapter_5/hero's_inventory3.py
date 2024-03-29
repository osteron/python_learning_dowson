# Арсенал героя 3.0
# Демонстрирует работу со списками
# создадим список с несколькими элементами и выведем его с помощью цикла for
inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]
print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)
input("\nНажмите Enter, чтобы продолжить.")

# найдем длину списка
print(f"Сейчас в вашем распоряжении {len(inventory)} предмета/ов.")
input("\nНажмите Enter, чтобы продолжить.")

# проверка на принадлежность списку с помощью in
if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете.")

# вывод одного элемента с определенным индексом
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print(f"Под индексом {index} в арсенале находится {inventory[index]}.")

# отобразим срез
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("Введите конечный индекс среза: "))
print(f"Срез inventory[{start}:{finish}] - это {inventory[start:finish]}")
input("\nНажмите Enter, чтобы продолжить.")

# соединим два списка
chest = ["золото", "драгоценные камни"]
print(f"Вы нашли ларец. Вот что в нем есть: {chest}")
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print(f"Теперь в вашем распоряжении: {inventory}")
input("\nНажмите Enter, чтобы продолжить.")

# присваиваем значение элементу по индексу
print("Вы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print(f"Теперь ваш арсенал содержит следующие предметы: {inventory}")
input("\nНажмите Enter, чтобы продолжить.")

# приписываем значение элементам по срезу индексов
print("За золото и драгоценные камни вы купили магический кристалл, способный предсказывать будущее.")
inventory[4:6] = ["магический кристалл"]
print(f"Теперь в вашем распоряжении: {inventory}")
input("\nНажмите Enter, чтобы продолжить.")

# удаляем элемент
print("В тяжелом бою был раздроблен ваш щит.")
del inventory[2]
print(f"Вот что осталось в арсенале: {inventory}")
input("\nНажмите Enter, чтобы продолжить.")

# удаляем срез
print("Воры лишили вас арбалета и кольчуги.")
del inventory[:2]
print(f"В арсенале теперь только: {inventory}")
input("\nНажмите Enter, чтобы выйти.")