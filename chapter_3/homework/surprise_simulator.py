# Симулятор пирожка с сюрпризом - пять разных "сюрпризов"
import random
bakery = random.randint(1, 5)
print("Добрый день. Сегодня вам достался пирожок с...")
if bakery == 1:
    print("...картофелем и грибами")
elif bakery == 2:
    print("...луком и яйцом")
elif bakery == 3:
    print("...капустой")
elif bakery == 4:
    print("...мясом")
else:
    print("...пустотой :)")
input("\nНажмите Enter, чтобы выйти.")