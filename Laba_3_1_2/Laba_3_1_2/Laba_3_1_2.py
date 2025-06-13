import os
import glob
import subprocess
import platform

def open_file(filename):
    if not os.path.isfile(filename):
        print("Файл не найден.")
        return
    try:
        if platform.system() == "Windows":
            os.startfile(filename)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", filename])
        else:  # Linux
            subprocess.run(["xdg-open", filename])
        print(f"Файл '{filename}' открыт в редакторе.")
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")

def show_file_content(filename):
    if not os.path.isfile(filename):
        print("Файл не найден.")
        return
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f"\nСодержимое файла '{filename}':\n")
            print(f.read())
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def find_files(pattern):
    print(f"\nРезультаты поиска по шаблону '{pattern}':")
    matches = glob.glob(f"**/*{pattern}*", recursive=True)
    if matches:
        for path in matches:
            print(os.path.abspath(path))
    else:
        print("Файлы не найдены.")

def list_directory_contents(path):
    if not os.path.isdir(path):
        print("Директория не найдена.")
        return
    print(f"\nСодержимое директории '{path}':")
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        print("[DIR]" if os.path.isdir(full_path) else "     ", item)

def show_menu():
    print("\n===== Консольный файловый менеджер =====")
    print("1 – Открыть файл")
    print("2 – Показать содержимое файла")
    print("3 – Найти файл/файлы")
    print("4 – Раскрыть директорию")
    print("0 – Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            filename = input("Введите имя файла для открытия: ")
            open_file(filename)

        elif choice == "2":
            filename = input("Введите имя файла для отображения содержимого: ")
            show_file_content(filename)

        elif choice == "3":
            pattern = input("Введите полное имя или часть имени файла для поиска: ")
            find_files(pattern)

        elif choice == "4":
            path = input("Введите путь к директории: ")
            list_directory_contents(path)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
