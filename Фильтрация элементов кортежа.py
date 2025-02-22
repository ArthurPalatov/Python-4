input_str = input("Введите кортеж чисел (например, (1, 5, 10, 15)): ")
threshold_str = input("Введите пороговое значение (например, 5): ")

try:
    # Преобразование строки в кортеж
    input_tuple = eval(input_str)  # Используем eval для преобразования строки в кортеж
    
    # Преобразование порогового значения в число
    threshold = int(threshold_str)
    
    # Проверка, что введённый объект является кортежем
    if not isinstance(input_tuple, tuple):
        raise ValueError("Введённые данные не являются кортежем.")
    
    # Фильтрация элементов кортежа
    filtered_tuple = tuple(x for x in input_tuple if x > threshold)
    
    # Вывод результата
    print(filtered_tuple)
except Exception as e:
    print(f"Ошибка: {e}. Убедитесь, что вы ввели кортеж и пороговое значение в правильном формате.")