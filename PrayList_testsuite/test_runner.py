import New_Timestamps
from selenium import webdriver
import TestBase
import unittest

# creating suites out of each module
new_page_suite = New_Timestamps.suite()

# creating a main suite to run
main_suite = unittest.TestSuite()
main_suite.addTest(new_page_suite)

# running main suite
unittest.TextTestRunner(verbosity=2).run(main_suite)

