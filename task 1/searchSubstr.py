def search_substr(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"

# Ввод данных
subst = input("Введите подстроку: ")
st = input("Введите строку: ")
print(search_substr(subst, st))