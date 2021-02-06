from helpers.initialize import initialize
from logic.maximize_teams import maximize_teams
from logic.maximize_pizzas import maximize_pizzas
from logic.possible_combinations import get_possible_combinations
teams, pizzas, total_pizzas = initialize()
possible_combinations = list(set(get_possible_combinations(
    total_pizzas, [team.members for team in teams])))

print(possible_combinations)

print()

maximized_pizza_combinations = maximize_pizzas(possible_combinations)

print(maximized_pizza_combinations)

maximized_teams_combinations = maximize_teams(maximized_pizza_combinations)

print(maximized_teams_combinations)
