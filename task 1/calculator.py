def calculator():
    while True:
        print("\nВведите операцию (+, -, *, /) или '0' для выхода:")
        operation = input()
        if operation == '0':
            print("Выход из калькулятора.")
            break
        if operation not in ['+', '-', '*', '/']:
            print("Неверный знак операции!")
            continue

        x = float(input("Введите первое число (x): "))
        y = float(input("Введите второе число (y): "))

        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            if y == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = x / y

        print(f"Результат: {result}")

# Запуск калькулятора
calculator()