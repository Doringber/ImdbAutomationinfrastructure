from pytest import mark

from common.logger import Logger
from pages.home_page import HomePage
from termcolor import colored


@mark.smoke
@mark.search_movie_titlepy
def test_menu_title(chrome_browser):
    home_page = HomePage(driver=chrome_browser)

    print(colored(' Step 1: open {} ', 'blue').format(str(home_page.url)))
    chrome_browser.get('https://www.imdb.com')

    print(colored('Step 2: Tap on first movie on opening week  ', 'blue'))
    home_page.menu_button.click()

    print(colored('Step 3: verify movie title ', 'blue'))
    text = home_page.menu_list_DVD.text

    print(colored('Step 4: verify movie title asset', 'blue'))
    Logger.get_instance().log_assert(text is not None, 'Failed finding menu text')
