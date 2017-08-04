class Cart:
    def __init__(self,driver):
        self.driver=driver


    def pinverification(self):
        self.driver.find_element_by_css_selector("input._3X4tVa[placeholder='Enter Delivery Pincode']").send_keys(
            "500050")

        self.driver.find_element_by_css_selector("span._2aK_gu").click()
