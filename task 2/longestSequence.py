def longest_sequence(arr):
    max_length = 1
    current_length = 1
    start_index = 0

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                start_index = i - max_length + 1
        else:
            current_length = 1

    return max_length, start_index

# Пример использования
arr = [1, 2, 2, 2, 3, 4, 4, 4, 4, 5]
length, start = longest_sequence(arr)
print(f"Длина последовательности: {length}, Начальный индекс: {start}")
