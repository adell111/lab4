string = input("Введите ваше выражение через пробел: ")
string = string.split() # Сплитим по пробелам

if len(string) < 3:
    raise ValueError("Выражение не полное")
else:
    first = float(string[0])
    second = float(string[2]) # Выделяем первое и второе число.Ы
    match string[1]:
        case '+':
            print(f"Результат: {first+second}")
        case '-':
            print(f"Результат: {first-second}")
        case '/':
            if second == 0:
                raise ZeroDivisionError("На ноль делить нельзя.")
            print(f"Результат: {first/second}")
        case '*':
            print(f"Результат: {first*second}")
        case _:
            print('Данной операции нет.')
        
