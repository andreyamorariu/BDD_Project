from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage

# fiecare pagina o sa aiba un fisier
class Sign_in_page(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    PASS_INPUT = (By.XPATH, '//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//span[text() = "Log in"]/parent::button')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[@href ="/forgot-password"]')

    def navigate_to_login_page(self):
        self.driver.get('https://jules.app/sign-in')

    # step(cea mai mica actiune pe care poate sa o faca un user pe o pagina)
    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pass(self, password):
        self.driver.find_element(*self.PASS_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # step definition(o agregare de pasi mici care au logica sa fie sub o singura umbrela/functie)
    def user_login(self, email, password):
        self.set_email(email)
        self.set_pass(password)
        self.click_login()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
