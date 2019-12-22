from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class ResultPage(BasePage):

    @property
    def result_header(self):
        locator = Locator(By.CSS_SELECTOR, '.findSearchTerm')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )

