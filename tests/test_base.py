import unittest

import os
from os import path

from termcolor import colored
from selenium import webdriver


MESSAGE_TEST_START_RUNNING = '\n===============| Test "%s" Started Running |==============='
MESSAGE_TEST_FINISHED_RUNNING = '===============| Test "%s" Finished Running |===============\n'


class TestBase(unittest.TestCase):

    def setUp(self):
        print(colored(MESSAGE_TEST_START_RUNNING % self._testMethodName, "green"))

        # Boot step 1: Setup logger
        # Logger.get_instance().initialization(self)

        # Boot step 2: Open URL
        # self.browser = webdriver.Chrome()

        self.__setup_appium_driver__()

    def tearDown(self):
        print(colored(MESSAGE_TEST_FINISHED_RUNNING % self._testMethodName, "green"))
        # self.take_screenshot()
        # self.browser.quit()


    def __setup_appium_driver__(self):
       # Logger.get_instance( ).take_screenshot()
       # self.take_screenshot()

       # Logger.get_instance( ).take_screenshot("application_finished_launching")
       print('Step 0.1: Application finished launching')

    def take_screenshot(self):
        self.test_logs_path = 'logs/screenshots/' + self._testMethodName.split(".")[-1] + "_screenshot.png"

        if path.exists(self.test_logs_path):
            os.remove(self.test_logs_path)

        self.browser.save_screenshot(self.test_logs_path)

