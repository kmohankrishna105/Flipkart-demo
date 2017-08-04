class Resultpage:
    def __init__(self,driver):
        self.driver=driver

    def resultdisplay(self):

        #self.driver.find_element_by_xpath("//h1[@class='_1ZODb3']/span/span").text
        resultcount = self.driver.find_element_by_css_selector("h1._1ZODb3").text
        print resultcount

    def selectproduct(self):
        self.driver.find_element_by_xpath("//div[@class='_3wU53n']").click()
