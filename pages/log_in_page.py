from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogInPage(Page):

    USER_EMAIL = (By.ID, 'email-2')
    USER_PASSWORD = (By.ID, 'field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a.login-button.w-button")

    def open_log_in_page(self):
        self.open('https://soft.reelly.io/')

    def login_user(self, email, password):
        self.input_text(email,  *self.USER_EMAIL)
        self.input_text(password, *self.USER_PASSWORD)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )

        self.click(*self.CONTINUE_BUTTON)
