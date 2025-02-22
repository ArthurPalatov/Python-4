# Ввод данных в формате списка кортежей
input_str = input("Введите список кортежей: ")

try:
    # Преобразование строки в список кортежей
    input_tuples = eval(input_str)  # Используем eval для преобразования строки в объект
    
    # Проверка, что введённый объект является списком кортежей
    if not isinstance(input_tuples, list) or not all(isinstance(item, tuple) for item in input_tuples):
        raise ValueError("Введённые данные не являются списком кортежей.")
    
    # Нахождение кортежа с максимальной суммой элементов
    max_tuple_by_sum = max(input_tuples, key=sum)
    
    # Нахождение кортежа с максимальной длиной
    max_tuple_by_len = max(input_tuples, key=len)
    
    # Вывод результатов
    print(f"Кортеж с максимальной суммой: {max_tuple_by_sum}")
    print(f"Кортеж с максимальной длиной: {max_tuple_by_len}")
except Exception as e:
    print(f"Ошибка: {e}. Убедитесь, что вы ввели список кортежей в правильном формате.")