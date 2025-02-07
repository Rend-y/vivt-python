def sum_and_product(arr):
    total_sum = sum(arr)
    product = 1
    for num in arr:
        product *= num
    return total_sum, product

# Пример использования
arr = [1, 2, 3, 4, 5]
sum_result, product_result = sum_and_product(arr)
print(f"Сумма: {sum_result}, Произведение: {product_result}")