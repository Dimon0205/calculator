press_axes = []  # Сюда переносим ключ: значение из press_axes_list если значение != 0
press_axes_list = [3.5, 4.5, 7.0, 7.5, 8.0, 8.5]  # Коеффициент тормозного нажатия в пересчёте на количество осей
r=[]
for c in press_axes_list[::]:
    d = int(input([c]) or 0)
    if d > 0:
        v = float(d) * c
        v = int(v)
        press_axes.append([c, d, v])
        r.append([d, v])
total_press_axes=([sum(i) for i in zip(*r[::])])
print(press_axes)
print(total_press_axes)