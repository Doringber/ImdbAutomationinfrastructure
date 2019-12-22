from selenium.webdriver.common.by import By

from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class HomePage(BasePage):
    url = 'https://www.imdb.com/'

    @property
    def search_bar(self):
        locator = Locator(By.ID, 'suggestion-search')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )

    @property
    def search_button(self):
        locator = Locator(By.ID, 'suggestion-search-button')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )

    @property
    def first_item(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.video-modal')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def opening_this_week_first_movie(self):
        locator = Locator(by=By.XPATH, value="//*[@class='title']//a")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
