import ast

# Ввод данных в формате словаря
input_str = input("Введите словарь (например, {'a': 1, 'b': 2, 'c': 1}): ")

try:
    # Преобразование строки в словарь
    input_dict = ast.literal_eval(input_str)  # Безопасное преобразование строки в словарь
    
    # Проверка, что введённый объект является словарём
    if not isinstance(input_dict, dict):
        raise ValueError("Введённые данные не являются словарём.")
    
    # Инверсия словаря
    inverted_dict = {}
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    
    # Вывод результата
    print(inverted_dict)
except Exception as e:
    print(f"Ошибка: {e}. Убедитесь, что вы ввели словарь в правильном формате.")