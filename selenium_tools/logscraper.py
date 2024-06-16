import os
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

ID_PWD_FIELD = "uiPassInput"
ID_BTN_OK = "submitLoginBtn"
sel_url = "http://selenium-hub:4444/wd/hub"
ID_PWD_FIELD = "uiPassInput"
ID_BTN_OK = "submitLoginBtn"
FRITZ_BOX_TITLE_AFTER_LOGIN = "FRITZ!Box 6591 Cable"
HEISE_URL = "https://www.heise.de"
FRITZBOX_URL = os.environ["FRITZBOX_URL"]
FRITZBOX_USER = os.environ["FRITZBOX_USER"]
FRITZBOX_PASSWORD = os.environ["FRITZBOX_PASSWORD"]
WHAT_BROWSER = os.environ["WHAT_BROWSER"]
SELENIUM_HUB_URL = "http://selenium-hub:4444"


def get_logs_from_fritzbox() -> list:
    """Retrieve all logs from fritzbox as json array

    Returns:
        list[]: _description_
    """
    driver = fritz_login(FRITZBOX_URL, FRITZBOX_USER, FRITZBOX_PASSWORD)
    logbox = get_logbox(driver=driver)
    assert logbox != "bubu"
    log_json = get_log_entries_from_logbox(logbox)
    return log_json


def build_ff_options():
    ff_options = webdriver.FirefoxOptions()
    ff_options.add_argument("-headless")
    return ff_options


def get_remote_ff(selenum_grid_url: str):
    """Helper to get default firefox browser"""
    driver = webdriver.Remote(
        command_executor=selenum_grid_url,
        options=build_ff_options(),
    )
    return driver




def get_remote_chrome(selenum_grid_url: str):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver1 = webdriver.Remote(
        command_executor=selenum_grid_url,
        # desired_capabilities={
        #    "browserName": "chrome",
        # },
        options=chrome_options,
    )
    # dc = webdriver.DesiredCapabilities()
    # dc.add("browserName", "chromium")  ##{'browserName': 'firefox', 'javascriptEnabled': True})
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.setCapability("browserVersion", "100")
    # chrome_options.setCapability("platformName", "Windows")
    # // Showing a test name instead of the session id in the Grid UI
    # chrome_options.setCapability("se:name", "My simple test")
    # // Other type of metadata can be seen in the Grid UI by clicking on the
    # // session info or via GraphQL
    # chrome_options.setCapability("se:sampleMetadata", "Sample metadata value")
    # driver = new RemoteWebDriver(new URL("http://gridUrl:4444"), chromeOptions);
    # driver = webdriver.Remote(command_executor=sel_url, options=chrome_options)
    return driver1
