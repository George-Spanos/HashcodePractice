from entities.team import Team


def maximize_teams(combinations):
    mapped_combinations = [len(combination) for combination in combinations]
    max_pizzas = max(mapped_combinations)
    return list(filter(lambda combination: len(combination) == max_pizzas, combinations))
