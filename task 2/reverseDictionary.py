def reverse_dictionary(ru_en_dict):
    en_ru_dict = {v: k for k, v in ru_en_dict.items()}
    return en_ru_dict

# Пример использования
ru_en_dict = {
    "яблоко": "apple",
    "кот": "cat",
    "собака": "dog"
}
en_ru_dict = reverse_dictionary(ru_en_dict)
print("Англо-русский словарь:", en_ru_dict)
