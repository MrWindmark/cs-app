from datetime import datetime
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('./files/orders.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

    order = (item, quantity, price, buyer, date.isoformat())
    data['orders'].append(json.dumps(order, indent=4))
    print(data)

    with open('./files/orders.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file)


if __name__ == '__main__':
    write_order_to_json('Fish', 1, 230, 'Client_1', datetime.now())
    write_order_to_json('Salad', 1, 180, 'Client_2', datetime.now())
    write_order_to_json('Cake', 1, 280, 'Client_3', datetime.now())
