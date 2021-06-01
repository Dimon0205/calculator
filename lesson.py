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

press_axes = []  # Сюда переносим ключ: значение из press_axes_list если значение != 0
press_axes_list = [3.5, 4.5, 7.0, 7.5, 8.0, 8.5]  # Коеффициент тормозного нажатия в пересчёте на количество осей
total_press_axes = []
r = []
for c in press_axes_list[::]:
    d = int(input([c]) or 0)
    if d > 0:
        v = float(d) * c
        v = int(v)
        press_axes.append([c, d, v])
        r.append([d, v])

# Подсчитываем итоговые данные количества тормозных осей и фактического тормозного нажатия
total_press_axes = ([sum(i) for i in zip(*r[::])])

# Требуемое тормозное нажатие расчитывается в условиях ниже
n = len(press_axes)
for i in range(n):
    if all(c not in [7.0, 7.5, 8.0, 8.5] for c in press_axes[i]):
        pressresult = Decimal(weight) * Decimal(press_coef[0])
    else:
        for total in total_press_axes[1:]:
            pressresult = Decimal(weight) * Decimal(press_coef[1])
            press_coef_hint = 'Расчёт по ' + str(press_coef[1]) + ' тс'
            if pressresult > total:
                pressresult = Decimal(weight) * Decimal(press_coef[2])
                press_coef_hint = 'Расчёт по ' + str(press_coef[2]) + ' тс'
            elif pressresult > total:
                pressresult = Decimal(weight) * Decimal(press_coef[3])
                press_coef_hint = 'Расчёт по ' + str(press_coef[3]) + ' тс'
            elif pressresult > total:
                pressresult = Decimal(weight) * Decimal(press_coef[4])
                press_coef_hint = 'Расчёт по ' + str(press_coef[4]) + ' тс'

out_result = {}

filname = 'out_result.json'
with open(filname, 'w', encoding="utf-8") as out:
    json.dump(

        [
            ['Вес поезда:', weight],
            ['Количество осей:', axes],
            ['Требуе мое нажатие:', math.ceil(pressresult), press_coef_hint],
            ['Требуется ручных тормозных осей:', parking_axes],
            ['Фактическое нажатие:', press_axes],
            ['Итого:', total_press_axes]
        ], out, ensure_ascii=False

    )
