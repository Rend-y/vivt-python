def count_purchases(n):
    purchases = {}
    for _ in range(n):
        buyer, item, quantity = input().split()
        quantity = int(quantity)
        if buyer not in purchases:
            purchases[buyer] = {}
        if item not in purchases[buyer]:
            purchases[buyer][item] = 0
        purchases[buyer][item] += quantity

    for buyer, items in purchases.items():
        print(f"{buyer}:")
        for item, quantity in items.items():
            print(f"  {item}: {quantity}")

# Пример использования
n = int(input("Введите количество записей: "))
count_purchases(n)
