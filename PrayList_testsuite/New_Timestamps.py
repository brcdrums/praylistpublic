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

    def test_timestamp(self):
        self.driver.get(TestBase.newURL)
        timestamps = self.driver.find_elements_by_class_name("timestamp")
        print "length of timestamps = " + str(len(timestamps))
        for stamp, next in timestampgen(timestamps):
            current_item = stamp.text
            next_item = next.text
            print "current item = " + current_item + "next item = " + next_item
            current_item_cleaned = TestBase.equate_time(current_item)
            next_item_cleaned = TestBase.equate_time(next_item)
            self.assertTrue(current_item_cleaned <= next_item_cleaned)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(NewTest))
    return suite

def timestampgen(timestamps):
    timestamp_iter = iter(timestamps)
    current = timestamp_iter.next()
    for next in timestamp_iter:
        yield current, next
        current = next

if __name__ == '__main__':
   unittest.main()