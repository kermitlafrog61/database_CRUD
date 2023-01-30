from funcs.crud import create, read_database, update, delete

database = {}

# create(database, 'Samsung Galaxy S10', 50000)
# create(database, 'iPhone 14', 140000)

# print(read_database(database))
# print(read_database(database, 'iPhone 14'))

# update(database, 'iPhone 14', 100000)
# print(read_database(database, 'iPhone 14'))

# delete(database, 'Samsung Galaxy S10')
# print(read_database(database))

# print(read_database(database, 'motorola'))


# TODO: написать тесты на update и delete
# TODO: написать интерфейс для управления функции

while True:
    action = input(
        """ 
что вы хотите сделать?
    create
    read
    update
    delete
Для выхода нажмите Enter
        """
    )
    try:
        if action == 'create':
            create(database, input('Введите название: '), int(input('Введите цену: ')))
        elif action == 'read':
            title = input('Введите название, иначе Enter: ')
            if title == '':
                print('Ваша база данных', read_database(database))
            else:
                print(f'Цена {title} равна: {read_database(database, title)}')
        elif action == 'update':
            update(database, input('Введите название товара: '), int(input('Введите новую цену: ')))
        elif action == 'delete':
            delete(database, input('Введите название товара: '))
            print('Товар успешно удален')
        elif action == '':
            break
        else:
            print('Нет такого действия!')
    except ValueError as msg:
        if str(msg) == 'Такого товара нет':
            print(msg)
        elif 'invalid literal for int() with base 10' in str(msg):
            print('Некорректный ввод цены')
        else:
            raise ValueError(msg)