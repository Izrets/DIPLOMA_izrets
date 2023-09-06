from mainlogic._init_ import Business, User, SignIn
from browser_chrome import Browser
from Automation.mainlogic.element import Random
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

# @pytest.fixture()
# def user_test():
#     return User(email="I1vanov123@ya.ru", password='q1w2e3')


@pytest.fixture()
def browser():
    setup_logging(time.strftime("%Y_%m_%d_%H_%M_%S"))
    return Browser()


# @pytest.fixture()
# def logic_test():
#     return Logic_data() #, email="I1vanov123@ya.ru", password='q1w2e3'
@pytest.fixture()
def user_test():
    return User(email="I1vanov123@ya.ru", password='q1w2e3')

# @pytest.fixture()
# def data_to_randomdata():
#     return Randomdata(grid='', count_of_divs='', in_stock_items='', path_of_button='')

class Testmainlogicpath:
    def test_logic(self, browser, user_test):
        LOGGER.info("Logging in")
        browser.go_to_site(SignIn.path)
        # browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(10)
        page = SignIn(browser)
        page.signin(user_test)
        browser.driver.implicitly_wait(10)



        LOGGER.info("Start testing mainlogic path")
        browser.go_to_site(Business.path)
        browser.driver.implicitly_wait(10)
        browser.go_to_site(Random.path)
        page = Business(browser)
        # page2 = Random(browser)
        page.logic_run()
        browser.driver.close()
        time.sleep(10)
        LOGGER.info("Mainlogic path works")
