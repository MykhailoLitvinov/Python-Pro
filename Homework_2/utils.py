from faker import Faker

def requirements():
    open_file = open("requirements.txt", "r")
    req = ''
    for line in open_file.readlines():
        req += line
    return req


def generate_users(num=10):
    fake = Faker()
    e_mail = ''
    for _ in range(num):
        e_mail += fake.name().split(' ')[0] + ' ' + fake.ascii_free_email() + '\n'
    return e_mail


print(generate_users(5))


