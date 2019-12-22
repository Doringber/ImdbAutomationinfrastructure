from pytest import mark

from common.logger import Logger
from pages.home_page import HomePage
from pages.result_page import ResultPage
from .test_base import TestBase
from termcolor import colored




@mark.smoke
@mark.search_movie
def test_click_first_button(chrome_browser):
    result_page = ResultPage(driver=chrome_browser)
    home_page = HomePage(driver=chrome_browser)

    print(colored('Step 1: open {} ', 'blue').format(str(home_page.url)))
    chrome_browser.get('https://www.imdb.com')

    print(colored('Step 2: search homeland ', 'blue'))
    home_page.search_bar.type_text('homeland')

    print(colored('Step 3: Click on search button ', 'blue'))
    home_page.search_button.click()

    print(colored('Step 4: Verify result header', 'blue'))
    test = result_page.result_header.text
    Logger.get_instance().log_assert(test is not None, 'Failed finding search header')








