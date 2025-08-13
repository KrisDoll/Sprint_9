
from pages.auth_page import Authorization
from helpers.generator import Generator
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "latest")
    options.set_capability("selenoid:options", {
        "enableVNC": False,
        "enableVideo": False
    })

    driver = webdriver.Remote(
        command_executor=os.getenv('SELENOID_URL'),
        options=options
    )
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture()
def register_user(driver):
    user_data = Generator.generate_user_data()
    page = Authorization(driver)
    page.get_signin_page()
    page.click_on_signup_button()
    page.create_user(user_data)
    return user_data


@pytest.fixture()
def login_user(driver, register_user):
    page = Authorization(driver)
    page.login_to_account(register_user)