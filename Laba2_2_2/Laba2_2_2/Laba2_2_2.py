print("Вводите отрицательные числа. Для завершения введите положительное число.")

count = 0     # Счётчик количества чисел
total = 0     # Сумма чисел

while True:
    num = int(input("Введите число: "))
    
    if num >= 0:
        break  # Завершаем, если положительное число
    total += num
    count += 1

# Проверка деления на ноль
if count == 0:
    print("Вы не ввели ни одного отрицательного числа.")
else:
    average = total / count
    print(f"Среднее арифметическое отрицательных чисел: {average}")

