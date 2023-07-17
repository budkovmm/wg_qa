import logging

from src.pages.base import Base
from src.pages.test.locators import WebsiteProgrammingLanguagesLocators


class WebsiteProgrammingLanguages(Base):
    logger = logging.getLogger()

    def __init__(self, driver):
        super().__init__(driver)

    def get_result_table(self):
        return self.driver.find_element(*WebsiteProgrammingLanguagesLocators.result_table)
