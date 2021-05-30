import subprocess

if __name__ == '__main__':
    first_str = ['разработка', 'сокет', 'декоратор']
    second_str = ['class', 'function', 'method']
    third = ['attribute', 'класс', 'функция', 'type']
    str_4 = ['разработка', 'администрирование', 'protocol', 'standard']

    for item in first_str:
        print(f'{item} - {type(item)}')

    for item in second_str:
        item_utf_b = bytes(item, "UTF-8")
        print(f'{item} - type: {type(item)} | {item_utf_b} - type: {type(item_utf_b)} -> len: {len(item_utf_b)}')

    for item in third:
        print(f'{item} in bytes {bytes(item, "UTF-8")}')

    for item in str_4:
        item_encode = item.encode('UTF-8')
        item_decode = item_encode.decode('UTF-8')
        print(f'Encoded: {item_encode} - {type(item_encode)} | Decoded: {item_decode} - {type(item_decode)}')


    def print_ping(params):
        subproc_ping = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='UTF-8')
        for data_line in subproc_ping.stdout:
            print(data_line)


    ping1 = ['ping', '-c4', 'yandex.ru']
    ping2 = ['ping', '-c4', 'youtube.com']

    print_ping(ping1)
    print_ping(ping2)

    file_lines = ['сетевое программирование', 'сокет', 'декоратор']

    with open('test_file.txt', 'w') as file:
        for line in file_lines:
            file.write(line + '\n')