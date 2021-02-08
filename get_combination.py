from logic.maximize_pizzas import maximize_pizzas
from logic.maximize_teams import maximize_teams
from logic.possible_combinations import get_possible_combinations


def get_combination(total_pizzas, teams):

# Πρεπει να γεμισεις τον πινακα με τα 4 και 3. Μετα πρεπει να αντικαταστησεις τα 4αρια με οσο περισσοτερα δυαρια γινεται. Ενδεχομενως και πολλαπλασια 
# τριων με δυαρια

    t_pizzas = total_pizzas
    team_members = [team.members for team in teams]
    combination = []
    b = True
    i = 0
    while b:
        if t_pizzas - team_members[i] >= 0:
            t_pizzas -= team_members[i]
            combination.append(team_members[i])
            i += 1
        else:
            combination.pop(len(combination)- 1)
            t_pizzas += team_members[i-1]
        if t_pizzas == 0:
            b = False
    return combination
    # possible_combinations = list(set(get_possible_combinations(
    #     total_pizzas, [team.members for team in teams])))

    # print(possible_combinations)

    # print()
    # maximized_pizza_combinations = maximize_pizzas(possible_combinations)

    # maximized_teams_combinations = maximize_teams(maximized_pizza_combinations)

    # print(maximized_teams_combinations)

    # return maximized_teams_combinations
