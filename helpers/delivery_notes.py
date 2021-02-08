class Delivery_Notes:
    def __init__(self):
        self.total_deliveries = 0
        self.teams = []
        self.total_score = 0

    def add_team(self, team):
        self.teams.append(team)
        self.total_deliveries += 1

    def add_pizza(self, pizza):
        team_to_add = self.find_team_with_least_pizzas_and_max_members()
        team_to_add.append_pizza(pizza)

    def find_team_with_least_pizzas_and_max_members(self):
        sorted_teams = sorted(self.teams, key=lambda team: len(team.pizzas))
        min_ammount_of_ingredients = len(sorted_teams[0].pizzas)
        least_ingredients_teams = [team for team in sorted_teams if len(
            team.pizzas) == min_ammount_of_ingredients]
        largest_team = sorted(least_ingredients_teams,
                              key=lambda team: team.members, reverse=True)
        return largest_team[0]

    def calc_total_score(self):
        score = 0
        for team in self.teams:
            score += team.get_unique_ingredients_length() ** 2
        self.total_score = score
