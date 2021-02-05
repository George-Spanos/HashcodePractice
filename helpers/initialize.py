def initialize():
    input = open("a_example", "r")
    text = input.read()
    input.close()

    first_split = text.split("\n")
    for i in range(len(first_split)):
        first_split[i] = first_split[i].strip()

    first_split = list(filter(None, first_split))
    # print(first_split)

    for i, y in zip(first_split, range(len(first_split))):
        first_split[y] = first_split[y].split(" ")
    # print(first_split)

    first_row = first_split[0]

    total_pizzas = first_split[0][0]
    teams = {
        "two": first_row[0],
        "three": first_row[1],
        "four": first_row[2]
    }
    print("Teams: ", teams)
    print("Total pizzas: ", total_pizzas)

__name__ == 'initialize'