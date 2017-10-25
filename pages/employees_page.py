# -*- coding: utf8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import traceback
from time import sleep
from pages.base import BasePage


class EmployeesPage(BasePage):

    GREETINGS = (By.ID, "greetings")
    ADD = (By.ID, "bAdd")
    EDIT = (By.ID, "bEdit")
    DELETE = (By.ID, "bDelete")
    FIRSTNAME = (By.XPATH, "//input[@ng-model='selectedEmployee.firstName']")
    LASTNAME = (By.XPATH, "//input[@ng-model='selectedEmployee.lastName']")
    STARTDATE = (By.XPATH, "//input[@ng-model='selectedEmployee.startDate']")
    EMAIL = (By.XPATH, "//input[@ng-model='selectedEmployee.email']")
    CONFIRM_ADD = (By.XPATH, "//button[text()='Add']")
    CONFIRM_UPDATE = (By.XPATH, "//button[text()='Update']")

    def get_greetings(self):
        return self.find_element(*EmployeesPage.GREETINGS).text

    def click_add_button(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(EmployeesPage.ADD)
            )
        except(TimeoutException, StaleElementReferenceException):
            traceback.print_exc()
        self.find_element(*EmployeesPage.ADD).click()

    def click_edit_button(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(EmployeesPage.EDIT)
            )
        except(TimeoutException, StaleElementReferenceException):
            traceback.print_exc()
        self.find_element(*EmployeesPage.EDIT).click()

    def click_delete_button(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(EmployeesPage.DELETE)
            )
        except(TimeoutException, StaleElementReferenceException):
            traceback.print_exc()
        self.find_element(*EmployeesPage.DELETE).click()

    def enter_first_name(self, firstname):
        self.find_element(*EmployeesPage.FIRSTNAME).clear()
        self.find_element(*EmployeesPage.FIRSTNAME).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.find_element(*EmployeesPage.LASTNAME).clear()
        self.find_element(*EmployeesPage.LASTNAME).send_keys(lastname)

    def enter_start_date(self, startdate):
        self.find_element(*EmployeesPage.STARTDATE).clear()
        self.find_element(*EmployeesPage.STARTDATE).send_keys(startdate)

    def enter_email(self, email):
        self.find_element(*EmployeesPage.EMAIL).clear()
        self.find_element(*EmployeesPage.EMAIL).send_keys(email)

    def click_confirm_add(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(EmployeesPage.CONFIRM_ADD)
            )
        except(TimeoutException, StaleElementReferenceException):
            traceback.print_exc()
        self.find_element(*EmployeesPage.CONFIRM_ADD).click()

    def click_confirm_update(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(EmployeesPage.CONFIRM_UPDATE)
            )
        except(TimeoutException, StaleElementReferenceException):
            traceback.print_exc()
        self.find_element(*EmployeesPage.CONFIRM_UPDATE).click()

    def click_employee_in_list(self, firstname, lastname):
        xpath_employee_record = "//li[contains(text(), '" + firstname + " " + lastname + "')]"
        EMPLOYEE_RECORD = (By.XPATH, xpath_employee_record)
        element = self.find_element(*EMPLOYEE_RECORD)
        element.location_once_scrolled_into_view
        element.click()

    def add_employee(self, firstname, lastname, startdate, email):
        self.click_add_button()
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_start_date(startdate)
        self.enter_email(email)
        self.click_confirm_add()

    def edit_employee(self, firstname, lastname, startdate, email):
        self.click_employee_in_list(firstname, lastname)
        self.click_edit_button()
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_start_date(startdate)
        self.enter_email(email)
        self.click_confirm_update()

    def delete_employee(self, firstname, lastname):
        self.click_employee_in_list(firstname, lastname)
        self.click_delete_button()
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.alert_is_present()
            )
        except(TimeoutException, StaleElementReferenceException):
            traceback.print_exc()
        alert = self.driver.switch_to.alert
        #print(alert.text)
        alert.accept()

