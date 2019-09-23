print("Вычисление площади треугольника по формуле Герона")
side_a = float(input(("Введите сторону 'a': ")))
side_b = float(input(("Введите сторону 'b': ")))
side_c = float(input(("Введите сторону 'c': ")))
p = (side_a + side_b + side_c)/2
S = (p*(p - side_a)*(p - side_b)*(p - side_c))**0.5
print("Площадь триугольника по формуле Герона равна: ", S)

