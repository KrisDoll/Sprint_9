import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.auth_page import Authorization
from helpers.generator import Generator


@pytest.fixture()
def driver():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "latest",
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities
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