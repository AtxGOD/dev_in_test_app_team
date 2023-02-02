import pytest

from framework.sidebar_page import SideBarPage


@pytest.fixture(scope='session')
def start(driver):
    obj = SideBarPage(driver)
    obj.log_in()
    yield obj


@pytest.fixture(scope='function')
def side_bar_fixture(start):
    yield start
    start.click_back()
