# -*- coding: utf8 -*-

from selenium import webdriver
import unittest
from time import sleep
from datetime import datetime
from pages.login_page import LoginPage
from pages.employees_page import EmployeesPage


class TestEmployeesPage(unittest.TestCase):
    "Test Employees Page"

    page_employees = 0

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        page_login = LoginPage(self.driver)
        TestEmployeesPage.page_employees = page_login.login_with_valid_user("Luke", "Skywalker")

    def tearDown(self):
        self.driver.quit()

    def test_001_add_employee(self):
        #print("test add employees")
        TestEmployeesPage.page_employees.add_employee("test", "test", "2017-10-25", "auto@test.com")
        #TODO - add assertion

    def test_002_edit_employee(self):
        #print("test edit employees")
        TestEmployeesPage.page_employees.edit_employee("test", "test", "2017-11-11", "auto@testtest.com")
        # TODO - add assertion

    def test_003_delete_employee(self):
        #print("test delete employees")
        TestEmployeesPage.page_employees.delete_employee("test", "test")
        # TODO - add assertion