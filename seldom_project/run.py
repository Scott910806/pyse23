import seldom



if __name__ == '__main__':
    # 运行测试用例
    seldom.main(path="./test_dir/test_sample.py")

    '''
    seldom.main()  # 默认运行当前测试文件
    seldom.main(path="./")  # 当前目录下的所有测试文件
    seldom.main(path="./test_dir/")  # 指定目录下的所有测试文件
    seldom.main(path="./test_dir/test_sample.py")  # 指定目录下的测试文件

    seldom.main(path="./",
              browser="chrome",
              report=None,
              title="百度测试用例",
              description="测试环境：chrome",
              debug=False,
              rerun=0,
              save_last_run=False,
              driver_path=None,
              grid_url=None,
              timeout=None
    )

说明：

    path ： 指定测试目录或文件。   
    browser : 指定测试浏览器，默认Chrome。
    report : 自定义测试报告的名称，默认格式为2020_04_04_11_55_20_result.html
    title ： 指定测试报告标题。
    description ： 指定测试报告描述。
    debug ： debug模式，设置为True不生成测试HTML测试，默认为False。
    rerun : 设置失败重新运行次数，默认为 0。
    save_last_run : 设置只保存最后一次的结果，默认为False。
    driver_path : 设置浏览器驱动的绝对路径。要和 browser 设置保持一致。
    grid_url : 设置远程节点，selenium Grid doc。
    timeout : 设置超时时间，默认10秒

    '''
