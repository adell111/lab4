a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
print(f"Максимальное число: {max(a,b,c)}")

if a >= c and a >= b: 
    print(f"Максимальное число: {a}")
elif c >= a and c >= b:
    print(f"Максимальное число: {c}")
else:
    print(f"Максимальное число: {b}")

    