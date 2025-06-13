
import requests
from bs4 import BeautifulSoup
import csv

# Список URL-адресов для каждой дисциплины, пола и года
urls = [
    ("https://worldathletics.org/records/toplists/800m/outdoor/women/2024", "800m", "женщины", 2024),
    ("https://worldathletics.org/records/toplists/1500m/outdoor/women/2024", "1500m", "женщины", 2024),
    ("https://worldathletics.org/records/toplists/5000m/outdoor/women/2024", "5000m", "женщины", 2024),
    ("https://worldathletics.org/records/toplists/10000m/outdoor/women/2024", "10000m", "женщины", 2024),
    ("https://worldathletics.org/records/toplists/800m/outdoor/men/2024", "800m", "мужчины", 2024),
    ("https://worldathletics.org/records/toplists/1500m/outdoor/men/2024", "1500m", "мужчины", 2024),
    ("https://worldathletics.org/records/toplists/5000m/outdoor/men/2024", "5000m", "мужчины", 2024),
    ("https://worldathletics.org/records/toplists/10000m/outdoor/men/2024", "10000m", "мужчины", 2024)
]

# Функция для извлечения данных с одной страницы
def extract_record_data(url, distance, gender, year):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr", class_="record")
    records = []
    for row in rows:
        try:
            name = row.find("td", class_="name").get_text(strip=True)
            country = row.find("td", class_="country").get_text(strip=True)
            time = row.find("td", class_="mark").get_text(strip=True)
            date = row.find("td", class_="date").get_text(strip=True)
            records.append([year, name, country, time, date, distance, gender])
        except AttributeError:
            continue
    return records

# Собираем данные для всех дисциплин
all_records = []
for url, distance, gender, year in urls:
    all_records.extend(extract_record_data(url, distance, gender, year))

# Сохраняем данные в CSV
with open("top_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Год", "Имя", "Страна", "Время", "Дата", "Дистанция", "Пол"])
    writer.writerows(all_records)

print("Данные успешно сохранены в top_results.csv")
