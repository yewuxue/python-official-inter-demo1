#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import unittest,os,time
from common import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


# 当前脚本所在文件绝对路径,其实就是项目目录
absolute_path = os.path.dirname(os.path.realpath(__file__))  #先获取文件路径，再获取上一层目录

def all_case(caseName="case", rule="Test_*.py"):
    '''加载所有的测试用例'''
    case_path = os.path.join(absolute_path, caseName)  # case文件夹，拼接路径

    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("测试用例路径:%s"%case_path)
    testcase = unittest.TestSuite()
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    #print(discover)
    # return discover
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到 testcase
            testcase.addTests(test_case)
    #print(testcase)
    return testcase

def run_case(alll_case, reportName="report"):
    '''执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_path = os.path.join(absolute_path, reportName)  # HTMLreport文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, "result%s.html"%now)
    print("测试报告路径:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(alll_case)
    fp.close()

def latestReport(testReport):
    '''获取最新测试报告'''
    lists=os.listdir(testReport)   #显示测试报告文件夹下得文件
    lists2=sorted(lists)           #排序
    file_new=os.path.join(testReport,lists2[-1])
    return file_new

def sendReport(new_report,host_server,sender_qq,pwd,sender_qq_mail,receivers):
    '''发送最新测试报告'''
    with open(new_report,"rb") as f:
        mail_body=f.read()

    mail_title="自动化测试报告"       #邮件标题
    msg=MIMEMultipart()
    msg["subject"] = Header(mail_title, "utf-8")
    msg["From"] = sender_qq_mail
    #邮件正文
    msg.attach(MIMEText(mail_body,"html","utf-8"))

    # ssl登陆
    smtp = SMTP_SSL(host_server, 465)
    smtp.set_debuglevel(0)  # debug测试
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
    smtp.sendmail(sender_qq_mail,receivers,msg.as_string())
    smtp.quit()



if __name__ == "__main__":
    #1加载用例
    #all_case = all_case()

    # 2执行用例
    run_case(all_case())

    report_path = os.path.join(absolute_path, "report")  # 用例文件夹
    # 3获取最新的测试报告
    new_report = latestReport(report_path)
    #邮箱配置
    host_server="smtp.qq.com"            #smtp邮件服务器地址
    sender_qq="821773282@qq.com"       #发件人的qq
    pwd="xxxxxx"              #授权密码
    sender_qq_mail="821773282@qq.com"  #发件人邮箱
    receivers=["821773282@qq.com","821773282@qq.com"]    #接收人

    # 4发送报告
    sendReport(new_report,host_server,sender_qq,pwd,sender_qq_mail,receivers)
