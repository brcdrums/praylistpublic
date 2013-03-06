import unittest
from selenium import webdriver
import TestBase

class NewTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        self.driver.get(TestBase.newURL)
        self.assertTrue("new" in self.driver.title)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(NewTest))
    return suite

if __name__ == '__main__':
   unittest.main()