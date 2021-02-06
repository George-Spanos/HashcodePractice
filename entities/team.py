class Team:
    def __init__(self, members):
        self.members = members
        self.pizzas = []
        self.delivered = False

    def append_pizza(self, pizza):
        if not self.delivered:
            self.pizzas.append(pizza)
            if len(self.pizzas) == self.members:
                self.delivered = True

    def get_unique_ingredients(self):
        all_ingredients = []
        for pizza in self.pizzas:
            all_ingredients += pizza.ingredients
        # print(all_ingredients)
        all_ingredients = list(set(all_ingredients))
        # print(all_ingredients)
        return all_ingredients

    def get_unique_ingredients_length(self):
        return len(self.get_unique_ingredients())

    def __str__(self):
        return f"Team Members: {self.members}"
