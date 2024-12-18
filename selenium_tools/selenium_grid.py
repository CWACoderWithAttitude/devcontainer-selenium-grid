from selenium import webdriver


def build_ff_options():
    ff_options = webdriver.FirefoxOptions()
    ff_options.add_argument("-headless")
    ff_options.enable_downloads = True
    return ff_options


def get_remote_ff(selenium_url: str):
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=build_ff_options(),
    )
    return driver


def get_remote_chrome(selenium_url: str, browserVersion="126.0"):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.enable_downloads = True
    if browserVersion is not None:
        chrome_options.set_capability("browserVersion", browserVersion)
    # https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/drivers/test_remote_webdriver.py#L43C5-L43C36
    driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
    return driver


def get_remote_chrome_download(selenium_url: str):
    return get_remote_chrome(selenium_url=selenium_url)
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.setcapability("se:downloadsEnabled", True)
    # chrome_options.set_capability("se:downloadsEnabled", True)
    chrome_options.enable_downloads = True
    chrome_options.add_argument("--headless=new")

    # desiredCapabilities = webdriver.DesiredCapabilities.CHROME.copy()

    # desiredCapabilities["version"] = "125.0"
    # https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/drivers/test_remote_webdriver.py#L43C5-L43C36
    # chrome_options.enable_downloads = True
    driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
    return driver
