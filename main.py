from random import randint

from faker import Faker

fake = Faker()

dict_users_data = {}


# Тут генеруються логіни
def generate_user_name():
    yield f'{fake.user_name() + str(randint(0, 100000))}'


# Тут генеруються паролі
def generate_password():
    yield fake.password(length=randint(5, 25), special_chars=False)


# Тут генерується словник з логінами і паролями
def generate_users_data(count_of_users):
    for _ in range(count_of_users):
        user_name = list(generate_user_name())
        user_password = list(generate_password())
        dict_users_data[user_name[0]] = user_password[0]


# перевірка чи правильна кількість даних згенерувалась
# якщо неправильна, то догенеровуються дані
def validation(count_of_users):
    if len(dict_users_data) == count_of_users:
        # \n count ==> {len(dict_users_data)} - чисто для перевірки точності роботи скрипта
        return f'{dict_users_data}, \n count ==> {len(dict_users_data)}'
    users_count = count_of_users - len(dict_users_data)
    generate_users_data(users_count)
    return validation(count_of_users)


# Вивід результату в  консоль
def consol_result():
    i = int(input('Введіть кількість користувачів ==> '))
    print(validation(i))


if __name__ == '__main__':
    consol_result()
