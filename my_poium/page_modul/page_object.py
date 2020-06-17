# import sys
# import os
# dir_path =os.path.abspath(__file__)
# sys.path.append(dir_path)

from poium import Page, PageElement

class BaiduHomePage(Page):

    search_input = PageElement(id_='input#kw', timeout=3, describe='百度搜索框')
    search_button = PageElement(id_='input#su', timeout=3, describe='百度一下按钮') 

