def get_positive_integer(prompt):
    while True: #цикл, пока пользователь не введет верное значение
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка: введите положительное целое число.")
        except ValueError:
            print("Ошибка: введите целое число.")

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Основной код
year = get_positive_integer("Введите год (положительное целое число): ")

if is_leap_year(year):
    days = 366
else:
    days = 365

print(f"В году {year} — {days} дней.")
