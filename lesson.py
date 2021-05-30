# Калькулятор расчёта справки об обеспечении поезда тормозами и исправном их действии

import math
from decimal import Decimal, getcontext

getcontext().prec = 5

out_result = {}  # Словарь для сбора всех расчётов
axes = int(input('Количество осей: '))
press_coef = [.55, .33, .32, .31, .3]
press_coef_hint = ''
weight = float(input('Вес поезда: ') or '0')
parking_axes = weight * .006  # Расчитываем требуемое количество ручных тормозных осей
parking_axes = math.ceil(parking_axes)
while parking_axes % 4 != 0:  # Округляем значение
    parking_axes += 1  # до кратного 4

press_axes_list = {
    3.5: 0,
    4.5: 0,
    7.0: 0,
    7.5: 0,
    8.0: 0,
    8.5: 0
}  # Коеффициент тормозного нажатия в пересчёте на количество осей

press_axes = {}  # Сюда переносим ключ: значение из press_axes_list если значение != 0

# Здесь расчитваем тормозное нажатие для каждой пары и заносим и заносим все данные в press_axes
for k, v in press_axes_list.items():
    v = (int(input(k) or '0'))
    if v > 0:
        p = float(v) * k
        p = int(p)
        print(k, v, p)
        if v != 0:
            press_axes[str(k)] = v, p

# Подсчитываем итоговые данные количества тормозных осей и фактического тормозного нажатия
total_press_axes = [sum(i) for i in zip(*press_axes.values())]

pressresult = 0  # Требуемое тормозное нажатие расчитывается в условиях ниже
for total in total_press_axes[::]:
    if '7.0' or '7.5' or '8.0' or '8.5' in press_axes:
        pressresult = (weight * press_coef[1])
        if pressresult > total:
            pressresult = (weight * press_coef[2])
            press_coef_hint = 'Расчёт по ' + str(press_coef[2]) + ' тс'
        elif pressresult > total:
            pressresult = (weight * press_coef[3])
            press_coef_hint = 'Расчёт по ' + str(press_coef[3]) + ' тс'
        elif pressresult > total:
            pressresult = (weight * press_coef[4])
            press_coef_hint = 'Расчёт по ' + str(press_coef[4]) + ' тс'
    else:  # Если в словарь не попали перечисленные ключи, то выполняем расчёт ниже
        pressresult = (weight * press_coef[0])

# Заполняем словарь  итоговыми расчётами
out_result.update({1: ('Вес поезда:', int(weight)),
                   2: ('Количество осей:', axes),
                   3: ('Требуемое нажатие:', math.ceil(pressresult), press_coef_hint),
                   4: ('Требуется ручных тормозных осей:', parking_axes),
                   5: ('Фактическое нажатие:', press_axes),
                   6: ('Итого:', total_press_axes)
                   })

print(out_result)
