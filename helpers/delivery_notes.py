class Delivery_Notes:
    def __init__(self):
        self.total_deliveries = 0
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)
        self.total_deliveries += 1
