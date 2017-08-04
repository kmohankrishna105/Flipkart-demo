class Search:
    def __init__(self,driver):
        self.driver=driver

    def EnterSearchText(self):
        self.driver.find_element_by_name("q").send_keys("Iphone")

    def ClickSearchIcon(self):
        self.driver.find_element_by_css_selector("svg._2BhAHa").click()
