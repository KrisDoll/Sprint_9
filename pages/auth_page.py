import allure
from pages.base_page import BasePage
from helpers.URLs import URLs
from helpers.locators import Locators


class Authorization(BasePage):

    @allure.step("Переход на страницу «Авторизации»")
    def get_signin_page(self):
        self.get_page(URLs.SIGNIN_PAGE)

    @allure.step("Клик по кнопке «Создать аккаунт» в шапке страницы")
    def click_on_signup_button(self):
        self.wait_for_element_to_be_clickable(Locators.SIGNUP_BUTTON)
        self.click_on(Locators.SIGNUP_BUTTON)
        self.wait_for_page(URLs.SIGNUP_PAGE)

    @allure.step("Заполнение полей регистрации")
    def fill_registration_fields(self, user_data):
        self.send_keys(Locators.FIRST_NAME_FIELD, user_data['first_name'])
        self.send_keys(Locators.LAST_NAME_FIELD, user_data['last_name'])
        self.send_keys(Locators.USER_NAME_FIELD, user_data['user_name'])
        self.send_keys(Locators.EMAIL_FIELD, user_data['email'])
        self.send_keys(Locators.PASSWORD_FIELD, user_data['password'])

    @allure.step("Клик по кнопке «Создать аккаунт»")
    def click_on_register_account(self):
        self.click_on(Locators.CREATE_ACCOUNT_BUTTON)

    @allure.step("Регистрация пользователя")
    def create_user(self, user_data):
        self.fill_registration_fields(user_data)
        self.click_on_register_account()
        self.wait_for_page(URLs.SIGNIN_PAGE)

    @allure.step("Заполнение полей авторизации")
    def fill_login_fields(self, user_data):
        self.send_keys(Locators.EMAIL_FIELD, user_data['email'])
        self.send_keys(Locators.PASSWORD_FIELD, user_data['password'])

    @allure.step("Клик по кнопке «Войти»")
    def click_on_login_to_account(self):
        self.click_on(Locators.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step("Вход в аккаунт")
    def login_to_account(self, user_data):
        self.fill_login_fields(user_data)
        self.click_on_login_to_account()
        self.wait_for_page(URLs.RECIPES_PAGE)

    @allure.step("Состояние кнопки «Выход»")
    def logout_is_visible(self):
        return self.find_element(Locators.LOGOUT_BUTTON).is_displayed()