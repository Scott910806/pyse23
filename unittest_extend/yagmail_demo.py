import yagmail
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

def send_mail(report):
    '''发送邮件到指定邮箱'''
    yag = yagmail.SMTP(user='yxma2010@126.com', password='pihai123456789', host='smtp.126.com')
    contents_text = ["python + selenium + unittest + ddt 测试报告，请查看附件（下载后查看）"]
    yag.send('yxma2010@126.com', subject='automation test report', contents=contents_text, attachments=report)
    yag.close()
    print("邮件已发送")

if __name__ == "__main__":
    
    # 组装test suit
    suit = unittest.defaultTestLoader.discover(
        start_dir = './test_case',
        pattern = 'parameterized*.py'
    )

    current_time = time.strftime('%y_%m_%d_%H_%M_%S')
    report_path = './test_reports/'+current_time+' result.html'
    with open(report_path,'wb') as f:
        runner = HTMLTestRunner(stream=f, title='parameterized test demo', description='automation test project')
        runner.run(suit, rerun=1, save_last_run=False)

# 发送邮件
send_mail(report_path)
