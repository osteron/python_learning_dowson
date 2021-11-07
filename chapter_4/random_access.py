# Случайные буквы
# Демонстрирует индексацию строк
import random
word = "индекс"
print(f"В переменной word хранится слово {word}.\n")
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print(f"word[{position}]\t {word[position]}")
input("\nНажмите Enter, чтобы выйти.")