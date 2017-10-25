# -*- coding: utf8 -*-

from selenium import webdriver
import unittest
from time import sleep
from pages.login_page import LoginPage
from pages.employees_page import EmployeesPage


class TestLoginPage(unittest.TestCase):
    "Test Login Page"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_with_valid_user(self):
        #print("test login page with valid user")
        page_login = LoginPage(self.driver)
        page_employees = page_login.login_with_valid_user("Luke", "Skywalker")
        self.assertEqual("Hello Luke", page_employees.get_greetings())

    def test_login_with_invalid_user(self):
        #print("test login page with invalid user")
        page_login = LoginPage(self.driver)
        error_msg = page_login.login_with_invalid_user("test", "testtest")
        self.assertEqual("Invalid username or password!", error_msg)