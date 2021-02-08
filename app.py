from helpers.initialize import initialize

from logic.similarity_levels import create_similarity_levels
from helpers.delivery_notes import Delivery_Notes
from entities.team import Team
from get_combinations import get_combinations
teams, pizzas, total_pizzas = initialize()

combinations = get_combinations(total_pizzas, teams)

pizzas_sl = create_similarity_levels(pizzas)

print(pizzas_sl)

delivery_notes = Delivery_Notes()

# right now takes only first combination
first_combination = combinations[0]
#

for noOfMembers in first_combination:
    delivery_notes.add_team(Team(noOfMembers))
for pizza_id in pizzas_sl.keys():
    pizza = [pizza for pizza in pizzas if pizza.Id == pizza_id][0]
    delivery_notes.add_pizza(pizza)
print(delivery_notes.total_score())
file = open("res.txt", "w")
file.write(f"{delivery_notes.total_deliveries}\n")
for team in delivery_notes.teams:
    file.write(f"{team.members} ")
    for pizza in team.pizzas:
        file.write(f"{pizza.Id} ")
    file.write("\n")
