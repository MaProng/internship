from pages.base_page import Page
from pages.log_in_page import LogInPage
from pages.setting_page import SettingPage
class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.log_in_page = LogInPage(driver)
        self.setting_page = SettingPage(driver)
