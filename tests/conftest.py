import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def chrome_browser():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # browser = webdriver.Remote(command_executor="http://localhost:4444",desired_capabilities=DesiredCapabilities.CHROME)
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.implicitly_wait(5)
    browser.maximize_window()
    return browser


@pytest.fixture(scope='function')
def safari_browser():
    browser = webdriver.Safari()
    browser.maximize_window()
    return browser
