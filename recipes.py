class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value
    def __str__(self):
        return self.name + ": " + str(self.quantity) + " " + self.unit
    def __repr__(self):
        return "Ingredient('" + self.name + "', " + str(self.quantity) + ", '" + self.unit + "')"
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit
    
class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        self.ingredients = []
        if ingredients is not None:
            for ingredient in ingredients:
                self.add_ingredient(ingredient)
    def add_ingredient(self, ingredient):
        for current in self.ingredients:
            if current == ingredient:
                current.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) == int or type(ratio) == float:
            return ratio > 0
        return False
    def scale(self, ratio):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент не может быть отрицательным или равным нулю")
        n_ingredients = []
        for ingredient in self.ingredients:
            new_ingredient = Ingredient(
                ingredient.name,
                ingredient.quantity * ratio,
                ingredient.unit
            )
            n_ingredients.append(new_ingredient)
        return Recipe(self.title, n_ingredients)
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        result = self.title + "\n"
        for ingredient in self.ingredients:
            result = result + str(ingredient) + "\n"
        return result