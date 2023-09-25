from Automation.mainlogic._init_ import LogicRun, User, SignIn
from Automation.browser_firefox import Browser
import pytest
import time
import logging
from pathlib import Path

LOGGER = logging.getLogger(__name__)


def setup_logging(id_test):
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    filenamelog = logs_dir/f"Register_Tric{id_test}.log"
    root_logger = logging.getLogger()
    file_handler = logging.FileHandler(filenamelog)
    file_handler.setLevel(level="INFO")
    log_format = logging.Formatter("[%(asctime)s - %(levelname)s - <%(module)s>: %(message)s]")
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)
    root_logger.setLevel(level="INFO")




@pytest.fixture()
def browser():
    setup_logging(time.strftime("%Y_%m_%d_%H_%M_%S"))
    return Browser()



@pytest.fixture()
def user_data():
    return User(email="I1vanov123@ya.ru", password='q1w2e3')


class Testplaylogic:
    def test_logic(self, browser, user_data):
        LOGGER.info("Logging in")
        browser.go_to_site(SignIn.path)
        # browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(10)
        page = SignIn(browser)
        page.signin(user_data)
        browser.driver.implicitly_wait(10)
        LOGGER.info("Logged in")

        LOGGER.info("Start buying")
        browser.go_to_site(LogicRun.path)
        LOGGER.info('got the page')
        page = LogicRun(browser)
        page.logicrun(browser)

