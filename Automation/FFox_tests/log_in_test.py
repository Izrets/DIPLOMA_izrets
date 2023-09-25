from Automation.login._init_ import SignIn, User
from Automation.browser_firefox import Browser
import pytest
import time

import logging
from pathlib import Path

LOGGER = logging.getLogger(__name__)


def setup_logging(id_test):
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    filenamelog = logs_dir/f"Logging_in_Tric{id_test}.log"
    root_logger = logging.getLogger()
    file_handler = logging.FileHandler(filenamelog)
    file_handler.setLevel(level="INFO")
    log_format = logging.Formatter("[%(asctime)s - %(levelname)s - <%(module)s>: %(message)s]")
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)
    root_logger.setLevel(level="INFO")


@pytest.fixture()
def user_test():
    return User(email="I1vanov123@ya.ru", password='q1w2e3')


@pytest.fixture()
def browser():
    setup_logging(time.strftime("%Y_%m_%d_%H_%M_%S"))
    return Browser()


class TestSignUpPage:
    def test_signin(self, browser, user_test):
        LOGGER.info("Запуск тестирования: test_signUp")
        browser.go_to_site(SignIn.path)
        # browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(10)
        page = SignIn(browser)
        page.signin(user_test)
        time.sleep(10)
        LOGGER.info("Тестирование test_signUp завершено")