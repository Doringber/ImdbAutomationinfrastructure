from pytest import mark

from common.logger import Logger
from pages.home_page import HomePage
from pages.movie_page import MoviePage
from .test_base import TestBase
from termcolor import colored


@mark.smoke
@mark.search_movie_titlepy
def test_movie_title(chrome_browser):
    home_page = HomePage(driver=chrome_browser)
    movie_page = MoviePage(driver=chrome_browser)
    movie_title = "Star Wars: Episode IX - The Rise of Skywalker (2019)\nPG-13 | 2h 21min | Action, Adventure, Fantasy | 20 December 2019 (USA)"

    print(colored('Step 1: open {} ', 'blue').format(str(home_page.url)))
    chrome_browser.get('https://www.imdb.com')

    print(colored('Step 2: Tap on first movie on opening week  ', 'blue'))
    home_page.opening_this_week_first_movie.click( )

    print(colored('Step 3: verify movie title ', 'blue'))
    text = movie_page.movie_title.text

    print(colored('Step 4: verify movie title asset', 'blue'))
    assert text == movie_title
