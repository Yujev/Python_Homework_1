# Задача 2
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input("Введи значение X: "))
y = bool(input("Введи значение Y: "))
z = bool(input("Введи значение Z: "))

if not(x or y or z) == (not x and not y and not z):
    print(True)
else:
    print(False)
