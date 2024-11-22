import csv
import json

def csv_to_json(input_file, output_file):
    # Инициализируем структуру для JSON
    result = []

    current_region = None  # Переменная для текущего региона

    print("Начало обработки CSV файла...")
    # Открываем CSV-файл для чтения
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')  # Указание разделителя ";"

        for index, row in enumerate(reader):
            # Логируем содержимое строки для отладки
            print(f"Строка {index + 1}: {row}")

            if not row or len(row) < 6:  # Пропускаем строки с недостаточным количеством колонок
                print(f"Пропущена строка: {row}")
                continue

            # Название региона или района находится во второй колонке (индекс 1)
            name = row[1].strip()
            # Маркер региона "+" находится в 6-й колонке (индекс 5)
            marker = row[5].strip()

            if marker == '+':  # Если маркер "+" найден, это регион
                print(f"Найден регион: {name}")
                current_region = {
                    "region": name,
                    "districts": []
                }
                result.append(current_region)
                print(f"Добавлен регион: {current_region}")
            elif current_region and name:  # Если текущий регион существует, добавляем район
                print(f"Добавлен район '{name}' в регион '{current_region['region']}'")
                current_region["districts"].append(name)

    print("Обработка завершена.")
    print(f"Итоговая структура: {json.dumps(result, ensure_ascii=False, indent=4)}")

    # Сохраняем результат в JSON-файл
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    print(f"Данные успешно преобразованы и сохранены в {output_file}")

# Использование скрипта
input_file = "tumanlar.csv"  # Замените на имя вашего CSV-файла
output_file = "tumanlar.json"  # Имя выходного JSON-файла

csv_to_json(input_file, output_file)
