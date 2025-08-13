import allure
from pages.auth_page import Authorization
from helpers.URLs import URLs
from conftest import driver
from helpers.generator import Generator


@allure.suite("Создание аккаунта")
class TestAccountCreate:

    @allure.description("Успешное создание аккаунта")
    def test_create_account(self, driver):
        page = Authorization(driver)
        page.get_signin_page()
        page.click_on_signup_button()
        user_data = Generator.generate_user_data()
        page.create_user(user_data)
        assert page.get_current_url() == URLs.SIGNIN_PAGE
