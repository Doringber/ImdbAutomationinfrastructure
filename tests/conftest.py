import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    browser.maximize_window()
    return browser


@pytest.fixture(scope='function')
def safari_browser():
    browser = webdriver.Safari()
    browser.maximize_window()
    return browser