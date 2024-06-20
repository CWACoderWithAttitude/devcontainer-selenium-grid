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


def test_download_csv():
    # options = webdriver.ChromeOptions()
    # prefs = {"download.default_directory": "./downloads/"}
    ## example: prefs = {"download.default_directory" : "C:\Tutorial\down"};
    # options.add_experimental_option("prefs", prefs)
    # driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
    driver = get_remote_chrome_download(selenium_url=SELENIUM_HUB_URL)
    # try:
    driver.get("https://www.browserstack.com/test-on-the-right-mobile-devices")
    print(f"title: {driver.title}")
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


#    except:
#        print("Invalid URL")
