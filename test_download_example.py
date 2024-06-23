# est_download_example.py
# https://www.browserstack.com/guide/download-file-using-selenium-python
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

from selenium_tools.selenium_grid import get_remote_chrome, get_remote_chrome_download, get_remote_ff
from selenium_tools.tools import get_timestamp, string_between_dots
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import time

SELENIUM_HUB_URL = "http://selenium-hub.local:4444/wd/hub"


def test_download_csv_chromium():
    driver = get_remote_chrome_download(selenium_url=SELENIUM_HUB_URL)
    driver.get("https://www.browserstack.com/test-on-the-right-mobile-devices")
    gotit = driver.find_element(By.ID, "accept-cookie-notification")
    gotit.click()
    downloadcsv = driver.find_element(By.CSS_SELECTOR, ".icon-csv")
    downloadcsv.click()
    time.sleep(5)
    files = driver.get_downloadable_files()
    for file in files:
        print(f"file: {file}")
        driver.download_file(file, "./downloads")
    driver.close()


def test_download_csv_firefox():
    driver = get_remote_ff(selenium_url=SELENIUM_HUB_URL)
    driver.get("https://www.browserstack.com/test-on-the-right-mobile-devices")
    gotit = driver.find_element(By.ID, "accept-cookie-notification")
    gotit.click()
    downloadcsv = driver.find_element(By.CSS_SELECTOR, ".icon-csv")
    downloadcsv.click()
    time.sleep(5)
    files = driver.get_downloadable_files()
    for file in files:
        print(f"file: {file}")
        driver.download_file(file, "./downloads")
    driver.close()


def test_download_pdf_firefox():
    driver = get_remote_ff(selenium_url=SELENIUM_HUB_URL)
    driver.get("https://www.corelegal.de/de-wAssets/docs/test.pdf")
    # gotit = driver.find_element(By.ID, "accept-cookie-notification")
    # gotit.click()
    # downloadcsv = driver.find_element(By.CSS_SELECTOR, ".icon-csv")
    # downloadcsv.click()
    time.sleep(15)
    files = driver.get_downloadable_files()
    print(f"files: {files}")
    for file in files:
        print(f"file: {file}")
        driver.download_file(file, "./downloads")
    driver.close()


def test_download_pdf():
    driver = get_remote_chrome_download(selenium_url=SELENIUM_HUB_URL)
    driver.get(
        "https://www.nlbk.niedersachsen.de/download/164891/Test-pdf_3.pdf.pdf&ved=2ahUKEwirkcyF9euGAxWrhP0HHbIsCPMQFnoECAYQAQ&usg=AOvVaw3cbUuEsNudpk695i_2Ho-R"
    )
    # gotit = driver.find_element(By.ID, "accept-cookie-notification")
    # gotit.click()
    # downloadcsv = driver.find_element(By.CSS_SELECTOR, ".icon-csv")
    # downloadcsv.click()
    time.sleep(15)
    files = driver.get_downloadable_files()
    print(f"files: {files}")
    for file in files:
        print(f"file: {file}")
        driver.download_file(file, "./downloads")
    driver.close()
