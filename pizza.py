class Pizza:
    def __init__(self, Id, ingredients):
        self.Id = Id
        self.ingredients = ingredients
        self.sent = False
        self.ingredients_lenth = len(self.ingredients)

    def __str__(self):
        return f"Id: {self.Id}, Ingredients: {self.ingredients}, Sent: {self.sent}"
