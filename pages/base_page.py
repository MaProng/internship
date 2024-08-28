from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def input_text(self, text: str, by: By, value: str):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def click(self, by: By, value: str):
        element = self.find_element(by, value)
        element.click()

    def open(self, url: str):
        self.driver.get(url)
