from pizza import Pizza


def initialize():
    input = open("a_example.txt", "r")
    text = input.read()
    input.close()

    first_split = text.split("\n")
    for i in range(len(first_split)):
        first_split[i] = first_split[i].strip()

    first_split = list(filter(None, first_split))

    for i, y in zip(first_split, range(len(first_split))):
        first_split[y] = first_split[y].split(" ")

    first_row = first_split[0]

    total_pizzas = first_split[0][0]
    teams = {
        "two": first_row[1],
        "three": first_row[2],
        "four": first_row[3]
    }
    print("Teams: ", teams)
    print("Total pizzas: ", total_pizzas)
    first_split.pop(0)
    pizzas = []
    for _pizza, index in zip(first_split, range(len(first_split))):
        _pizza.pop(0)
        ingredients = _pizza
        pizza = Pizza(index, _pizza)
        pizzas.append(pizza)
    for pizza in pizzas:
        print(pizza)
__name__ == 'initialize'
