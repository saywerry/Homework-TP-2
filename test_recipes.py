import pytest
from recipes import Ingredient
def test_ingredient_create():
    ingredient = Ingredient("Мука", 500, "г")
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"
def test_ingredient_str():
    ingredient = Ingredient("Мука", 500, "г")
    assert str(ingredient) == "Мука: 500.0 г"
def test_eq_same():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Мука", 100, "г")
    assert ingredient1 == ingredient2
def test_eq_name():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Сахар", 500, "г")
    assert ingredient1 != ingredient2
def test_eq_unit():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Мука", 500, "кг")
    assert ingredient1 != ingredient2
"Запускаю дополнительные тесты, чтобы не допустить ошибки в классе при проверке quantuty<=0"    
def test_negative_quantity():
    with pytest.raises(ValueError):
        Ingredient("Мука", -500, "г")
def test_zero_quantity():
    with pytest.raises(ValueError):
        Ingredient("Мука", 0, "г")