def roman_to_int(s):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    for char in s[::-1]:  # Идем с конца строки
        value = roman_dict.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Ввод данных
roman_number = input("Введите римское число: ")
try:
    arabic_number = roman_to_int(roman_number.upper())
    if 1 <= arabic_number <= 1999:
        print(f"Арабское число: {arabic_number}")
    else:
        print("Число должно быть от 1 до 1999.")
except KeyError:
    print("Неверный формат римского числа.")