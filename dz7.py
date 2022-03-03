from encodings import utf_8
import os


import os
with open(r'Дз 7/recepies.txt', 'r', encoding='utf_8') as file:
    cook_book = {}
    for string in file:
        dish_name = string.strip()
        quantity = int(file.readline().strip())
        dish =[]
        for i in range(quantity):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            dish.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish_name] = dish
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredients = dict([(ingredient['ingredient_name'], {'quantity': int(ingredient['quantity']) * person_count,'measure': ingredient['measure']})])
            if shop_list.get(ingredient['ingredient_name']) == 'None':
                ing_list = (int(shop_list[ingredient['ingredient_name']]['quantity']) +
                           int(shop_list[ingredient['ingredient_name']]['quantity']))
                shop_list[ingredient['ingredient_name']]['quantity'] = ing_list
            else:
                shop_list.update(ingredients)
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 3))