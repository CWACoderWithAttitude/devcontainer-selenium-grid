from selenium.common.exceptions import WebDriverException

from selenium_tools.selenium_grid import get_remote_chrome, get_remote_ff
from selenium_tools.tools import get_timestamp, string_between_dots
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

SELENIUM_HUB_URL = "http://selenium-hub.local:4444/wd/hub"
what_is_my_browser = "https://www.whatsmybrowser.org/"
heise = "https://www.heise.de"
TEST_TIME = get_timestamp()


def test_make_screenshot_from_page_firefox():
    try:
        driver = get_remote_ff(selenium_url=SELENIUM_HUB_URL)
        driver.get(url=what_is_my_browser)
        shot_ok = driver.get_screenshot_as_file(f"./{TEST_TIME}-{string_between_dots(what_is_my_browser)}_firefox.png")
        assert shot_ok is True
    except WebDriverException:
        print(f"WebDriver Error occured: {WebDriverException}")
    finally:
        if driver is not None:
            driver.quit()


def test_make_screenshot_from_page_chrome():
    try:
        driver = get_remote_chrome(selenium_url=SELENIUM_HUB_URL)
        driver.get(url=what_is_my_browser)
        shot_ok = driver.get_screenshot_as_file(f"./{TEST_TIME}-{string_between_dots(what_is_my_browser)}_chrome.png")
        assert shot_ok is True
    except WebDriverException:
        print(f"WebDriver Error occured: {WebDriverException}")
    finally:
        if driver is not None:
            driver.quit()
