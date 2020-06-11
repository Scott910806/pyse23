import json

# 打开json文件
with open('./data/user_data.json','r') as f:
    data = f.read()

# data类型为字符串
print(data,type(data)) 

# 解析json格式的字符串
user_list = json.loads(data) 
print(user_list,type(user_list))