from selenium import webdriver


def build_ff_options():
    ff_options = webdriver.FirefoxOptions()
    ff_options.add_argument("-headless")
    return ff_options


def get_remote_ff(selenium_url: str):
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=build_ff_options(),
    )
    return driver


def get_remote_chrome(selenium_url: str):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
    return driver
