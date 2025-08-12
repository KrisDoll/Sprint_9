import allure
import pytest
import os
from pages.recipes_page import RecipesPage
from pages.auth_page import Authorization
from conftest import driver, register_user
from helpers.generator import Generator


@allure.feature('Создание рецепта')
class TestCreateRecipe:

    @allure.story('Успешное создание рецепта')
    @allure.title('Число ингредиентов: {ingredients_number}')
    @pytest.mark.parametrize('ingredients_number', [2, 5])
    def test_create_recipe(self, driver, register_user, ingredients_number):
        page = Authorization(driver)
        page.login_to_account(register_user)
        recipe_data = Generator.generate_recipe_data()
        recipe_data['ingredients_number'] = ingredients_number
        relative_path = "tests/test_data/test_picture.png"
        absolute_path = os.path.abspath(relative_path)
        page = RecipesPage(driver)
        page.click_on_create_recipe_tab()
        page.upload_picture_to_recipe(absolute_path)
        page.create_recipe(recipe_data)
        assert page.get_recipe_title() == recipe_data['recipe_name']