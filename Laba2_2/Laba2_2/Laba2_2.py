# Ввод чисел A и B
A = int(input("Введите число A: "))
B = int(input("Введите число B (B > A): "))

# Проверка, что A < B
if A >= B:
    print("Ошибка: A должно быть меньше B.")
else:
    total = 0
    for i in range(A, B + 1):  # range от A до B включительно
        total += i
    print(f"Сумма целых чисел от {A} до {B} равна {total}")


