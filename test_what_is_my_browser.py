import os
import time

import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium_tools.selenium_grid import get_remote_chrome, get_remote_chrome_download, get_remote_ff
from selenium_tools.tools import get_date, get_timestamp, string_between_dots

SELENIUM_HUB_URL = "http://selenium-hub.local:4444/wd/hub"
what_is_my_browser = "https://www.whatsmybrowser.org/"
heise = "https://www.heise.de"
heise_expected_title = "heise online - IT-News, Nachrichten und Hintergründe | heise online"
TEST_TIME = get_timestamp()
IMAGE_BASE = "images"
IMAGE_DIR = f"images/{get_date()}"


@pytest.fixture()
def init():
    os.makedirs(IMAGE_DIR, exist_ok=True)


def test_make_screenshot_from_page_firefox(init):
    try:
        driver = get_remote_ff(selenium_url=SELENIUM_HUB_URL)
        driver.get(url=what_is_my_browser)
        shot_ok = driver.get_screenshot_as_file(f"./{IMAGE_DIR}/{TEST_TIME}-{string_between_dots(what_is_my_browser)}_firefox.png")
        assert shot_ok is True
    except WebDriverException:
        print(f"WebDriver Error occured: {WebDriverException}")
    finally:
        if driver is not None:
            driver.quit()


def test_make_screenshot_from_page_chromium(init):
    chrome_versions = ["125.0", "126.0"]
    for version in chrome_versions:
        try:
            driver = get_remote_chrome(selenium_url=SELENIUM_HUB_URL, browserVersion=version)
            driver.get(url=what_is_my_browser)
            shot_ok = driver.get_screenshot_as_file(
                f"./{IMAGE_DIR}/{TEST_TIME}-{string_between_dots(what_is_my_browser)}_chromium_{version}.png"
            )
            assert shot_ok is True
        except WebDriverException:
            print(f"WebDriver Error occured: {WebDriverException}")
        finally:
            if driver is not None:
                driver.quit()
