import pytest

from framework.page import Page


test_data_user_login = [(Page.valid_login, Page.valid_password, 'Add hub'),
                        ('qa.ajax.app.automation@gmail.com', 'wrong_password', False),
                        ('email', 'password', False)]


@pytest.mark.parametrize('login, password, expected', test_data_user_login)
def test_user_login(user_login_fixture, login, password, expected):
    user_login_fixture.click_on_log_in_button()
    user_login_fixture.enter_username_and_password(login, password)
    user_login_fixture.click_log_in_next_button()
    assert user_login_fixture.check_logged_in() == expected


test_data_wrong_field = [('qa.ajax.app.automation@gmail.com', ''),
                         ('', 'wrong_password')]


@pytest.mark.parametrize('login, password', test_data_wrong_field)
def test_wrong_field(user_login_fixture, login, password):
    user_login_fixture.click_on_log_in_button()
    user_login_fixture.enter_username_and_password(login, password)
    user_login_fixture.click_log_in_next_button()
    assert user_login_fixture.check_wrong_field() == 'Please fill all required fields.'
