import yaml

data = {
    'drinks': ['tea', 'coffee', 'juice'],
    'total price': 340,
    'total convert': {
        '¥': 29.67,
        '£': 3.28
    }
}

if __name__ == '__main__':
    with open('./files/file.yaml', 'w', encoding='UTF-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

    with open('./files/file.yaml', encoding='UTF-8') as f:
        print(f.read())
