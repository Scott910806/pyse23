class BaiduHomePage():

    def __init__(self, driver):
        self.driver = driver

    @property
    def search_input(self):
        # 百度输入框
        return self.driver.find_element_by_css_selector("input#kw")

    @property
    def search_button(self):
        # 百度一下按键
        return self.driver.find_element_by_css_selector("input#su")