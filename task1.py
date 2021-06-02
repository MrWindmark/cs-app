import os
import re
import csv


def info_search(data: list, pattern: str):
    regex = re.compile(f'^{pattern}')
    for line in data:
        if regex.search(line):
            return line.replace(f'{pattern}:', '').strip()


def get_data():
    path = './files'
    titles = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    files_list = os.listdir(path=path)
    files_to_read = []

    for file_name in files_list:
        if file_name.startswith('info_'):
            files_to_read.append(file_name)

    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []

    if len(files_to_read) > 0:
        for file in files_to_read:
            with open(f'{path}/{file}', encoding='windows-1251') as cf:
                temp_data = cf.readlines()
            os_prod_list.append(info_search(temp_data, titles[0]))
            os_name_list.append(info_search(temp_data, titles[1]))
            os_code_list.append(info_search(temp_data, titles[2]))
            os_type_list.append(info_search(temp_data, titles[3]))
    else:
        print('No files to read')

    return [
        titles,
        os_prod_list,
        os_name_list,
        os_code_list,
        os_type_list,
    ]


def write_to_csv(path):
    data = get_data()
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(data.pop(0))

        # кастылик для поворота строки в столбец
        for step in range(len(data[0])):
            line_to_write = []
            for line in data:
                line_to_write.append(line.pop(0))
            writer.writerow(line_to_write)


if __name__ == '__main__':
    write_to_csv('./files/test.csv')
