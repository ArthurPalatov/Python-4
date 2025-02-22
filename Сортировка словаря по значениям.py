import ast

# Функция для сортировки словаря по значениям
def sort_dict_by_values(d):
    return sorted(d.items(), key=lambda x: x[1])

# Основная программа
if __name__ == "__main__":
    # Ввод данных в формате {'a': 3, 'b': 1, 'c': 2}
    input_str = input("Введите словарь: ")
    
    # Преобразование строки в словарь
    try:
        input_dict = ast.literal_eval(input_str)  # Безопасное преобразование строки в словарь
        if not isinstance(input_dict, dict):
            raise ValueError("Введённые данные не являются словарём.")
        
        # Сортировка словаря по значениям
        sorted_list = sort_dict_by_values(input_dict)
        
        # Вывод результата
        print(sorted_list)
    except (ValueError, SyntaxError):
        print("Ошибка: Введённые данные некорректны. Убедитесь, что вы ввели словарь в правильном формате.")