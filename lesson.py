# Калькулятор расчёта справки об обеспечении поезда тормозами и исправном их действии

import json
import math
from decimal import Decimal, getcontext

getcontext().prec = 5

while True:
    try:
        axes = int(input('Количество осей: ') or 0)
        if axes % 4 or axes <= 0:
            raise Exception()
        break
    except Exception:
        print('Количество осей должно быть кратно 4 и не иметь отрицательного числа!')
while True:
    try:
        weight = float(input('Вес поезда: ') or '0')
        if weight > 9000 or weight < 0:
            raise Exception()
        break
    except Exception:
        print('Вес не должен быть меньше 0 и болше 9000 тонн!')

press_coef = [.55, .33, .32, .31, .3]
press_coef_hint = ''
parking_axes = weight * .006  # Расчитываем требуемое количество ручных тормозных осей
parking_axes = math.ceil(parking_axes)
if parking_axes % 4:  # Округляем значение
    parking_axes += 4 - parking_axes % 4  # до кратного 4

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
            press_axes[k] = v, p

# Подсчитываем итоговые данные количества тормозных осей и фактического тормозного нажатия
total_press_axes = [sum(i) for i in zip(*press_axes.values())]

pressresult = 0  # Требуемое тормозное нажатие расчитывается в условиях ниже
for total in total_press_axes[::]:
    if not press_axes.keys() & {7.0, 7.5, 8.0, 8.5}:
        pressresult = Decimal(weight) * Decimal(press_coef[0])
    else:  # Если в словарь не попали перечисленные ключи, то выполняем расчёт ниже
        if pressresult <= total:
            pressresult = Decimal(weight) * Decimal(press_coef[1])
            press_coef_hint = 'Расчёт по ' + str(press_coef[1]) + ' тс'
        elif pressresult > total:
            pressresult = Decimal(weight) * Decimal(press_coef[2])
            press_coef_hint = 'Расчёт по ' + str(press_coef[2]) + ' тс'
        elif pressresult > total:
            pressresult = Decimal(weight) * Decimal(press_coef[3])
            press_coef_hint = 'Расчёт по ' + str(press_coef[3]) + ' тс'
        elif pressresult > total:
            pressresult = Decimal(weight) * Decimal(press_coef[4])
            press_coef_hint = 'Расчёт по ' + str(press_coef[4]) + ' тс'

# Заполняем словарь  итоговыми расчётами
# out_result = {
#                 "Количество осей:": axes,
#                 "Требуемое нажатие:": math.ceil(pressresult) press_coef_hint,
#                 "Требуется ручных тормозных осей:": parking_axes,
#                 "Фактическое нажатие:": press_axes,
#                 "Итого:": total_press_axes
#
# }
out_result = {}

filname = 'out_result.json'
with open(filname, 'w', encoding="utf-8") as out:
    json.dump([
        'Вес поезда:', weight,
        'Количество осей:', axes,
        'Требуемое нажатие:', math.ceil(pressresult), press_coef_hint,
        'Требуется ручных тормозных осей:', parking_axes,
        'Фактическое нажатие:', press_axes,
        'Итого:', total_press_axes
    ], out, ensure_ascii=False, )


