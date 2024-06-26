from selenium.common.exceptions import WebDriverException

from selenium_tools.selenium_grid import get_remote_chrome, get_remote_chrome_download, get_remote_ff
from selenium_tools.tools import get_timestamp, string_between_dots
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os

SELENIUM_HUB_URL = "http://selenium-hub.local:4444/wd/hub"
what_is_my_browser = "https://www.whatsmybrowser.org/"
heise = "https://www.heise.de"
heise_expected_title = "heise online - IT-News, Nachrichten und Hintergründe | heise online"
TEST_TIME = get_timestamp()

DOWNLOADS_CHROMIUM = f"./downloads/{TEST_TIME}/chromium"
os.makedirs(DOWNLOADS_CHROMIUM, exist_ok=True)


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


def test_download_file():
    try:
        driver = get_remote_chrome_download(selenium_url=SELENIUM_HUB_URL)
        driver.get(url="http://xcal1.vodafone.co.uk")

        assert driver.title == "Download Test Files"
        all_href = driver.find_elements(By.XPATH, "//*[contains(@href, 'http://212.183.159.230/5MB.zip')]")
        assert all_href is not None
        assert len(all_href) == 2
        all_href[0].click()
        all_href[1].click()
        WebDriverWait(driver, timeout=120, poll_frequency=5).until(lambda d: "5MB.jpg" in d.get_downloadable_files())
        files = driver.get_downloadable_files()
        print(f"files: {files}")
        for file in files:
            print(f"file: {file}")
            driver.download_file(file, DOWNLOADS_CHROMIUM + "/pdf")
    except WebDriverException:
        print(f"WebDriver Error occured: {WebDriverException}")
    finally:
        if driver is not None:
            driver.quit()


def get_and_test_title(driver):
    driver.get(heise)
    print(f"driver.title: {driver.title}")
    assert driver.title == heise_expected_title
