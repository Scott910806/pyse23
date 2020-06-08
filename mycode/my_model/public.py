import time

class Login():
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        dr = self.driver
        elem = dr.find_element_by_css_selector("div#loginDiv > iframe")
        dr.switch_to.frame(elem)
        dr.find_element_by_css_selector("[name = 'email']").send_keys(username)
        dr.find_element_by_css_selector("[name = 'password']").send_keys(password)

    def close_window(self):
        self.driver.quit()