import pytest
import os
from selenium_tools.selenium_grid import get_remote_ff, get_remote_chrome
from selenium.common.exceptions import WebDriverException
from selenium_tools.tools import get_timestamp

SELENIUM_HUB_URL = "http://selenium-hub.local:4444/wd/hub"
what_is_my_browser = "https://www.whatsmybrowser.org/"
heise = "https://www.heise.de"
heise_expected_title = "heise online - IT-News, Nachrichten und Hintergründe | heise online"
TEST_TIME = get_timestamp()


def test_get_heise_with_firefox():
    driver = None
    try:
        driver = get_remote_ff(SELENIUM_HUB_URL)
        get_and_test_title
    except WebDriverException:
        print(f"WebDriver Error occured: {WebDriverException}")
    finally:
        if driver is not None:
            driver.quit()


def test_get_heise_with_chrome():
    driver = None
    try:
        driver = get_remote_chrome(SELENIUM_HUB_URL)
        get_and_test_title(driver)
    except WebDriverException:
        print(f"WebDriver Error occured: {WebDriverException}")
    finally:
        if driver is not None:
            driver.quit()


def test_make_screenshot_from_page_firefox():
    try:
        driver = get_remote_ff(selenium_url=SELENIUM_HUB_URL)
        driver.get(url=what_is_my_browser)
        shot_ok = driver.get_screenshot_as_file(f"./{TEST_TIME}-wimb_firefox.png")
        assert shot_ok is True
    except WebDriverException:
        print(f"WebDriver Error occured: {WebDriverException}")
    finally:
        if driver is not None:
            driver.quit()


def test_make_screenshot_from_page_chrome():
    try:
        driver = get_remote_chrome(selenium_url=SELENIUM_HUB_URL)
        driver.get(url="https://www.heise.de")
        shot_ok = driver.get_screenshot_as_file(f"./{TEST_TIME}-wimb_chrome.png")
        assert shot_ok is True
    except WebDriverException:
        print(f"WebDriver Error occured: {WebDriverException}")
    finally:
        if driver is not None:
            driver.quit()


def get_and_test_title(driver):
    driver.get(heise)
    print(f"driver.title: {driver.title}")
    assert driver.title == heise_expected_title
