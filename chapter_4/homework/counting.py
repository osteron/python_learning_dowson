# Напишите программу, которая бы считала по просьбе пользователя.
# Надо позволить пользователю ввести начало и конец счета, а
# также интервал между называемыми целыми числами
print("В данной программе я буду считать за вас.")
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
step = int(input("Введите шаг диапазона: "))
# цикл счета
for i in range(start, end, step):
    print(i, end=' ')
input("\nНажмите Enter, чтобы выйти.")