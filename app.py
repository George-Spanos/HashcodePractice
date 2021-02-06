from helpers.initialize import initialize
from logic.maximize_teams import maximize_teams
from logic.maximize_pizzas import maximize_pizzas
from logic.possible_combinations import get_possible_combinations
from logic.add_pizzas import create_similarity_levels
from helpers.delivery_notes import Delivery_Notes
from entities.team import Team
teams, pizzas, total_pizzas = initialize()
possible_combinations = list(set(get_possible_combinations(
    total_pizzas, [team.members for team in teams])))

print(possible_combinations)

print()

maximized_pizza_combinations = maximize_pizzas(possible_combinations)

# print(maximized_pizza_combinations)

maximized_teams_combinations = maximize_teams(maximized_pizza_combinations)

print(maximized_teams_combinations)

pizzas_sl = create_similarity_levels(pizzas)

print(pizzas_sl)

delivery_notes = Delivery_Notes()

# right now takes only first combination
notes = maximized_teams_combinations[0]
for note in notes:
    delivery_notes.add_team(Team(note))
