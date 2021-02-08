def create_similarity_levels(pizzas):
    pizza_sls = {}
    for pizza, i in zip(pizzas, range(len(pizzas))):
        temp_colection = pizzas.copy()
        temp_colection.pop(i)
        similarity_level = 0
        for p in temp_colection:
            for ingredient in pizza.ingredients:
                if ingredient in p.ingredients:
                    similarity_level += 1
        pizza_sls[pizza.Id] = similarity_level

    sorted_dict = {}
    sorted_keys = sorted(pizza_sls, key=pizza_sls.get,reverse=True)
    for w in sorted_keys:
        sorted_dict[w] = pizza_sls[w]
    return sorted_dict
