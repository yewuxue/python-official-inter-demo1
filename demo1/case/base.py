#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import logging,os,unittest,json

from common.CommonMethod import CommonMethod
from config.write_excel import write_excel
from log.log import logger

'''获取项目目录，拼接日志文件路径，如果需要用的多处，可以封装成一个函数'''
absolute_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LogFolderPath = os.path.join(absolute_path, "log")
if not os.path.exists(LogFolderPath): os.mkdir(LogFolderPath)#判断是否存在，如果不存在即创建
LogFilePath = os.path.join(LogFolderPath, "Logger.txt")
absolute_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TestDataFile=os.path.join(absolute_path,"testdata.xlsx")

class base(unittest.TestCase,logger):

    def setUp(self):
        '''初始化里面主要做的是获取接口需要的参数，比如：IP、路径、端口号、头文件、方法、数据库连接等数据'''
        # 通过继承调用logger用于在console打印日志
        self.logger = logger(consoleLevel=logging.DEBUG, logFile=LogFilePath, fileLevel=logging.DEBUG)
        self.logger.info('从ini，excel文件中开始读取数据')


        self.host=CommonMethod().Get_Host()
        self.headers= CommonMethod().Get_Headers()
        self.DataType = CommonMethod().Get_DataType()


        if CommonMethod().Get_Token()=="":
            self.headers = CommonMethod().Get_Headers()
        else:
            a = eval(CommonMethod().Get_Headers())
            a["X-Auth-Token"]=CommonMethod().Get_Token()
            self.headers=json.dumps(a)

    def wirte_result(self, res,sheet):
        # 返回结果的行数row_nub
        row_nub = res["rowNum"]
        print("-------------%s"%row_nub)
        wt = write_excel(TestDataFile,sheet)
        wt.write(row_nub, 6,res["expires_in"])  # 写入返回状态码statuscode,第8列


    def tearDown(self):
        '''数据清理工作'''
        pass