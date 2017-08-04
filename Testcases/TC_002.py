
import unittest
import time
from PagesFlipkart.Searchpage import Search
from common.Driverstart import Browseropen
from PagesFlipkart.Product import Resultpage
from PagesFlipkart.Productdetails import selproductdetails
from PagesFlipkart.CartPage import Cart


class Showprice2(Browseropen,unittest.TestCase):
    def testaddcart(self):

        search=Search(self.driver)
        search.EnterSearchText()
        time.sleep(3)
        search.ClickSearchIcon()


        selproduct=Resultpage(self.driver)
        time.sleep(3)
        selproduct.resultdisplay()
        time.sleep(3)
        selproduct.selectproduct()

        newwindow = self.driver.window_handles[1]
        oldwindow = self.driver.window_handles[0]
        self.driver.switch_to.window(newwindow)
        currenturl = self.driver.current_url
        print(currenturl)

        selproduct=selproductdetails(self.driver)
        time.sleep(3)
        try:

            selproduct.product_price()
            time.sleep(3)
        except:
            print "The price cannot be fetched"

        try:
            selproduct.AddtoCart()
            print "Added to cart"

        except:
            pass
        cadd=Cart(self.driver)

        time.sleep(3)
        self.driver.save_screenshot("D:/jamel.jpg")
        cadd.pinverification()


if __name__=="__main__":
    unittest.main()
