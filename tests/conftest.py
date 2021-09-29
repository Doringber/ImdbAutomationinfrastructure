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
    browser = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME)
    # browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    browser.maximize_window()
    return browser


@pytest.fixture(scope='function')
def safari_browser():
    browser = webdriver.Safari()
    browser.maximize_window()
    return browser
