import pytest
import os
from selenium_tools import get_remote_ff

SELENIUM_HUB_URL = os.environ["SELENIUM_HUB_URL"]


def test_get_remote_ff():
    try:
        driver = get_remote_ff(SELENIUM_HUB_URL)
    except:
        if driver is not None:
            driver.quit()
    else:
        assert driver.capabilities == "bubu"
