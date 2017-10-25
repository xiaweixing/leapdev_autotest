# -*- coding: utf8 -*-

import unittest
from tests.test_login_page import TestLoginPage
from tests.test_employees_page import TestEmployeesPage


if __name__ == '__main__':
    suite = unittest.TestSuite()

    temp_suite = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
    suite.addTests(temp_suite)
    temp_suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployeesPage)
    suite.addTests(temp_suite)

    unittest.TextTestRunner(verbosity=2).run(suite)