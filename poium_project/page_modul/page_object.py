from poium import Page, NewPageElement

class BaiduHomePage(Page):

    search_input = NewPageElement(css='#kw', timeout=3, describe='百度搜索框')
    search_button = NewPageElement(css='#su', timeout=3, describe='百度一下按钮')