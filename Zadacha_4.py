# Задача 4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print("Введи номер четверти: ")
number = int(input())
if number == 1:
    print("Диапазон возможных значений 1 четверти: x > 0, y > 0 ")
elif number == 2:
    print("Диапазон возможных значений 2 четверти: x < 0, y > 0 ")
elif number == 3:
    print("Диапазон возможных значений 3 четверти: x < 0, y < 0 ")
elif number == 4:
    print("Диапазон возможных значений 4 четверти: x > 0, y < 0 ")
else:
    print(" Такой четверти нет! ")
