import itertools


def get_possible_combinations(total_pizzas, numbers):
    result = [seq for i in range(len(numbers), 0, -1)
              for seq in itertools.combinations(numbers, i) if sum(seq) <= total_pizzas]
    return result
