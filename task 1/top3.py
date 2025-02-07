from collections import Counter

def top3(st):
    # Убираем пробелы и считаем символы
    st = st.replace(" ", "")
    counter = Counter(st)
    top_3 = counter.most_common(3)
    result = ", ".join([f"{char} – {count}" for char, count in top_3])
    return result

# Ввод данных
text = input("Введите текст: ")
print(f"Топ-3 символов: {top3(text)}")