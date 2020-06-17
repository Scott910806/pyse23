import csv
import codecs
from itertools import islice

# 打开并读取csv文件
data = csv.reader(codecs.open('./data/user_data.csv','r','utf_8_sig'))

# 创建接收数据的数组
users = []

# 循环读取内容
for line in islice(data, 1, None): # 忽略掉首行标题
    users.append(line)

print(users)