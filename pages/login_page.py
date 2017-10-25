# -*- coding: utf8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
from time import sleep
from pages.base import BasePage
from pages.employees_page import EmployeesPage


class LoginPage(BasePage):

    USERNAME = (By.XPATH, "//input[@type='text']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN = (By.XPATH, "//button[text()='Login']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#login-form > fieldset > p")

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.open("/login")

    def enter_username(self, username):
        self.find_element(*LoginPage.USERNAME).clear()
        self.find_element(*LoginPage.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find_element(*LoginPage.PASSWORD).clear()
        self.find_element(*LoginPage.PASSWORD).send_keys(password)

    def click_login_button(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(LoginPage.LOGIN)
            )
        except(TimeoutException, StaleElementReferenceException):
            traceback.print_exc()
        self.find_element(*LoginPage.LOGIN).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def login_with_valid_user(self, username, password):
        self.login(username, password)
        return EmployeesPage(self.driver)

    def login_with_invalid_user(self, username, password):
        self.login(username, password)
        return self.find_element(*LoginPage.ERROR_MESSAGE).text