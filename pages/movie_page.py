from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class MoviePage(BasePage):

    @property
    def movie_title(self):
        locator = Locator(By.XPATH, "//div[@class='title_wrapper']")
        return BaseElement(
            driver=self.driver,
            locator=locator

        )

