class Cooking:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.dressing = None

    def add_pasta(self, pasta_type):
        self.type = pasta_type

    def add_sauce(self, sauce_type):
        self.sauce = sauce_type

    def add_topping(self, topping_type):
        self.topping = topping_type

    def add_dressing(self, dressing_type):
        self.dressing = dressing_type

class Builder:
    def __init__(self):
        self.cooking = Cooking()

    def add_pasta(self, pasta_type):
        self.cooking.add_pasta(pasta_type)
        return self

    def add_sauce(self, sauce_type):
        self.cooking.add_sauce(sauce_type)
        return self

    def add_topping(self, topping_type):
        self.cooking.add_topping(topping_type)
        return self

    def add_dressing(self, dressing_type):
        self.cooking.add_dressing(dressing_type)
        return self

    def build(self):
        return self.cooking


builder1 = Builder()
recipe1 = builder1.add_pasta("Spaghetti").add_sauce("Tomato").add_topping("Parmesan").build()
print("Recept 1:", recipe1.type, recipe1.sauce, recipe1.topping, recipe1.dressing)

builder2 = Builder()
recipe2 = builder2.add_pasta("Penne").add_topping("Olive").add_dressing("Vinegar").build()
print("Recept 2:", recipe2.type, recipe2.sauce, recipe2.topping, recipe2.dressing)

builder3 = Builder()
recipe3 = builder3.add_pasta("Bucatini").add_sauce("Olive Oil").add_topping("Parmesan").build()
print("Recept 3:", recipe3.type, recipe3.sauce, recipe3.topping, recipe3.dressing)

