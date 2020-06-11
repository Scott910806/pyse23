from xml.dom import minidom

# 打开xml文件
dom = minidom.parse("./data/info.xml")

# 获得文档元素对象
root = dom.documentElement

# 获取一组元素对象
tag_names = root.getElementsByTagName("province")
print(tag_names,type(tag_names),len(tag_names))

# 获取标签对之间的数据
print(tag_names[0].firstChild.data)
print(tag_names[1].firstChild.data)
print(tag_names[2].firstChild.data)

# 获取一组元素对象
user_info = root.getElementsByTagName("login")

# 获取标签属性中的数据
username = user_info[0].getAttribute("username")
print(username)

password = user_info[0].getAttribute("password")
print(password)

username = user_info[1].getAttribute("username")
print(username)

password = user_info[1].getAttribute("password")
print(password)