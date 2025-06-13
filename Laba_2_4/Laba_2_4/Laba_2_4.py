# Ввод количества элементов
N = int(input("Введите количество элементов в массиве: "))

# Ввод элементов массива
array = []
for i in range(N):
    num = int(input(f"Введите элемент {i + 1}: "))
    array.append(num)

# Поиск минимального элемента и его индекса
min_value = min(array)
min_index = array.index(min_value)

# Вывод результатов
print(f"Минимальный элемент: {min_value}")
print(f"Индекс минимального элемента: {min_index}")

