# Программа реализует подбрасывание монеты 100 раз и сообщает, сколько раз
# выпал орел и решка
import random
eagle = 0
tails = 0
count = 1
while count < 101:
    # если 1 - орел, 2 - решка
    if random.randint(1, 2) == 1:
        eagle += 1
    else:
        tails += 1
    count += 1
print(f"Орел выпал {eagle} раз, решка {tails} раз.")