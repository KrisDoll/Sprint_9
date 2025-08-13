import allure
from pages.auth_page import Authorization
from helpers.URLs import URLs
from conftest import driver, register_user


@allure.suite("Авторизация пользователя")
class TestAuthorization:

    @allure.description("Успешная авторизация пользователя")
    def test_authorisation(self, driver, register_user):
        page = Authorization(driver)
        page.login_to_account(register_user)
        assert page.get_current_url() == URLs.RECIPES_PAGE
        assert page.logout_is_visible() is True