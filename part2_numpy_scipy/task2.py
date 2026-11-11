

import numpy as np

while True:
    try:
        lengths = np.array(input("Введите длины участков через пробел: ").split(), dtype=float)
        speeds = np.array(input("Введите скорости на участках через пробел: ").split(), dtype=float)
    except ValueError:
        print("Ошибка: нужно вводить только числа (например: 12 7 15). Попробуйте снова.\n")
        continue

    if lengths.size == 0 or speeds.size == 0:
        print("Ошибка: строка не должна быть пустой. Попробуйте снова.\n")
        continue
    if lengths.size != speeds.size:
        print(f"Ошибка: длин {lengths.size}, а скоростей {speeds.size}. Количество должно совпадать.\n")
        continue
    if not (np.all(np.isfinite(lengths)) and np.all(np.isfinite(speeds))):
        print("Ошибка: значения nan и inf недопустимы.\n")
        continue
    if np.any(lengths <= 0) or np.any(speeds <= 0):
        print("Ошибка: длины и скорости должны быть больше нуля.\n")
        continue
    break

n = lengths.size


while True:
    try:
        k = int(input("Введите номер участка въезда k: "))
        p = int(input("Введите номер участка выезда p: "))
    except ValueError:
        print("Ошибка: k и p должны быть целыми числами. Попробуйте снова.\n")
        continue

    if k < 1 or p > n or k > n or p < 1:
        print(f"Ошибка: номера участков должны быть от 1 до {n}.\n")
        continue
    if k > p:
        print("Ошибка: k не должно быть больше p.\n")
        continue
    break


seg_len = lengths[k - 1:p]
seg_speed = speeds[k - 1:p]

seg_time = seg_len / seg_speed         
S = seg_len.sum()                   
T = seg_time.sum()                   
V = S / T                              

print(f"\nS = {S:.2f} км, T = {T:.2f} ч, V = {V:.2f} км/ч")

while True:
    try:
        t = float(input(f"Введите время t в часах (от 0 до {T:.2f}): "))
    except ValueError:
        print("Ошибка: t должно быть числом. Попробуйте снова.\n")
        continue

    if not np.isfinite(t) or t < 0:
        print("Ошибка: t должно быть неотрицательным числом.\n")
        continue
    if t > T:
        print(f"Ошибка: t больше общего времени в пути ({T:.2f} ч).\n")
        continue
    break


cum_time = np.cumsum(seg_time)


idx = np.searchsorted(cum_time, t)

if idx == 0:
    time_before = 0
else:
    time_before = cum_time[idx - 1]

distance = (t - time_before) * seg_speed[idx]  
segment_number = k + idx                         

print(f"Через {t:g} ч автомобиль на участке {segment_number}, в {distance:.1f} км от его начала")
