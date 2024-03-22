import csv

file_name = ''
table_output = ''
yes_output = ['1', 'дА', 'да', 'Да']
new_file_name = ''
date_time_for_table = []


def searching(file):
    with open(file, newline='', encoding='utf-8') as betelgeuse:
        data = csv.DictReader(betelgeuse, delimiter=',')
        is_chain = False
        current_luminosity, previous_luminosity = 0, 0
        decreases_number, biggest_decreases_number = 0, 0
        old_biggest_decreases_datetime, current_datetime = '', ''
        previous_chain_decreases_datetime, new_biggest_decreases_datetime = '', '',
        for row in data:
            current_luminosity = int(row['яркость'])
            current_datetime = row['дата'] + ' ' + row['время']
            if current_luminosity <= previous_luminosity:
                if is_chain is False:
                    is_chain = True
                    decreases_number = 2
                    old_biggest_decreases_datetime = previous_chain_decreases_datetime
                else:
                    decreases_number += 1
            else:
                if decreases_number > biggest_decreases_number:
                    biggest_decreases_number = decreases_number
                    new_biggest_decreases_datetime = old_biggest_decreases_datetime
                decreases_number = 0
                is_chain = False
            previous_chain_decreases_datetime = current_datetime
            previous_luminosity = current_luminosity

    if decreases_number > biggest_decreases_number:
        biggest_decreases_number = decreases_number
        new_biggest_decreases_datetime = old_biggest_decreases_datetime

    return new_biggest_decreases_datetime, biggest_decreases_number


if file_name == '':
    print("Запущенное консольное приложение является примером решения задачи 'Бетельгейзе'.\n"
          "В итоге выполнения программы она выведет дату и время начала наибольшей последовательности"
          " убывающих значений яркости, а также число,\n"
          "равное количеству не возрастающих значений яркости в этой последовательности.\n"
          "При желании, будет возможность создать новую таблицу с расширением '.csv' в корне программы,"
          " в которой сохранятся вышеперечисленные данные.")
    print("\nДля начала поиска переместите вашу таблицу с данными в корень выполняемой программы.\n"
          "Таблица должна быть в формате 'CSV' и обязательно содержать"
          " столбцы с названиями: 'дата', 'время' и 'яркость'.")
    file_name = str(input("Введите имя вашей таблицы (например: 'таблица', не указывая кавычки и расширение файла): "))
    file_name += '.csv'
    result = searching(file_name)
    print('\nДанные о найденной наибольшей последовательности убывающих значений яркости:\n'
          f'Дата и время: {result[0]}\n'
          f'Не возрастающих значений: {result[1]}')
    print('\nСохранить найденные значения в отдельной таблице?')
    table_output = str(input("Введите 'да' или нажмите 'Enter', что бы завершить программу: "))
    if table_output in yes_output:
        new_file_name = str(input("\nВведите имя новой таблицы: "))
        new_file_name += '.csv'
        date_time_for_table = result[0].split()
        with (open(new_file_name, 'w', newline='', encoding='utf-8') as new_file):
            writer = csv.writer(new_file)
            writer.writerow(
                (
                    'дата',
                    'время',
                    'длина'
                )
            )
        with open(new_file_name, 'a', encoding='utf-8') as new_file:
            writer = csv.writer(new_file)
            writer.writerow(
                (
                    date_time_for_table[0],
                    date_time_for_table[1],
                    result[1]
                )
            )
