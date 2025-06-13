import pickle
import os  # Для проверки наличия файла

# 📌 Имя файла
FILENAME = "data.pickle"

# 📌 Функция загрузки словаря из файла, если он существует
def load_phones_from_file(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            print(f"Загружаем словарь из файла: {filename}")
            return pickle.load(f)
    else:
        print(f"Файл {filename} не найден. Используем исходный словарь.")
        return None

# 📌 Исходный словарь (если файла нет)
default_phones = {
    "iPhone 15": {
        "USA": 999, "UK": 1099, "Germany": 1050, "France": 1060,
        "Japan": 980, "India": 1200, "China": 990, "Canada": 1020
    },
    "Samsung Galaxy S23": {
        "USA": 950, "UK": 980, "Germany": 970, "France": 960,
        "Japan": 920, "India": 1100, "China": 940, "Canada": 960
    },
    "Google Pixel 8": {
        "USA": 800, "UK": 820, "Germany": 830, "France": 815,
        "Japan": 790, "India": 950, "China": 805, "Canada": 810
    },
    "Xiaomi 13": {
        "USA": 750, "UK": 780, "Germany": 760, "France": 770,
        "Japan": 730, "India": 880, "China": 740, "Canada": 760
    },
    "OnePlus 11": {
        "USA": 720, "UK": 750, "Germany": 730, "France": 740,
        "Japan": 710, "India": 850, "China": 720, "Canada": 730
    },
    "Huawei P60": {
        "USA": 680, "UK": 710, "Germany": 700, "France": 690,
        "Japan": 660, "India": 800, "China": 680, "Canada": 700
    },
    "Sony Xperia 5": {
        "USA": 790, "UK": 820, "Germany": 810, "France": 800,
        "Japan": 770, "India": 900, "China": 780, "Canada": 800
    }
}

# 📌 Загружаем из файла или используем начальные данные
phones = load_phones_from_file(FILENAME)
if phones is None:
    phones = default_phones.copy()

# 1. Средняя стоимость
print("\nСписок телефонов и их средняя стоимость:")
avg_prices = {}
for model, prices in phones.items():
    avg = sum(prices.values()) / len(prices)
    avg_prices[model] = avg
    print(f"{model}: {avg:.2f}")

# 2. Удаление с минимальной средней ценой
min_model = min(avg_prices, key=avg_prices.get)
print(f"\nУдаляем модель с минимальной средней ценой: {min_model}")
del phones[min_model]

# 3. Модели, у которых средняя цена >= 70% от максимальной
print("\nТелефоны с ценой менее чем на 30% ниже максимальной средней:")
max_avg = max(avg_prices.values())
threshold = max_avg * 0.7
for model, avg in avg_prices.items():
    if avg >= threshold:
        print(f"{model}: {avg:.2f}")

# 4. Цена в США выше, чем в UK
print("\nТелефоны, где цена в США > UK:")
for model, prices in phones.items():
    if prices["USA"] > prices["UK"]:
        print(model)

# 5. Сохраняем обновлённый словарь в файл
with open(FILENAME, "wb") as f:
    pickle.dump(phones, f)
print(f"\nОбновлённый словарь сохранён в файл {FILENAME}")
