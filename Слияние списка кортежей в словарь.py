# Ввод данных в формате списка кортежей
input_str = input("Введите список кортежей")

try:
    # Преобразование строки в список кортежей
    input_list = eval(input_str)  # Используем eval для преобразования строки в объект
    
    # Проверка, что введённый объект является списком кортежей
    if not isinstance(input_list, list) or not all(isinstance(item, tuple) and len(item) == 2 for item in input_list):
        raise ValueError("Введённые данные не являются списком кортежей.")
    
    # Преобразование списка кортежей в словарь
    output_dict = dict(input_list)
    
    # Вывод результата
    print(output_dict)
except Exception as e:
    print(f"Ошибка: {e}. Убедитесь, что вы ввели список кортежей в правильном формате.")