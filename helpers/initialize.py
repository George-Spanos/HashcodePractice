from entities.pizza import Pizza
from entities.team import Team


def initialize():
    input = open("b_example.txt", "r")
    text = input.read()
    input.close()

    first_split = text.split("\n")
    for i in range(len(first_split)):
        first_split[i] = first_split[i].strip()

    first_split = list(filter(None, first_split))

    for i, y in zip(first_split, range(len(first_split))):
        first_split[y] = first_split[y].split(" ")

    first_row = first_split[0]

    total_pizzas = int(first_split[0][0])
    first_row.pop(0)
    teams = []
    for i in range(int(first_row[0])):
        teams.append(Team(2))
    for i in range(int(first_row[1])):
        teams.append(Team(3))
    for i in range(int(first_row[2])):
        teams.append(Team(4))

    first_split.pop(0)
    pizzas = []
    for _pizza, index in zip(first_split, range(len(first_split))):
        ingredients_length = _pizza.pop(0)
        ingredients = _pizza
        pizza = Pizza(index, ingredients_length, ingredients)
        pizzas.append(pizza)
    return teams, pizzas, total_pizzas
