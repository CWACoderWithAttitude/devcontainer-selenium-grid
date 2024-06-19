from selenium.common.exceptions import WebDriverException

from selenium_tools.selenium_grid import get_remote_chrome, get_remote_chrome_download, get_remote_ff
from selenium_tools.tools import get_timestamp, string_between_dots
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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


def get_and_test_title(driver):
    driver.get(heise)
    print(f"driver.title: {driver.title}")
    assert driver.title == heise_expected_title
