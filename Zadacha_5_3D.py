# Задача 5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти раcстояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# 3D пространство:

import np as np
print("Расстояние между точками в 3D пространстве:")
print()
print("Введите координаты точки X1: ")
x1 = float(input())

print("Введите координаты точки Y1: ")
y1 = float(input())

print("Введите координаты точки Z1: ")
z1 = float(input())

print("Введите координаты точки X2: ")
x2 = float(input())

print("Введите координаты точки Y2: ")
y2 = float(input())

print("Введите координаты точки Z2: ")
z2 = float(input())

result = np.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2) + pow(z1 - z2, 2))
a = round(result, 2)
print()
print("Расстояние между точками равно: " f'{a}')
print()
