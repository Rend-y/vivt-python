def commonElements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = sorted(set1.intersection(set2))
    return common

# Пример использования
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common_elements(list1, list2)
print("Общие элементы:", result)
