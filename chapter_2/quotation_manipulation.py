# Манипуляции с цитатой
# Демонстрирует строковые методы
# цитата из Томаса Уотсона, который в 1943 г. был директором IBM
quote = "Думаю, на мировом рынке можно будет продать штук пять компьютеров."
print("Исходная цитата:")
print("\nОна же в верхнем регистре:")
print(quote.upper())
print("\nВ нижнем регистре:")
print(quote.lower())
print("\nКак заголовок:")
print(quote.title())
print("\nС ма-а-аленькой заменой:")
print(quote.replace("штук пять", "несколько миллионов"))
print("\nА вот опять исходная цитата:")
print(quote)
input("\nНажмите Enter, чтобы выйти.")