import pytest
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

from selenium_tools.selenium_grid import get_remote_chrome, get_remote_chrome_download, get_remote_ff
from selenium_tools.tools import get_timestamp, string_between_dots
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

SELENIUM_HUB_URL = "http://selenium-hub.local:4444/wd/hub"
what_is_my_browser = "https://www.whatsmybrowser.org/"
heise = "https://www.heise.de"
heise_expected_title = "heise online - IT-News, Nachrichten und Hintergründe | heise online"
TEST_TIME = get_timestamp()


@pytest.fixture()
def init():
    pass


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
        WebDriverWait(driver, 5).until(lambda d: "5MB.jpg" in d.get_downloadable_files())
        files = driver.get_downloadable_files()
        for file in files:
            print(f"file: {file}")
            driver.download_file(file, "./downloads")
    except NoSuchElementException as nsex:
        print(f"NoSuchElementException occured: {nsex}")
    # except TimeoutException as tex:
    #    print(f"TimeoutException occured: {tex}")
    except WebDriverException as wdex:
        print(f"WebDriver Error occured: {str(wdex)}, args: {wdex.args}")
    finally:
        if driver is not None:
            driver.quit()
