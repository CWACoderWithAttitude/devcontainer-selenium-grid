# est_download_example.py
# https://www.browserstack.com/guide/download-file-using-selenium-python
import os
import time

import pytest
from selenium.webdriver.common.by import By

from selenium_tools.selenium_grid import get_remote_chrome, get_remote_ff
from selenium_tools.tools import get_date

DOWNLOADS_FIREFOX = None
DOWNLOADS_CHROMIUM = None

SELENIUM_HUB_URL = "http://selenium-hub.local:4444/wd/hub"
TS = get_date()
DOWNLOADS_FIREFOX = f"./downloads/{TS}/firefox"
DOWNLOADS_CHROMIUM = f"./downloads/{TS}/chromium"
os.makedirs(DOWNLOADS_CHROMIUM, exist_ok=True)
os.makedirs(DOWNLOADS_FIREFOX, exist_ok=True)


def test_download_csv_chromium():
    driver = get_remote_chrome(selenium_url=SELENIUM_HUB_URL)
    driver.get("https://www.browserstack.com/test-on-the-right-mobile-devices")
    gotit = driver.find_element(By.ID, "accept-cookie-notification")
    gotit.click()
    downloadcsv = driver.find_element(By.CSS_SELECTOR, ".icon-csv")
    downloadcsv.click()
    time.sleep(5)
    files = driver.get_downloadable_files()
    for file in files:
        print(f"file: {file}")
        driver.download_file(file, DOWNLOADS_CHROMIUM)
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
        driver.download_file(file, DOWNLOADS_FIREFOX)
    driver.close()


def test_download_firefox_pdf():
    """Not OK"""
    driver = get_remote_ff(selenium_url=SELENIUM_HUB_URL)
    driver.get(
        "https://www.nlbk.niedersachsen.de/download/164891/Test-pdf_3.pdf.pdf&ved=2ahUKEwirkcyF9euGAxWrhP0HHbIsCPMQFnoECAYQAQ&usg=AOvVaw3cbUuEsNudpk695i_2Ho-R"
    )
    time.sleep(15)
    files = driver.get_downloadable_files()
    print(f"files: {files}")
    for file in files:
        print(f"file: {file}")
        driver.download_file(file, DOWNLOADS_FIREFOX + "/pdf")
    driver.close()


def test_download_chromium_pdf():
    """OK"""
    driver = get_remote_chrome(selenium_url=SELENIUM_HUB_URL)
    driver.get(
        "https://www.nlbk.niedersachsen.de/download/164891/Test-pdf_3.pdf.pdf&ved=2ahUKEwirkcyF9euGAxWrhP0HHbIsCPMQFnoECAYQAQ&usg=AOvVaw3cbUuEsNudpk695i_2Ho-R"
    )
    time.sleep(15)
    files = driver.get_downloadable_files()
    print(f"files: {files}")
    for file in files:
        print(f"file: {file}")
        driver.download_file(file, DOWNLOADS_CHROMIUM + "/pdf")
    driver.close()


def test_download2_chromium_pdf():
    """Not OK"""
    driver = get_remote_chrome(selenium_url=SELENIUM_HUB_URL)
    driver.get("https://www.corelegal.de/de-wAssets/docs/test.pdf")
    time.sleep(15)
    files = driver.get_downloadable_files()
    print(f"files: {files}")
    for file in files:
        print(f"file: {file}")
        driver.download_file(file, DOWNLOADS_CHROMIUM + "/pdf")
    driver.close()
