

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

axes = int(input('Количество осей: ') or '0')
press_coef = [0.33, 0.55]
weight = float(input('Вес поезда: ') or '0')
parking_axes = weight * 0.006

press_axes_list = {
    3.5: 0.0,
    4.5: 0.0,
    7.0: 0.0,
    7.5: 0.0,
    8.0: 0.0,
    8.5: 0.0
}

press_axes = {}
for k, v in press_axes_list.items():
    v = float(input(k) or '0')
    if v > 0:
        s = v * k
        print(k, v, s)
        if v != 0:
            for i in range(6):
                i = i + 1
                r = [k, v, s]
                press_axes = r

print(press_axes)
press_axes_list = list(press_axes_list)
if press_axes_list[2::] == 0:
    pressresult = Decimal(weight) * Decimal(press_coef[1])
else:
    pressresult = Decimal(weight) * Decimal(press_coef[0])
print('Вес поезда: ' + str(int(weight)), 'Требуемое тормозное нажатие: ' + str(math.ceil(pressresult)))
print('Требуется ручных тормозов: ' + str(math.ceil(parking_axes)), 'Всего осей: ' + str(axes), end='\n')
