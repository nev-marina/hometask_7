from encodings import utf_8
import os

def get_cook_book():
    with open(r'Дз 7/recepies.txt', 'r', encoding='utf_8') as file:
        cook_book = {}
        for string in file:
            dish_name = string.strip()
            quantity = int(file.readline().strip())
            dish = []
            for i in range(quantity):
                ingredient_name, quantity, measure = file.readline().strip().split('|')
                dish.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish_name] = dish
            file.readline()
        return cook_book


# print(get_cook_book())


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in get_cook_book()[dish]:
            ingr_name = ingredient['ingredient_name']
            if ingr_name not in shop_list:
                shop_list[ingr_name] = {'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}
            else:
                shop_list[ingr_name]['quantity'] += int(ingredient['quantity']) * person_count
    return shop_list


print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))
