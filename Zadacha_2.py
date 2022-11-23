# Задача 2
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# X Y Z     X Y Z
# 1 1 1     0 0 0
# 1 1 0     0 0 1
# 1 0 1     0 1 0
# 0 1 1     1 0 0


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not (x or y or z) == (not x and not y and not z):
                print(f' {x} {y} {z} - True')
            else:
                print(f' {x} {y} {z} - False')

