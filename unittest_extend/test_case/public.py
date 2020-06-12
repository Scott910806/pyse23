# 定义baidu_search方法
def baidu_search(dr, keyword):
    dr.find_element_by_css_selector("input#kw").send_keys(keyword)
    dr.find_element_by_css_selector("input#su").click()