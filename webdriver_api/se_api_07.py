'''
上传文件,使用input标签实现的上传功能，可以直接将需要上传的文件路径，传给input标签元素即可
'''
import os
import time
from selenium import webdriver

path_01 = os.path.dirname(os.path.abspath(__file__)) #获取当前文件所在文件夹的路径
print(path_01)
path_02 = os.path.dirname(path_01) #获取上一级文件夹路径
print(path_02)
upload_html_path = os.path.join(path_02,"html","upload.html") #通过拼接获取目标文件路径
print(upload_html_path)

dr = webdriver.Chrome()
dr.get(upload_html_path)
time.sleep(2)

dr.find_element_by_name("file").send_keys("D:\\yxma\\learn\\upload_practice.txt")