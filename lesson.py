# required -- required data
# weight -- train weight
# axes--  number of axes
# press_coef -- coefficient of calculation of the required brake pressure
# pressresult -- required single brake press
# parking_axes -- manual brake axles required
# parking_axes_coef -- coefficient of calculation of required hand brakes in axles
# press_axes -- actual calculated click on the axis
# press_axes_coef -- coefficient for calculating the actual click

# press = weight * press_coef[0]
# print(press)
import math
from decimal import Decimal, getcontext

getcontext().prec = 5

out_result = {}
axes = int(input('Количество осей: ') or '0')
press_coef = [0.55, 0.33, 0.32, 0.31, 0.30]
weight = float(input('Вес поезда: ') or '0')
parking_axes = weight * 0.006

press_axes_list = {
    3.5: 0,
    4.5: 0,
    7.0: 0,
    7.5: 0,
    8.0: 0,
    8.5: 0
}

press_axes = {}
for k, v in press_axes_list.items():
    v = int(input(k) or '0')
    if v > 0:
        p = float(v) * k
        p = int(p)
        print(k, v, p)
        if v != 0:
            press_axes[k] = [v, p]
total_press_axes = [sum(i) for i in zip(*press_axes.values())]

# print(press_axes)
# print('Итого: ' + str(total_press_axes))
pressresult = 0
press_axes_list = list(press_axes_list)
for total in total_press_axes:
    if press_axes_list[2::] == 0:
        pressresult = Decimal(weight) * Decimal(press_coef[0])
    if press_axes_list[2::] != 0:
        if pressresult == 0:
            pressresult = [Decimal(weight) * Decimal(press_coef[1])]
        # if pressresult > total:
        #     pressresult = [Decimal(weight) * Decimal(press_coef[2])]
        # if pressresult > total:
        #     pressresult = [Decimal(weight) * Decimal(press_coef[3])]
        # if pressresult > total:
        #     pressresult = [Decimal(weight) * Decimal(press_coef[4])]

# pressresult = int(pressresult)

out_result.update({'Вес поезда: ': int(weight),
                   'Количество осей: ': axes,
                   'Требуемое нажатие: ': pressresult,
                   'Требуется ручных тормозных осей:': parking_axes,
                   press_axes.keys(): press_axes.values(),
                   'Итого: ': total_press_axes
                   })
print(out_result)
# print('Вес поезда: ' + str(int(weight)), 'Требуемое тормозное нажатие: ' + str(math.ceil(pressresult)))
# print('Требуется ручных тормозов: ' + str(math.ceil(parking_axes)), 'Всего осей: ' + str(axes))
