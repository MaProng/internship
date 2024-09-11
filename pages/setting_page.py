from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingPage(Page):

    MAIN_MENU_BUTTON = (By.CSS_SELECTOR, "div.circle-gradient")
    SETTING_BUTTON = (By.CSS_SELECTOR, 'div[class="menu-text-icon-block"] a[href="/settings"]')
    SETTING_OPTIONS = (By.CSS_SELECTOR, "div.setting-text")
    CONNECT_COMPANY_BUTTON = (By.CSS_SELECTOR, 'div[class="settings-block-menu"] a[href="/book-presentation"] div[class="get-free-period menu"]')

    def click_main_menu(self):
        main_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.app.setting_page.MAIN_MENU_BUTTON)
        )
        main_menu.click()
        sleep(10)

    def click_setting(self):
        sleep(10)
        setting_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.app.setting_page.SETTING_BUTTON)
        )
        setting_button.click()
        sleep(10)

    def setting_page_url(self):
        expected_url = 'https://soft.reelly.io/settings'
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL to be {expected_url} but got {current_url}"

    def setting_options(self, amount):
        amount = int(amount)
        options = self.driver.find_elements(*self.SETTING_OPTIONS)
        assert len(options) >= amount, f'Expected {amount} options but got {len(options)}'

    def connect_company_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONNECT_COMPANY_BUTTON)
        )
        assert button is not None, "Connect company button is not available or visible."
