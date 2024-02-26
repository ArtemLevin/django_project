import math
from random import choice
import json
# with open('dishes.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     dish_dict = {}
#     for line in lines:
#         dishes = line[line.find('.')+1:].strip().split(" - ")
#         dish_dict[dishes[0]] = dishes[1][:-1].capitalize()
#     dish_list = list(dish_dict.items())
#     print(choice(dish_list)[1])

# with open('my_dish.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     print(lines)

# with open('recipes.txt', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     for dish in data:
#         print(dish)


def eq(x):
    return 9*math.log((x**2-3*x-4), 12)-10-math.log(((x+1)**9)/(x-4), 12)
print(eq(4))