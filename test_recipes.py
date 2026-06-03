import pytest
from recipes import Recipe, Ingredient, ShoppingList

def test_ingredient_create():
    ingredient = Ingredient("Водка", 50, "мл")
    assert ingredient.name == "Водка"
    assert ingredient.quantity == 50.0
    assert ingredient.unit == "мл"
def test_ingredient_str():
    ingredient = Ingredient("Водка", 50, "мл")
    assert str(ingredient) == "Водка: 50.0 мл"
def test_eq_same():
    ingredient1 = Ingredient("Водка", 50, "мл")
    ingredient2 = Ingredient("Водка", 100, "мл")
    assert ingredient1 == ingredient2
def test_eq_name():
    ingredient1 = Ingredient("Водка", 50, "мл")
    ingredient2 = Ingredient("Кофейный ликер", 50, "мл")
    assert ingredient1 != ingredient2
def test_eq_unit():
    ingredient1 = Ingredient("Водка", 50, "мл")
    ingredient2 = Ingredient("Водка", 0.05, "л")
    assert ingredient1 != ingredient2
def test_negative_quantity():
    with pytest.raises(ValueError):
        Ingredient("Сливки", -30, "мл")
def test_zero_quantity():
    with pytest.raises(ValueError):
        Ingredient("Сливки", 0, "мл")


def test_create():
    ingredient = Ingredient("водка", 0.5, "л")
    recipe = Recipe("Отвертка", [ingredient])
    assert recipe.title == "Отвертка"
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == "водка"
    assert recipe.ingredients[0].quantity == 0.5
    assert recipe.ingredients[0].unit == "л"
def test_add_ingr():
    recipe = Recipe("Отвертка")
    ingredient = Ingredient("пиво", 1.5, "л")
    recipe.add_ingredient(ingredient)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == "пиво"
def test_add_same_ingr():
    recipe = Recipe("Отвертка")
    first_ingredient = Ingredient("пиво", 0.45, "л")
    second_ingredient = Ingredient("пиво", 0.75, "л")
    recipe.add_ingredient(first_ingredient)
    recipe.add_ingredient(second_ingredient)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 1.2
def test_scale():
    ingredient = Ingredient("водка", 0.25, "л")
    recipe = Recipe("Отвертка", [ingredient])
    new_recipe = recipe.scale(4)
    assert new_recipe.title == "Отвертка"
    assert new_recipe.ingredients[0].quantity == 1
def test_scale_not_change():
    ingredient = Ingredient("водка", 0.25, "л")
    recipe = Recipe("Отвертка", [ingredient])
    new_recipe = recipe.scale(4)
    assert recipe.ingredients[0].quantity == 0.25
    assert new_recipe.ingredients[0].quantity == 1
def test_scale_error():
    recipe = Recipe("Отвертка")
    with pytest.raises(ValueError):
        recipe.scale(0)
def test_recipe_len():
    vodka = Ingredient("водка", 0.7, "л")
    beer = Ingredient("пиво", 2.25, "л")
    recipe = Recipe("Отвертка", [vodka, beer])
    assert len(recipe) == 2


def test_create_list():
    shopping_list = ShoppingList()
    assert shopping_list.ingredients == {}
def test_add_recipe():
    gin = Ingredient("джин", 50, "мл")
    tonic = Ingredient("тоник", 150, "мл")
    recipe = Recipe("Джин-тоник", [gin, tonic])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe)
    assert shopping_list.ingredients["джин"] == 50
    assert shopping_list.ingredients["тоник"] == 150
def test_add_two_recipes():
    gin = Ingredient("джин", 50, "мл")
    tonic = Ingredient("тоник", 150, "мл")
    lime = Ingredient("лайм", 1, "долька")
    recipe1 = Recipe("Джин-тоник", [gin, tonic])
    recipe2 = Recipe("Украшение", [lime])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe1)
    shopping_list.add_recipe(recipe2)
    assert shopping_list.ingredients["джин"] == 50
    assert shopping_list.ingredients["тоник"] == 150
    assert shopping_list.ingredients["лайм"] == 1
def test_add_same_ingr():
    gin1 = Ingredient("джин", 50, "мл")
    gin2 = Ingredient("джин", 75, "мл")
    recipe1 = Recipe("Джин-тоник", [gin1])
    recipe2 = Recipe("Крепкий джин-тоник", [gin2])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe1)
    shopping_list.add_recipe(recipe2)
    assert shopping_list.ingredients["джин"] == 125