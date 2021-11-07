# Только согласные
# Демонстрирует, как создавать новые строки из исходных с помощью цикла for
message = input("Введите текст: ")
new_message = ""
VOWELS = "aeiouаеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print(f"Создана новая строка: {new_message}")
print(f"\nВот ваш текст с изъятыми глаными буквами: {new_message}")
input("\nНажмите Enter, чтобы выйти.")8