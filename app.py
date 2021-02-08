from helpers.initialize import initialize

from logic.similarity_levels import create_similarity_levels
from helpers.delivery_notes import Delivery_Notes
from entities.team import Team
from get_combination import get_combination

import time


def calc_delivery():
    start = time.time()
    teams, pizzas, total_pizzas = initialize()

    combination = get_combination(total_pizzas, teams)
    print(combination)
    pizzas_sl = create_similarity_levels(pizzas)

    print(pizzas_sl)

    delivery_notes = Delivery_Notes()
    for noOfMembers in combination:
        delivery_notes.add_team(Team(noOfMembers))
    for pizza_id in pizzas_sl.keys():
        pizza = [pizza for pizza in pizzas if pizza.Id == pizza_id][0]
        delivery_notes.add_pizza(pizza)
    delivery_notes.calc_total_score()
    file = open("res.txt", "w")
    file.write(f"{delivery_notes.total_deliveries}\n")
    for team in delivery_notes.teams:
        file.write(f"{team.members} ")
        for pizza in team.pizzas:
            file.write(f"{pizza.Id} ")
        file.write("\n")
    end = time.time()
    print(end - start)
    print(delivery_notes.total_score)


def main():
    calc_delivery()


if __name__ == "__main__":
    main()
