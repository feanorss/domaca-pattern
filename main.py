class Cooking:
    def __init__(self):
        self.field = []

    def add(self, field):
        self.field.append(field)

class Builder:
    def __init__(self):
        self.cooking = Cooking()

    def add_pasta(self, pasta_type):
        self.cooking.add(f"Pasta: {pasta_type}")
        return self

    def add_sauce(self, sauce_type):
        self.cooking.add(f"Sauce: {sauce_type}")
        return self

    def add_topping(self, topping_type):
        self.cooking.add(f"Topping: {topping_type}")
        return self

    def add_dressing(self, dressing_type):
        self.cooking.add(f"Dressing: {dressing_type}")
        return self

    def build(self):
        return self.cooking



builder1 = Builder()
recipe1 = builder1.add_pasta("Spaghetti").add_sauce("Tomato").add_topping("Parmesan").add_dressing("None").build().field
print("Recept 1:", recipe1)

builder2 = Builder()
recipe2 = builder2.add_pasta("Penne").add_topping("Olive").add_dressing("Vinegar").build().field
print("Recept 2:", recipe2)

builder3 = Builder()
recipe3 = builder3.add_pasta("Bucatini").add_sauce("Olive Oil").add_topping("Parmesan").build().field
print("Recept 3:", recipe3)

