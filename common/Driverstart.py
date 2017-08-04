
import unittest
from selenium import webdriver

path = "C:/Python34/chromedriver.exe"
import time

class Browseropen(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=path)
        self.driver.get("https://www.flipkart.com/")
        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.TestCase
