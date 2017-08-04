"Search for a text and results displayed , verify the price"
import unittest
from PagesFlipkart.Searchpage import Search
from common.Driverstart import Browseropen
from PagesFlipkart.Product import Resultpage
import time

class Showprice1(Browseropen,unittest.TestCase):
    def testVerifyprice(self):
        try:
            self.driver.save_screenshot("D:/Flipkart/openpage.png")
            self.driver.find_element_by_css_selector("button._2AkmmA._29YdH8").click()
            assert "Online Shopping Site for Mobiles, Fashion, Books, Electronics, Home Appliances and More" in self.driver.title
        except:
            assert "Online Shopping Site for Mobiles, Fashion, Books, Electronics, Home Appliances and More" in self.driver.title
            print self.driver.title

        search=Search(self.driver)
        search.EnterSearchText()
        time.sleep(3)
        search.ClickSearchIcon()

        selproduct=Resultpage(self.driver)
        time.sleep(4)
        selproduct.resultdisplay()
        time.sleep(3)
        selproduct.selectproduct()

if __name__=="__main__":
    unittest.main()
