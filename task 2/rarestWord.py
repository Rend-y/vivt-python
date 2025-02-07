# task7.py
import re
from collections import Counter

def rarest_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    min_count = min(word_counts.values())
    rarest_words = [word for word, count in word_counts.items() if count == min_count]
    return min(rarest_words)

# Пример использования
text = "Это тестовая строка. Это строка для теста."
result = rarest_word(text)
print("Самое редкое слово:", result)
