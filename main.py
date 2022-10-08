from random import randint

from faker import Faker

fake = Faker()


# Тут генеруються логіни
def generate_user_name(self):
    return f'{fake.user_name() + str(randint(0, self))}'


# Тут генеруються паролі
def generate_password():
    return fake.password(length=randint(5, 25), special_chars=False)


# Тут генерується словник з логінами і паролями
def generate_users_data(count_of_users):
    # каунт для виводу прогресу в консоль
    count_generation = 1
    # Словник з даними користувачів
    dict_users_data = {}
    while len(dict_users_data) < count_of_users:
        user_name = generate_user_name(count_of_users)
        user_password = generate_password()
        if user_name in dict_users_data:
            continue
        print(f'Generation ==>  {count_generation}')
        count_generation += 1
        dict_users_data[user_name] = user_password
    return dict_users_data


# Та сама валідація))))
def validation(count_of_users):
    if len(generate_users_data(count_of_users)) == count_of_users:
        print('Scripts work is OK')
    else:
        print('Script work with error')


# Вивід результату в консоль
def console_result():
    i = int(input('Введіть кількість користувачів ==> '))
    validation(i)


if __name__ == '__main__':
    console_result()
