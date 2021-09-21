from faker import Faker
import csv
import requests


def requirements() -> str:
    open_file = open("requirements.txt", "r")
    req = ''
    for line in open_file.readlines():
        req += line + '<br>'
    return req


def generate_users(num: int = 100) -> str:
    fake = Faker()
    user = ''
    for _ in range(num):
        name = fake.name().split(' ')[0]
        if name == 'Mr':
            while name != 'Mr':
                name = fake.name().split(' ')[0]
        user += name + ' ' + fake.email() + '\n' + '<br>'
    return user


def open_csv(file='my_csv.csv') -> list:
    with open(file, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        csv_data = []
        for row in file_reader:
            csv_data.append(''.join(row))
    return csv_data


def mean(data: list) -> dict:
    data.pop(0)
    data.pop()
    split_data = []
    for _ in data:
        split_data.append(_.split(' '))
    height = []
    weight = []
    for _ in split_data:
        height.append(float(_[1]) * 2.54)
        weight.append(float(_[2]) * 0.45)
    avg_height = sum(height) / len(height)
    avg_weight = sum(weight) / len(weight)

    w_h = {"avg_height": avg_height,
           "avg_weight": avg_weight}
    return w_h


def space() -> str:
    r = requests.get('http://api.open-notify.org/astros.json')
    numb = r.json().get('number')
    return f'В настоящий момент в мире {numb} космонавнтов.'
