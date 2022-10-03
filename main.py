from random import randint
from faker import Faker

fake = Faker()


def generate_users_data(count_of_users):
    while True:
        dict_users_data = {f'{fake.user_name() + str(randint(0, 100000))}': (
            (fake.password(
                length=randint(5, 25), special_chars=False, digits=True, upper_case=True, lower_case=True))) for _ in range(count_of_users)}
        if len(dict_users_data) == count_of_users:
            return dict_users_data


users_count = int(input('Введіть кількість користувачів ==> '))

print(generate_users_data(users_count))
