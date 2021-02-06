class Pizza:
    def __init__(self, Id, ingredients_length, ingredients):
        self.Id = Id
        self.ingredients = ingredients
        self.sent = False
        self.ingredients_lenth = ingredients_length

    def send_pizza(self):
        self.sent = True

    def unsend_pizza(self):
        self.sent = False

    def __str__(self):
        return f"Id: {self.Id}, Ingredients: {self.ingredients}, Ingredients Length: {self.ingredients_lenth}, Sent: {self.sent}"
