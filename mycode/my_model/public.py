
class Login():
    '''类的初始化方法'''
    def __init__(self, driver):
        self.driver = driver

    '''定义登录方法'''
    def login(self, username, password):
        dr = self.driver
        elem = dr.find_element_by_css_selector("div#loginDiv > iframe")
        dr.switch_to.frame(elem)
        dr.find_element_by_css_selector("[name = 'email']").send_keys(username)
        dr.find_element_by_css_selector("[name = 'password']").send_keys(password)

    '''定义关闭浏览器方法'''
    def close_browser(self):
        self.driver.quit()

    '''百度搜索方法'''
def baidu_search(dr, keyword):
    dr.find_element_by_css_selector("input#kw").send_keys(keyword)
    dr.find_element_by_css_selector("input#su").click()