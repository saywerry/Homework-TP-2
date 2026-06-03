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
    
class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть больше 0")
        changed_recipe = recipe.scale(portions)
        for ingredient in changed_recipe.ingredients:
            self._items.append((ingredient, recipe.title))
    def remove_recipe(self, title):
        new_items = []
        for item in self._items:
            ingredient = item[0]
            recipe_title = item[1]
            if recipe_title != title:
                new_items.append((ingredient, recipe_title))
        self._items = new_items
    def get_list(self):
        rez = {}
        for item in self._items:
            ingredient = item[0]
            k = (ingredient.name, ingredient.unit)
            if k in rez:
                rez[k] += ingredient.quantity
            else:
                rez[k] = ingredient.quantity
        ingredients = []
        for k in rez:
            name = k[0]
            unit = k[1]
            quantity = rez[k]
            ingredients.append(Ingredient(name, quantity, unit))
        def get_ingredient_name(ingredient):
            return ingredient.name
        ingredients.sort(key=get_ingredient_name)
        return ingredients
    def __add__(self, other):
        new_shopping_list = ShoppingList()
        for item in self._items:
            ingredient = item[0]
            recipe_title = item[1]
            new_shopping_list._items.append((ingredient, recipe_title))
        for item in other._items:
            ingredient = item[0]
            recipe_title = item[1]
            new_shopping_list._items.append((ingredient, recipe_title))
        return new_shopping_list
    
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self, ratio):
        scaled_recipe = super().scale(ratio)
        return DietaryRecipe(
            self.title,
            self.diet_type,
            scaled_recipe.ingredients
        )
    def __str__(self):
    recipe_text = super().__str__()
    return "[" + self.diet_type + "] " + recipe_text