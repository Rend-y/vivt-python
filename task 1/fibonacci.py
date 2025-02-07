def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Ввод данных
n = int(input("Введите количество элементов ряда Фибоначчи: "))
print(f"Ряд Фибоначчи: {fibonacci(n)}")