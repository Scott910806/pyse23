'''创建配置文件，配置测试数据路径，可在测试用例文件中直接引用'''
import os

base_path =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 百度搜索测试数据路径
baidu_search_data_path = os.path.join(base_path, "test_data", "baidu_search_data.json")

if __name__ == "__main__":
    print(base_path)
    print(baidu_search_data_path)