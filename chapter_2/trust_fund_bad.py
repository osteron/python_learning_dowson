# Рантье (версия с ошибкой)
# Демонстрирует логическую ошибку
print(
    """
            Рантье
Программа подсчитывает ваши ежемесячные расходы. Эту статистику нужно знать, чтобы
у вас не закончились деньги и вам не пришлось искать работу.
Введите суммы расходов по всем статьям, перечисляемым ниже. Вы богаты - так не ме-
лочитесь, пишите суммы в долларах, без центов.
    """
)
car = input("Техническое обслуживание машины 'Ламборгини': ")
rent = input("Съем роскошной квартиры на Манхэттене: ")
jet = input("Аренда самолета: ")
gifts = input("Подарки: ")
food = input("Обеды и ужины в ресторанах: ")
staff = input("Жалованье прислуши (дворецкий, повар, водитель, секретарь): ")
guru = input("Плата личному психоаналитику: ")
games = input("Компьютерные игры: ")
total = car + rent + jet + gifts + food + staff + guru + games
print("\nОбщая сумма:", total)
input("\nНажмите Enter, чтобы выйти.")