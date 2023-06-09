# Задание 4.
#
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.
#
# Пример:
# Введите выручку фирмы: 1000
# Введите издержки фирмы: 500
# Финансовый результат - прибыль. Ее величина: 500
# Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
# Рентабельность выручки = 0.5
# Введите численность сотрудников фирмы: 10
# Прибыль фирмы в расчете на одного сотрудника = 50.0

proceed = int(input("Введите выручку фирмы: "))
outlay = int(input("Введите издержки фирмы: "))
if proceed > outlay:
    profitability = proceed-outlay
    rentab = profitability/proceed
    print(f"У вас прибыль, выручка составляет: {profitability} ")
    worker = int(input("Введите число сотрудников: "))
    print(f"{profitability/worker} на одного сотрудника")
elif proceed == outlay:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")