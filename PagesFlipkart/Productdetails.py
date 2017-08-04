class selproductdetails:
    def __init__(self,driver):
        self.driver=driver

    def product_price(self):

        price = self.driver.find_element_by_css_selector("div._1vC4OE._37U4_g").text
        print price

    def AddtoCart(self):
        self.driver.find_element_by_css_selector("button._2AkmmA._2Npkh4._2MWPVK").click()
