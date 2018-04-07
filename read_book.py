"""
Создана функция read_cook_book():
-читаем файл, обходим в одном шаге цикле for наше блюдю (название, количесвто ингридиентов, строки с ингридиентами
-первую строку в название блюда, откидываем символ завер. строки и приводим к нижнему регистру
-вторую строку считываем как число и использоем это число для обхода списка ингрид. отнимая в каждом шаге цикла -1,
-считываем строки в список (ingridient_set) пока ingridient_count не будет = 0, разд. через сплит и приводя к ниж.рег.
-из списка ingridient_set делаем словарь с ингридиентами (ingridient_dict) и далее добавляем в список (ingridient_list)
-в конце шага for формируем словарь где ключ - уник. название блюда, знач. - список ингридиент. (ingridient_list)
-вызов функции вернет словарь cook_book

Вызываем функ. read_cook_book() в get_shop_list_by_dishes() и используем наш словарь далее в программе.

Ну и раз тема про файлы, доработали функцию print_shop_list(shop_list):
добавили вывод в файл (shop_list.txt) через контекстный менеджер и именованый аргумент file функции print
сделал "append" т.к. вывод в файл в цикле
"""


def read_cook_book():
    cook_book = dict()

    with open("cook_book.txt") as f:

        for line in f:

            dish_name = line.lower().rstrip()
            ingridient_count = int(f.readline())
            ingridient_list = list()

            while ingridient_count != 0:
                name, quantity, measure = f.readline().lower().split(' | ')
                measure = measure.rstrip()

                ingridient_dict = {'ingridient_name': name,
                                   'quantity': int(quantity),
                                   'measure': measure}

                ingridient_list.append(ingridient_dict)
                ingridient_count -= 1

            cook_book[dish_name] = ingridient_list
            f.readline()  # Пропускаем пустую строку для переходу к сл. блюду

    return cook_book

# cook_book = {
#     'яйчница': [
#         {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#     'стейк': [
#         {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#     'салат': [
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
# }


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book()
    shop_list = {}

    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    with open("shop_list.txt", 'a') as f:

        for shop_list_item in shop_list.values():
            print('{} {} {}'.format(shop_list_item[
                                        'ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

            print('{} {} {}'.format
                  (shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']), file=f)


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


def main():
    create_shop_list()


main()