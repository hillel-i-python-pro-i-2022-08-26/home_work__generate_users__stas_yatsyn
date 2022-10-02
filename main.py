from random import randint
from faker import Faker

fake = Faker()

count_of_users = int(input('Введіть кількість користувачів ==> '))

while True:
    dict_users_data = {f'{fake.user_name() + str(randint(0, 100000))}': (
        (fake.password(
            length=randint(5, 25), special_chars=False, digits=True, upper_case=True, lower_case=True))) for _ in range(
        count_of_users)}
    if len(dict_users_data) == count_of_users:
        break


print(dict_users_data)
print(len(dict_users_data))
