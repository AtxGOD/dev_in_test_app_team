import pytest

from framework.sidebar_page import SideBarLocators


test_sidebar_icons_data = [(SideBarLocators.LOCATOR_ADD_HUB_BUTTON, '//*[@resource-id="com.ajaxsystems:id/toolbarTitle"]', 'Add hub'),
                           (SideBarLocators.LOCATOR_APP_SETTINGS_BUTTON, '//*[@resource-id="com.ajaxsystems:id/toolbarTitle"]', 'Account'),
                           (SideBarLocators.LOCATOR_HELP_BUTTON, '//*[@resource-id="com.ajaxsystems:id/toolbarTitle"]', 'Installation Manuals'),
                           (SideBarLocators.LOCATOR_PERORT_A_PROBLEM_BUTTON, '//*[@resource-id="com.ajaxsystems:id/title" and @text="Report a problem"]', 'Report a problem'),
                           (SideBarLocators.LOCATOR_VIDEO_SURVEILLANCE_BUTTON, '//*[@resource-id="com.ajaxsystems:id/toolbarTitle"]', 'Video Surveillance')]


@pytest.mark.parametrize('element, xpath, expected', test_sidebar_icons_data)
def test_sidebar_icons(side_bar_fixture, element, xpath, expected):
    side_bar_fixture.click_side_bar_elements(element)
    assert side_bar_fixture.try_to_find_element(xpath) == expected




