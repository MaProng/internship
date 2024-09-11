from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text: str, by: By, value: str):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def click(self, by: By, value: str):
        element = self.find_element(by, value)
        element.click()

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            f'Element not clickable by {locator}'
        ).click()

    def open(self, url: str):
        self.driver.get(url)

