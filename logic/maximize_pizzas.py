from entities.team import Team
from entities.pizza import Pizza
from helpers.filter import get_teams
import itertools


def maximize_pizzas(combinations):
    mapped_combinations = [sum(combination) for combination in combinations]
    max_pizzas = max(mapped_combinations)
    return list(filter(lambda combination: sum(combination) == max_pizzas, combinations))
