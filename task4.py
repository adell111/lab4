from math import sqrt

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

if a == 0:
    print('Уравнение не является квадратным.')
else:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + sqrt(D)) / 2*a
        x2 = (-b - sqrt(D)) / 2*a
        print(f"Два корня: x1 = {x1:.2f}, x2 = {x2:.2f}") # Вывысти до 2 знаков после запятой
    elif D == 0:
        x1 = -b/(2*a)
        print(f'Один корень: x1 = {x1:.2f}')
    else:
        print("Корней нет")

