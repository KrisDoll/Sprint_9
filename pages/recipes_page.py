from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from helpers.URLs import URLs
from helpers.generator import Generator
from helpers.locators import Locators
from helpers.URLs import URLs

class RecipesPage(BasePage):


    @allure.step("Переход на страницу «Создать рецепт»")
    def get_recipes_page(self):
        self.get_page(URLs.RECIPES_PAGE)

    @allure.step("Клик по вкладке «Создать рецепт»")
    def click_on_create_recipe_tab(self):
        self.wait_for_element(Locators.CREATE_RECIPE_TAB)
        self.click_on(Locators.CREATE_RECIPE_TAB)
        self.wait_for_element_to_be_visible(Locators.CREATE_RECIPE_BUTTON)

    @allure.step("Ввод текста в поле «Название рецепта»")
    def fill_recipe_name_field(self, text):
        self.send_keys(Locators.RECIPE_NAME_INPUT, text)

    @allure.step("Ввод текста в поле «Ингредиенты»")
    def fill_ingredients_field(self, text):
        self.send_keys(Locators.INGREDIENTS_INPUT, text)

    @allure.step("Выбор случайного ингредиента из списка")
    def click_on_random_ingredient_from_popup_list(self):
        self.wait_for_element_to_be_visible(Locators.INGREDIENTS_POPUP_LIST)
        ingredients_list = self.find_elements(Locators.INGREDIENTS_POPUP_LIST)
        ingredient_index = Generator.get_number(0, len(ingredients_list) - 1)
        self.scroll_to_element(ingredients_list[ingredient_index])

        with allure.step('Данные теста'):
            allure.attach(str(ingredients_list[ingredient_index].text), name='ingredient_name')

        ingredients_list[ingredient_index].click()

    @allure.step("Ввод количества ингредиента")
    def fill_ingredient_amount_value(self, text):
        self.send_keys(Locators.INGREDIENTS_AMOUNT_VALUE, text)

    @allure.step("Клик по кнопке «Добавить ингредиент»")
    def click_on_add_ingredient_button(self):
        self.click_on(Locators.ADD_INGREDIENT_BUTTON)

    @allure.step("Добавление случайного ингредиента")
    def add_random_ingredient(self):
        # выбор ингредиента по первой букве
        start_letter = Generator.get_russian_letter(self)
        self.fill_ingredients_field(start_letter)
        self.click_on_random_ingredient_from_popup_list()
        # ввод массы ингредиента
        amount_value = str(Generator.get_number(1, 999))
        self.fill_ingredient_amount_value(amount_value)
        # добавить ингредиент
        self.click_on_add_ingredient_button()

    @allure.step("Указание времени приготовления")
    def set_cooking_time(self, text):
        self.send_keys(Locators.COOKING_TIME_INPUT, text)

    @allure.step("Загрузка тестовой картинки рецепта")
    def upload_picture_to_recipe(self, picture_link):
        self.make_element_to_be_visible(Locators.IMAGE_UPLOAD_INPUT)
        self.upload_image(Locators.IMAGE_UPLOAD_INPUT, picture_link)

    @allure.step("Добавление описания рецепта")
    def set_recipe_description(self, text):
        self.send_keys(Locators.RECIPE_DESCRIPTION_INPUT, text)

    @allure.step("Заполнение полей рецепта")
    def fill_recipe_fields(self, recipe_data):
        self.fill_recipe_name_field(recipe_data['recipe_name'])
        for _ in range(recipe_data['ingredients_number']):
            self.add_random_ingredient()
        self.set_cooking_time(recipe_data['cooking_time'])
        self.upload_picture_to_recipe(recipe_data['picture_link'])
        self.set_recipe_description(recipe_data['recipe_description'])

    @allure.step("Клик по кнопке «Создать рецепт»")
    def click_on_create_recipe_button(self):
        self.click_on(Locators.CREATE_RECIPE_BUTTON)
        self.wait_for_element_to_be_visible(Locators.CREATE_RECIPE_BUTTON)

    @allure.step("Создание рецепта")
    def create_recipe(self, recipe_data):
        self.fill_recipe_fields(recipe_data)
        self.click_on_create_recipe_button()
        self.wait_for_url_matches(URLs.READY_RECIPE_URL_PATTERN)

    @allure.step("Извлечение имени рецепта")
    def get_recipe_title(self):
        self.wait_for_element_to_be_visible(Locators.RECIPE_TITLE)
        recipe_title = self.find_element(Locators.RECIPE_TITLE).text

        with allure.step('Данные теста'):
            allure.attach(str(recipe_title), name='recipe_title')

        return recipe_title