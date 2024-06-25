"""Tools & helpers to assist using selenium"""

import io
import json
import re
from datetime import datetime

from selenium import webdriver


def build_ff_options():
    ff_options = webdriver.FirefoxOptions()
    ff_options.add_argument("-headless")
    return ff_options


def get_remote_ff(sel_url: str):
    driver = webdriver.Remote(
        command_executor=sel_url,
        options=build_ff_options(),
    )
    return driver


def get_remote_chrome(selenium_url: str):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.setCapability("browserVersion", "100")
    # chrome_options.setCapability("platformName", "Windows")
    # // Showing a test name instead of the session id in the Grid UI
    # chrome_options.setCapability("se:name", "My simple test")
    # // Other type of metadata can be seen in the Grid UI by clicking on the
    # // session info or via GraphQL
    # chrome_options.setCapability("se:sampleMetadata", "Sample metadata value")
    # driver = new RemoteWebDriver(new URL("http://gridUrl:4444"), chromeOptions);
    driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
    return driver


def get_timestamp():
    now = datetime.now()  # current date and time
    # date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    date_time = now.strftime("%Y-%m-%d_%H_%M_%S")
    print("date and time:", date_time)
    return date_time


def get_date():
    now = datetime.now()  # current date and time
    # date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    date_time = now.strftime("%Y-%m-%d")
    print("date and time:", date_time)
    return date_time


def write_json_to_file(data: dict, file: str) -> None:
    """Write JSON to file as dicussed here
    https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file"""
    with io.open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False))


def string_between_dots(text) -> str:
    """String between two dots

    Args:
        text (_type_): String to extract substring from.

    Returns:
        str: If string contains two dots the string between them - empty string otherwise.
    """
    pattern = r"\.(.*?)\."
    matches = re.findall(pattern, text)
    if len(matches) > 0:
        return matches[0]
    else:
        return ""


def sabitize_string(input: str) -> str:
    output = input.replace(" ", "_").replace(".", "_")
    return output
