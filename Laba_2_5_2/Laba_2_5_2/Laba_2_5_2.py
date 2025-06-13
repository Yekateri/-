# Рекурсивная функция (функция, вызывающая себя для решения) для нахождения минимума в массиве
def find_min_recursive(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n - 1], find_min_recursive(arr, n - 1))

# Ввод массива
N = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(N):
    array.append(int(input(f"Введите элемент {i + 1}: ")))

# Нахождение и вывод минимума
minimum = find_min_recursive(array, len(array))
print(f"Минимальный элемент в массиве: {minimum}")

